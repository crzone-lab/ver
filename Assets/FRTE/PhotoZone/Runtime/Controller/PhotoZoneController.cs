using System;
using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Implements IPhotoZoneController.
    /// Manages active PhotoZone preset and layer configurations.
    /// </summary>
    public sealed class PhotoZoneController : IPhotoZoneController
    {
        private readonly IPhotoZoneProvider _provider;
        private readonly Dictionary<PhotoZoneLayer, bool> _layerVisibilities = new Dictionary<PhotoZoneLayer, bool>();

        public PhotoZonePreset CurrentPreset { get; private set; }

        public PhotoZoneController(IPhotoZoneProvider provider)
        {
            _provider = provider ?? throw new ArgumentNullException(nameof(provider));

            // Initialize all layers as visible
            foreach (PhotoZoneLayer layer in Enum.GetValues(typeof(PhotoZoneLayer)))
            {
                _layerVisibilities[layer] = true;
            }
        }

        public bool ApplyPhotoZone(string presetId)
        {
            if (!_provider.TryGetById(presetId, out var preset))
            {
                Debug.LogWarning($"[PhotoZoneController] Preset ID '{presetId}' not found.");
                return false;
            }

            var previousId = CurrentPreset != null ? CurrentPreset.Id : string.Empty;
            CurrentPreset = preset;

            // Broadcast Event
            FRTESdkManager.Instance.EventBus?.Publish(new PhotoZoneChangedEvent
            {
                PreviousId = previousId,
                CurrentId = preset.Id
            });

            Debug.Log($"[PhotoZone] Applied preset '{preset.Id}'");
            return true;
        }

        public void ClearPhotoZone()
        {
            if (CurrentPreset == null) return;

            var clearedId = CurrentPreset.Id;
            CurrentPreset = null;

            FRTESdkManager.Instance.EventBus?.Publish(new PhotoZoneClearedEvent
            {
                ClearedId = clearedId
            });

            Debug.Log("[PhotoZone] PhotoZone cleared.");
        }

        public void SetLayerVisibility(PhotoZoneLayer layer, bool visible)
        {
            _layerVisibilities[layer] = visible;
            
            FRTESdkManager.Instance.EventBus?.Publish(new PhotoZoneLayerChangedEvent
            {
                Layer = layer,
                IsVisible = visible
            });
        }

        public bool IsLayerVisible(PhotoZoneLayer layer)
        {
            if (_layerVisibilities.TryGetValue(layer, out bool visible))
            {
                return visible;
            }
            return true;
        }
    }

    // --- PHOTOZONE EVENTS ---
    public struct PhotoZoneChangedEvent { public string PreviousId; public string CurrentId; }
    public struct PhotoZoneClearedEvent { public string ClearedId; }
    public struct PhotoZoneLayerChangedEvent { public PhotoZoneLayer Layer; public bool IsVisible; }
}
