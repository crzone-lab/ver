using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;
using FRTE.AI;

namespace FRTE.Decoration
{
    /// <summary>
    /// Implements the layered accessory decoration manager.
    /// Handles instantiation, lifecycle, and dynamic tracking of decorations mapping to AI coordinates.
    /// </summary>
    public sealed class DecorationManager : IDecorationEngine, IPlugin
    {
        public string PluginId => "FRTE.DecorationEngine";
        public bool IsEnabled { get; private set; }

        private readonly Dictionary<string, DecorationItem> _activeDecorations = new Dictionary<string, DecorationItem>();
        private Transform _parentContainer;

        private struct DecorationItem
        {
            public GameObject Instance;
            public LandmarkType Anchor;
            public Vector3 Offset;
            public int SortingOrder;
        }

        public void Initialize(FRTEContainer container)
        {
            container.Register<IDecorationEngine>(this);

            // Create a runtime container under which all instantiated decoration items will live
            var go = new GameObject("FRTE_DecorationContainer");
            _parentContainer = go.transform;
            Object.DontDestroyOnLoad(go);
        }

        public void Enable()
        {
            IsEnabled = true;
            if (_parentContainer != null)
            {
                _parentContainer.gameObject.SetActive(true);
            }
        }

        public void Disable()
        {
            IsEnabled = false;
            ClearDecorations();
            if (_parentContainer != null)
            {
                _parentContainer.gameObject.SetActive(false);
            }
        }

        public void AddDecoration(string key, GameObject prefab, LandmarkType anchor, int sortingOrder, Vector3 offset)
        {
            if (prefab == null) return;

            // Remove existing item if key overlaps
            RemoveDecoration(key);

            var go = Object.Instantiate(prefab, _parentContainer);
            go.name = $"Deco_{key}";

            // Apply sorting order on all SpriteRenderers inside the item
            var spriteRenderers = go.GetComponentsInChildren<SpriteRenderer>(true);
            for (int i = 0; i < spriteRenderers.Length; i++)
            {
                spriteRenderers[i].sortingOrder = sortingOrder;
            }

            var item = new DecorationItem
            {
                Instance = go,
                Anchor = anchor,
                Offset = offset,
                SortingOrder = sortingOrder
            };

            _activeDecorations.Add(key, item);
        }

        public void RemoveDecoration(string key)
        {
            if (_activeDecorations.TryGetValue(key, out var item))
            {
                if (item.Instance != null)
                {
                    Object.DestroyImmediate(item.Instance);
                }
                _activeDecorations.Remove(key);
            }
        }

        public void ClearDecorations()
        {
            foreach (var item in _activeDecorations.Values)
            {
                if (item.Instance != null)
                {
                    Object.DestroyImmediate(item.Instance);
                }
            }
            _activeDecorations.Clear();
        }

        public void UpdateDecorationPositions(LandmarkData[] landmarks, float meshWidth, float meshHeight)
        {
            if (landmarks == null || landmarks.Length == 0) return;

            foreach (var item in _activeDecorations.Values)
            {
                if (item.Instance == null) continue;

                // Find corresponding landmark
                bool found = false;
                for (int i = 0; i < landmarks.Length; i++)
                {
                    if (landmarks[i].Type == item.Anchor)
                    {
                        var lm = landmarks[i];
                        // Map normalized [0, 1] UV back to mesh local coordinates (centered)
                        float localX = (lm.Position.x - 0.5f) * meshWidth;
                        float localY = (lm.Position.y - 0.5f) * meshHeight;

                        item.Instance.transform.localPosition = new Vector3(localX, localY, 0f) + item.Offset;
                        found = true;
                        break;
                    }
                }

                item.Instance.SetActive(found);
            }
        }
    }
}
