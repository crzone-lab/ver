using UnityEngine;
using FRTE.Core;
using FRTE.Physics;

namespace FRTE.Materials
{
    /// <summary>
    /// Coordinates loading and hot-swapping squishy material presets.
    /// Drives physics parameter receivers, audio service clips, and visual properties.
    /// </summary>
    public sealed class MaterialPresetController : IMaterialPresetController
    {
        private readonly IMaterialPresetProvider _provider;
        private readonly ISquishySettingsRepository _settingsRepo;
        private readonly ISquishyAudioService _audioService;

        private ISquishyParameterReceiver _parameterReceiver;
        private DeformableJellyRenderer _jellyRenderer;
        private SquishyUserSettings _userSettings;

        // Reference constants for parameter multipliers mapping
        private const float BaseRadius = 0.15f;
        private const float BaseTouchStrength = 15f;
        private const float BaseDragStrength = 20f;
        private const float BaseMaxDisplacement = 0.15f;
        private const float BaseEdgeResistance = 2.0f;
        private const float BaseForceLimit = 50f;

        public SquishyMaterialPreset CurrentPreset { get; private set; }

        public MaterialPresetController(
            IMaterialPresetProvider provider,
            ISquishySettingsRepository settingsRepo,
            ISquishyAudioService audioService)
        {
            _provider = provider ?? throw new System.ArgumentNullException(nameof(provider));
            _settingsRepo = settingsRepo ?? throw new System.ArgumentNullException(nameof(settingsRepo));
            _audioService = audioService ?? throw new System.ArgumentNullException(nameof(audioService));

            _userSettings = _settingsRepo.Load();
        }

        /// <summary>
        /// Links the controller with active runtime scene components.
        /// </summary>
        public void BindRenderers(ISquishyParameterReceiver receiver, DeformableJellyRenderer renderer)
        {
            _parameterReceiver = receiver;
            _jellyRenderer = renderer;

            // Apply last selected preset automatically
            if (_userSettings != null && !string.IsNullOrEmpty(_userSettings.SelectedPresetId))
            {
                ApplyPreset(_userSettings.SelectedPresetId);
            }
            else
            {
                ApplyDefaultPreset();
            }
        }

        public bool ApplyPreset(string presetId)
        {
            if (_provider.TryGetById(presetId, out var preset))
            {
                return ApplyPreset(preset, animateTransition: true);
            }
            Debug.LogWarning($"[MaterialController] Preset ID '{presetId}' not found. Restoring default.");
            ApplyDefaultPreset();
            return false;
        }

        public bool ApplyPreset(SquishyMaterialPreset preset, bool animateTransition)
        {
            if (preset == null) return false;

            string previousId = CurrentPreset != null ? CurrentPreset.Id : string.Empty;
            CurrentPreset = preset;

            // 1. Map SquishyPhysicsParameters to SquishyRuntimeParameters
            var p = preset.Physics;
            var runtimeParams = new SquishyRuntimeParameters
            {
                TouchRadius = Mathf.Max(0.01f, p.TouchRadiusMultiplier > 0.001f ? p.TouchRadiusMultiplier * BaseRadius : p.TouchRadiusMultiplier),
                TouchStrength = Mathf.Max(0.1f, p.TouchStrengthMultiplier > 0.001f ? p.TouchStrengthMultiplier * BaseTouchStrength : p.TouchStrength),
                DragStrength = Mathf.Max(0.1f, p.DragStrengthMultiplier > 0.001f ? p.DragStrengthMultiplier * BaseDragStrength : p.DragStrength),
                SpringStrength = Mathf.Clamp(p.SpringStrength, 1f, 250f),
                NeighborSpringStrength = Mathf.Clamp(p.NeighborSpringStrength, 1f, 250f),
                Damping = Mathf.Clamp(p.Damping, 0.1f, 50f),
                Mass = Mathf.Clamp(p.Mass, 0.05f, 5f),
                MaxDisplacement = Mathf.Max(0.01f, p.MaxDisplacementMultiplier > 0.001f ? p.MaxDisplacementMultiplier * BaseMaxDisplacement : p.MaxDisplacementMultiplier),
                EdgeResistance = Mathf.Max(0.1f, p.EdgeResistanceMultiplier > 0.001f ? p.EdgeResistanceMultiplier * BaseEdgeResistance : p.EdgeResistanceMultiplier),
                MultiTouchForceLimit = Mathf.Max(1f, p.MultiTouchForceLimitMultiplier > 0.001f ? p.MultiTouchForceLimitMultiplier * BaseForceLimit : p.MultiTouchForceLimitMultiplier),
                WobbleAmount = Mathf.Max(0f, p.WobbleAmount),
                WobbleFrequency = Mathf.Max(0f, p.WobbleFrequency),
                RecoverySpeed = Mathf.Max(0.1f, p.RecoverySpeed),
                CreepRate = Mathf.Max(0f, p.HoldResponse * 2f),
                CreepRecoveryRate = Mathf.Max(0.1f, p.RecoverySpeed * 0.5f)
            };

            // 2. Drive the active physics parameter receiver (Simulation)
            if (_parameterReceiver != null)
            {
                var curve = AnimationCurve.EaseInOut(0f, 0f, 1f, 1f);
                var options = new MaterialTransitionOptions
                {
                    Animate = animateTransition,
                    Duration = 0.3f, // 0.3s transition window
                    Curve = curve,
                    PreserveCurrentDeformation = true // Smooth continuity
                };
                _parameterReceiver.ApplyParameters(runtimeParams, options);
            }

            // 3. Configure audio parameters
            _audioService.SetAudioParameters(preset.Audio);

            // 4. Configure visual parameters
            if (_jellyRenderer != null)
            {
                bool fxEnabled = _userSettings != null ? _userSettings.VisualEffectsEnabled : true;
                _jellyRenderer.ApplyVisuals(preset.Visual, fxEnabled);
            }

            // 5. Update user settings cache and save
            if (_userSettings != null)
            {
                _userSettings.SelectedPresetId = preset.Id;
                _settingsRepo.Save(_userSettings);
            }

            // 6. Broadcast event through SDK Event Bus
            var eventBus = FRTESdkManager.Instance.EventBus;
            if (eventBus != null)
            {
                eventBus.Publish(new MaterialPresetChangedEvent
                {
                    PreviousId = previousId,
                    CurrentId = preset.Id
                });
            }

            return true;
        }

        public void ApplyDefaultPreset()
        {
            var defaultPreset = _provider.GetDefault();
            if (defaultPreset != null)
            {
                ApplyPreset(defaultPreset, animateTransition: false);
            }
        }
    }

    /// <summary>
    /// Event broadcast when the active material preset changes.
    /// </summary>
    public struct MaterialPresetChangedEvent
    {
        public string PreviousId;
        public string CurrentId;
    }
}
