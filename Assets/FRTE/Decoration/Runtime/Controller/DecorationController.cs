using System;
using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// Implements IDecorationController.
    /// Manages active decoration placements, locks, limits, sorting orders, and landmark anchors.
    /// </summary>
    public sealed class DecorationController : IDecorationController
    {
        private readonly IDecorationPresetProvider _presetProvider;
        private readonly List<DecorationInstanceData> _instances = new List<DecorationInstanceData>();
        
        private const int MaxDecorationsCount = 30;

        public string SelectedInstanceId { get; set; } = string.Empty;
        public IReadOnlyList<DecorationInstanceData> CurrentDecorations => _instances;

        public DecorationController(IDecorationPresetProvider provider)
        {
            _presetProvider = provider ?? throw new ArgumentNullException(nameof(provider));
        }

        public string AddDecoration(string presetId)
        {
            if (_instances.Count >= MaxDecorationsCount)
            {
                Debug.LogWarning($"[DecorationController] Maximum limit of {MaxDecorationsCount} decorations reached. Cannot add more.");
                return string.Empty;
            }

            if (!_presetProvider.TryGetById(presetId, out var preset))
            {
                Debug.LogError($"[DecorationController] Preset ID '{presetId}' not found.");
                return string.Empty;
            }

            // Create Instance
            var instance = new DecorationInstanceData
            {
                InstanceId = Guid.NewGuid().ToString(),
                PresetId = preset.Id,
                NormalizedPosition = preset.DefaultNormalizedPosition,
                Scale = preset.DefaultScale,
                Rotation = preset.DefaultRotation,
                SortingOrder = preset.DefaultSortingOrder,
                FlipX = false,
                IsVisible = true
            };

            // Evaluate Anchor Placement if face data is resolved
            var landmarkProvider = FRTESdkManager.Instance.Container.Resolve<IFaceLandmarkProvider>();
            if (landmarkProvider != null && landmarkProvider.HasValidFace && preset.AnchorType != DecorationAnchorType.Free)
            {
                if (landmarkProvider.TryGetLandmarks(out var face))
                {
                    switch (preset.AnchorType)
                    {
                        case DecorationAnchorType.HeadTop:
                            instance.NormalizedPosition = face.HeadTop;
                            break;
                        case DecorationAnchorType.Forehead:
                            instance.NormalizedPosition = face.Forehead;
                            break;
                        case DecorationAnchorType.EyesCenter:
                            instance.NormalizedPosition = (face.LeftEye + face.RightEye) * 0.5f;
                            instance.Rotation = face.FaceRotation;
                            break;
                        case DecorationAnchorType.LeftCheek:
                            instance.NormalizedPosition = face.LeftCheek;
                            break;
                        case DecorationAnchorType.RightCheek:
                            instance.NormalizedPosition = face.RightCheek;
                            break;
                        case DecorationAnchorType.Chin:
                            instance.NormalizedPosition = face.Chin;
                            break;
                    }
                }
            }

            _instances.Add(instance);
            SelectedInstanceId = instance.InstanceId;

            // Broadcast Event
            FRTESdkManager.Instance.EventBus?.Publish(new DecorationAddedEvent { InstanceId = instance.InstanceId, PresetId = presetId });
            FRTESdkManager.Instance.EventBus?.Publish(new DecorationSelectedEvent { InstanceId = instance.InstanceId });

            return instance.InstanceId;
        }

        public void MoveDecoration(string instanceId, Vector2 delta)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.NormalizedPosition += delta;

            // Prevent going completely off-screen bounds
            inst.NormalizedPosition.x = Mathf.Clamp(inst.NormalizedPosition.x, -2f, 2f);
            inst.NormalizedPosition.y = Mathf.Clamp(inst.NormalizedPosition.y, -2f, 2f);

            NotifyChange(instanceId);
        }

        public void RotateDecoration(string instanceId, float deltaAngle)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.Rotation = (inst.Rotation + deltaAngle) % 360f;
            if (inst.Rotation < 0f) inst.Rotation += 360f;

            NotifyChange(instanceId);
        }

        public void ScaleDecoration(string instanceId, Vector2 deltaScale)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.Scale += deltaScale;
            inst.Scale.x = Mathf.Clamp(inst.Scale.x, 0.1f, 5.0f);
            inst.Scale.y = Mathf.Clamp(inst.Scale.y, 0.1f, 5.0f);

            NotifyChange(instanceId);
        }

        public void FlipDecoration(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.FlipX = !inst.FlipX;
            NotifyChange(instanceId);
        }

        public void DeleteDecoration(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            _instances.Remove(inst);
            if (SelectedInstanceId == instanceId)
            {
                SelectedInstanceId = string.Empty;
                FRTESdkManager.Instance.EventBus?.Publish(new DecorationSelectedEvent { InstanceId = string.Empty });
            }

            FRTESdkManager.Instance.EventBus?.Publish(new DecorationRemovedEvent { InstanceId = instanceId });
        }

        public void DuplicateDecoration(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            if (_instances.Count >= MaxDecorationsCount) return;

            var copy = new DecorationInstanceData
            {
                InstanceId = Guid.NewGuid().ToString(),
                PresetId = inst.PresetId,
                NormalizedPosition = inst.NormalizedPosition + new Vector2(0.05f, -0.05f), // offset slightly
                Scale = inst.Scale,
                Rotation = inst.Rotation,
                SortingOrder = inst.SortingOrder + 1,
                FlipX = inst.FlipX,
                IsVisible = inst.IsVisible
            };

            _instances.Add(copy);
            SelectedInstanceId = copy.InstanceId;

            FRTESdkManager.Instance.EventBus?.Publish(new DecorationAddedEvent { InstanceId = copy.InstanceId, PresetId = copy.PresetId });
            FRTESdkManager.Instance.EventBus?.Publish(new DecorationSelectedEvent { InstanceId = copy.InstanceId });
        }

        public void SendToFront(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            int maxOrder = -100;
            for (int i = 0; i < _instances.Count; i++)
            {
                if (_instances[i].SortingOrder > maxOrder) maxOrder = _instances[i].SortingOrder;
            }

            inst.SortingOrder = Mathf.Clamp(maxOrder + 1, -100, 100);
            NotifyChange(instanceId);
        }

        public void SendToBack(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            int minOrder = 100;
            for (int i = 0; i < _instances.Count; i++)
            {
                if (_instances[i].SortingOrder < minOrder) minOrder = _instances[i].SortingOrder;
            }

            inst.SortingOrder = Mathf.Clamp(minOrder - 1, -100, 100);
            NotifyChange(instanceId);
        }

        public void SendForward(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.SortingOrder = Mathf.Clamp(inst.SortingOrder + 1, -100, 100);
            NotifyChange(instanceId);
        }

        public void SendBackward(string instanceId)
        {
            var inst = FindInstance(instanceId);
            if (inst == null) return;

            inst.SortingOrder = Mathf.Clamp(inst.SortingOrder - 1, -100, 100);
            NotifyChange(instanceId);
        }

        public void ClearAll()
        {
            _instances.Clear();
            SelectedInstanceId = string.Empty;
            FRTESdkManager.Instance.EventBus?.Publish(new DecorationSelectedEvent { InstanceId = string.Empty });
        }

        private DecorationInstanceData FindInstance(string id)
        {
            if (string.IsNullOrEmpty(id)) return null;
            for (int i = 0; i < _instances.Count; i++)
            {
                if (_instances[i].InstanceId == id) return _instances[i];
            }
            return null;
        }

        private void NotifyChange(string id)
        {
            FRTESdkManager.Instance.EventBus?.Publish(new DecorationChangedEvent { InstanceId = id });
        }
    }

    // --- DECORATION EVENTS ---
    public struct DecorationAddedEvent { public string InstanceId; public string PresetId; }
    public struct DecorationRemovedEvent { public string InstanceId; }
    public struct DecorationSelectedEvent { public string InstanceId; }
    public struct DecorationChangedEvent { public string InstanceId; }
}
