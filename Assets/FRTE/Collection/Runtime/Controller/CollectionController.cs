using System;
using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;
using FRTE.Surprise;

namespace FRTE.Collection
{
    /// <summary>
    /// Implements ICollectionController.
    /// Manages discovery entries, counts, UTC dates, and saves.
    /// </summary>
    public sealed class CollectionController : ICollectionController
    {
        private readonly ICollectionRepository _repository;
        private readonly Dictionary<string, CollectionEntryData> _entries = new Dictionary<string, CollectionEntryData>();

        public CollectionController(ICollectionRepository repo)
        {
            _repository = repo ?? throw new ArgumentNullException(nameof(repo));

            LoadData();

            // Subscribe to Surprise Discovery Event
            FRTESdkManager.Instance.EventBus?.Subscribe<SurpriseEventDiscoveredEvent>(OnSurpriseDiscovered);
        }

        public bool IsDiscovered(string eventId)
        {
            if (_entries.TryGetValue(eventId, out var ent))
            {
                return ent.IsDiscovered;
            }
            return false;
        }

        public void RegisterDiscovery(string eventId, string relatedFruitId)
        {
            if (string.IsNullOrEmpty(eventId)) return;

            bool isNew = false;
            if (!_entries.TryGetValue(eventId, out var ent))
            {
                ent = new CollectionEntryData
                {
                    EventId = eventId,
                    IsDiscovered = true,
                    DiscoveryCount = 1,
                    FirstDiscoveredUtc = DateTime.UtcNow.ToString("o"),
                    LastDiscoveredUtc = DateTime.UtcNow.ToString("o"),
                    RelatedFruitId = relatedFruitId
                };
                _entries.Add(eventId, ent);
                isNew = true;
            }
            else
            {
                if (!ent.IsDiscovered)
                {
                    ent.IsDiscovered = true;
                    ent.FirstDiscoveredUtc = DateTime.UtcNow.ToString("o");
                    isNew = true;
                }
                ent.DiscoveryCount++;
                ent.LastDiscoveredUtc = DateTime.UtcNow.ToString("o");
                if (string.IsNullOrEmpty(ent.RelatedFruitId))
                {
                    ent.RelatedFruitId = relatedFruitId;
                }
            }

            SaveData();

            // Broadcast Event
            FRTESdkManager.Instance.EventBus?.Publish(new CollectionUpdatedEvent
            {
                EventId = eventId,
                IsNewDiscovery = isNew,
                TotalDiscovered = GetDiscoveredCount()
            });

            Debug.Log($"[Collection] Discovered event '{eventId}' (New: {isNew}, Count: {ent.DiscoveryCount})");
        }

        public IReadOnlyList<CollectionEntryData> GetEntries()
        {
            var list = new List<CollectionEntryData>(_entries.Values);
            return list;
        }

        public void ClearAll()
        {
            _entries.Clear();
            _repository.Reset();
            
            FRTESdkManager.Instance.EventBus?.Publish(new CollectionUpdatedEvent
            {
                EventId = "",
                IsNewDiscovery = false,
                TotalDiscovered = 0
            });
        }

        private void OnSurpriseDiscovered(SurpriseEventDiscoveredEvent evt)
        {
            RegisterDiscovery(evt.EventId, evt.RelatedFruitId);
        }

        private void LoadData()
        {
            _entries.Clear();
            var data = _repository.Load();
            if (data == null || data.Entries == null) return;

            for (int i = 0; i < data.Entries.Count; i++)
            {
                var ent = data.Entries[i];
                if (ent == null || string.IsNullOrEmpty(ent.EventId)) continue;
                _entries[ent.EventId] = ent;
            }
        }

        private void SaveData()
        {
            var data = new CollectionSaveData();
            data.Entries.AddRange(_entries.Values);
            _repository.Save(data);
        }

        private int GetDiscoveredCount()
        {
            int count = 0;
            foreach (var ent in _entries.Values)
            {
                if (ent.IsDiscovered) count++;
            }
            return count;
        }
    }

    // --- COLLECTION EVENTS ---
    public struct CollectionUpdatedEvent
    {
        public string EventId;
        public bool IsNewDiscovery;
        public int TotalDiscovered;
    }
}
