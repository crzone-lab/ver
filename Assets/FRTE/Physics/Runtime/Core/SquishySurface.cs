using System;
using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Physics
{
    /// <summary>
    /// Coordinates input, simulation steps, dynamic mesh updates, and haptic feedback triggers.
    /// Implements ISquishySurface.
    /// </summary>
    [RequireComponent(typeof(SquishyMeshController), typeof(SquishyInputProvider))]
    public sealed class SquishySurface : MonoBehaviour, ISquishySurface, ISquishyParameterReceiver
    {
        private bool _isInitialized;
        private SquishySimulation _simulation;
        private SquishyMeshController _meshController;
        private SquishyInputProvider _inputProvider;
        private IHapticService _hapticService;

        private RectTransform _containerRect;
        private Camera _targetCamera;
        private SquishyMeshQuality _quality;

        private readonly List<SquishyTouchData> _rawTouches = new List<SquishyTouchData>();
        private readonly List<SquishyTouchData> _localTouches = new List<SquishyTouchData>();

        // Cooldown timer for haptics to prevent execution overload
        private float _hapticCooldownTimer;
        private const float HapticCooldown = 0.15f;

        private Coroutine _transitionCoroutine;
        private SquishyRuntimeParameters _currentParameters;

        public bool IsInitialized => _isInitialized;
        public SquishyRuntimeParameters CurrentParameters => _currentParameters;

        /// <summary>
        /// Gets the active simulation solver.
        /// </summary>
        public SquishySimulation Simulation => _simulation;

        /// <summary>
        /// Gets or sets the haptic service adapter.
        /// </summary>
        public IHapticService HapticService
        {
            get => _hapticService ?? (_hapticService = new NullHapticService());
            set => _hapticService = value;
        }

        private void Awake()
        {
            _meshController = GetComponent<SquishyMeshController>();
            _inputProvider = GetComponent<SquishyInputProvider>();
            _simulation = new SquishySimulation();
            _meshController.LinkSimulation(_simulation);
        }

        private ISquishyAudioService _audioService;
        private IMaterialPresetController _presetController;
        private ISquishySettingsRepository _settingsRepo;
        private IAppModeController _appModeController;

        private void Start()
        {
            var container = FRTESdkManager.Instance.Container;
            if (container != null)
            {
                container.TryResolve<ISquishyAudioService>(out _audioService);
                container.TryResolve<IMaterialPresetController>(out _presetController);
                container.TryResolve<ISquishySettingsRepository>(out _settingsRepo);
                container.TryResolve<IAppModeController>(out _appModeController);
            }
        }

        public void Initialize(SquishySurfaceInput input)
        {
            if (_isInitialized) return;

            _containerRect = input.ContainerRect;
            _targetCamera = input.TargetCamera;
            _quality = input.Quality;

            // 1. Resolve mesh columns/rows divisions based on quality settings
            int columns = 35;
            int rows = 50;
            switch (_quality)
            {
                case SquishyMeshQuality.Low:
                    columns = 20;
                    rows = 30;
                    break;
                case SquishyMeshQuality.Medium:
                    columns = 35;
                    rows = 50;
                    break;
                case SquishyMeshQuality.High:
                    columns = 50;
                    rows = 70;
                    break;
            }

            // Adjust aspect ratio if image details exist
            if (input.SourceTexture != null)
            {
                float aspect = (float)input.SourceTexture.width / input.SourceTexture.height;
                if (aspect > 1f)
                {
                    // Landscape
                    columns = Mathf.RoundToInt(rows * aspect);
                }
                else
                {
                    // Portrait
                    rows = Mathf.RoundToInt(columns / aspect);
                }
            }

            // Ensure division indices are valid bounds
            columns = Mathf.Clamp(columns, 5, 100);
            rows = Mathf.Clamp(rows, 5, 100);

            // 2. Build Simulation Grid
            _simulation.InitializeGrid(columns, rows);

            // 3. Build Mesh
            var meshSettings = new SquishyMeshSettings
            {
                Width = input.Width,
                Height = input.Height,
                Columns = columns,
                Rows = rows,
                Quality = _quality
            };
            _meshController.BuildMesh(meshSettings);

            // Apply texture to MeshRenderer
            var meshRenderer = GetComponent<MeshRenderer>();
            if (meshRenderer != null && input.SourceTexture != null)
            {
                meshRenderer.material.mainTexture = input.SourceTexture;
            }

            UpdateCurrentParameters();
            _isInitialized = true;
        }

        public void ResetSurface()
        {
            if (!_isInitialized) return;

            _simulation.ResetSimulation();
            _meshController.ResetVertices();
            _localTouches.Clear();
            _rawTouches.Clear();
        }

        public void RebuildSurface(SquishySurfaceInput input)
        {
            ResetSurface();
            _isInitialized = false;
            Initialize(input);
        }

        private void Update()
        {
            if (!_isInitialized) return;

            if (_appModeController != null && _appModeController.CurrentMode != SquishyAppMode.SquishyPlay)
            {
                _localTouches.Clear();
                _rawTouches.Clear();
                _simulation.SetTouchInputs(_localTouches);
                _simulation.Step(Time.deltaTime);
                _meshController.ApplyVertexPositions();
                return;
            }

            if (_hapticCooldownTimer > 0f)
            {
                _hapticCooldownTimer -= Time.deltaTime;
            }

            // 1. Gather screen touches
            _inputProvider.GetActiveTouches(_rawTouches);
            _localTouches.Clear();

            int count = _rawTouches.Count;
            for (int i = 0; i < count; i++)
            {
                var touch = _rawTouches[i];

                // 2. Transform screen coordinates to local RectTransform coordinates [-0.5, 0.5]
                if (_containerRect != null)
                {
                    Vector2 localPoint;
                    bool isInsideRect = RectTransformUtility.ScreenPointToLocalPointInRectangle(
                        _containerRect,
                        touch.ScreenPosition,
                        _targetCamera,
                        out localPoint
                    );

                    float rectWidth = _containerRect.rect.width;
                    float rectHeight = _containerRect.rect.height;

                    if (rectWidth > 0.01f && rectHeight > 0.01f)
                    {
                        // Normalize local point from pixel bounds to [-0.5, 0.5] range
                        float localX = localPoint.x / rectWidth;
                        float localY = localPoint.y / rectHeight;

                        // Check if touch coordinates fall within target photo bounds
                        if (localX >= -0.5f && localX <= 0.5f && localY >= -0.5f && localY <= 0.5f)
                        {
                            Vector2 prevLocalPoint;
                            RectTransformUtility.ScreenPointToLocalPointInRectangle(
                                _containerRect,
                                touch.PreviousScreenPosition,
                                _targetCamera,
                                out prevLocalPoint
                            );

                            float prevLocalX = prevLocalPoint.x / rectWidth;
                            float prevLocalY = prevLocalPoint.y / rectHeight;

                            touch.ScreenPosition = new Vector2(localX, localY);
                            touch.PreviousScreenPosition = new Vector2(prevLocalX, prevLocalY);
                            touch.Delta = touch.ScreenPosition - touch.PreviousScreenPosition;

                            _localTouches.Add(touch);

                            // Trigger Haptics & Audio on touch down peak
                            if (touch.Phase == SquishyTouchPhase.Began)
                            {
                                float hapticIntensity = 0.3f;
                                if (_presetController != null && _presetController.CurrentPreset != null)
                                {
                                    hapticIntensity = _presetController.CurrentPreset.Haptic.TouchIntensity;
                                }
                                TriggerHapticFeedback(hapticIntensity);

                                if (_audioService != null)
                                {
                                    _audioService.PlayTouch(new SquishyInteractionContext
                                    {
                                        Speed = touch.Speed,
                                        Duration = touch.Duration,
                                        Intensity = 0.5f,
                                        UV = touch.ScreenPosition
                                    });
                                }

                                FRTESdkManager.Instance.EventBus?.Publish(new SquishyTouchStartedEvent
                                {
                                    TouchId = touch.TouchId,
                                    UV = touch.ScreenPosition,
                                    TimeStamp = Time.time
                                });
                            }
                            else if (touch.Phase == SquishyTouchPhase.Moved && touch.Speed > 2f)
                            {
                                float hapticIntensity = 0.2f;
                                if (_presetController != null && _presetController.CurrentPreset != null)
                                {
                                    hapticIntensity = _presetController.CurrentPreset.Haptic.DragIntensity;
                                }
                                TriggerHapticFeedback(hapticIntensity);

                                if (_audioService != null)
                                {
                                    _audioService.PlayDrag(new SquishyInteractionContext
                                    {
                                        Speed = touch.Speed,
                                        Duration = touch.Duration,
                                        Intensity = 0.3f,
                                        UV = touch.ScreenPosition
                                    });
                                }
                            }
                            else if (touch.Phase == SquishyTouchPhase.Ended)
                            {
                                float hapticIntensity = 0.25f;
                                if (_presetController != null && _presetController.CurrentPreset != null)
                                {
                                    hapticIntensity = _presetController.CurrentPreset.Haptic.ReleaseIntensity;
                                }
                                TriggerHapticFeedback(hapticIntensity);

                                if (_audioService != null)
                                {
                                    _audioService.PlayRelease(new SquishyInteractionContext
                                    {
                                        Speed = touch.Speed,
                                        Duration = touch.Duration,
                                        Intensity = 0.5f,
                                        UV = touch.ScreenPosition
                                    });
                                }

                                FRTESdkManager.Instance.EventBus?.Publish(new SquishyTouchReleasedEvent
                                {
                                    TouchId = touch.TouchId,
                                    UV = touch.ScreenPosition,
                                    Duration = touch.Duration
                                });
                            }
                        }
                    }
                }
            }

            // 3. Feed local touch inputs and execute simulation step
            _simulation.SetTouchInputs(_localTouches);
            _simulation.Step(Time.deltaTime);

            // 4. Update rendering mesh vertices
            _meshController.ApplyVertexPositions();

            // Detect high velocity rebound wobble to fire strong bounce haptic
            DetectBounceHaptic();
        }

        private void TriggerHapticFeedback(float intensity)
        {
            if (_hapticCooldownTimer > 0f) return;

            // Load user setting check
            bool hapticEnabled = true;
            if (_settingsRepo != null)
            {
                var settings = _settingsRepo.Load();
                hapticEnabled = settings.HapticEnabled;
            }

            if (!hapticEnabled) return;

            // Query preset haptic override if exists
            float cooldown = HapticCooldown;
            if (_presetController != null && _presetController.CurrentPreset != null)
            {
                var h = _presetController.CurrentPreset.Haptic;
                if (!h.Enabled) return;
                cooldown = h.MinInterval;
            }

            var haptic = HapticService;
            if (intensity <= 0.33f)
            {
                haptic.PlayLight();
            }
            else if (intensity <= 0.66f)
            {
                haptic.PlayMedium();
            }
            else
            {
                haptic.PlayStrong();
            }

            // Notify Event Bus for testing/diagnostics
            var eventBus = FRTESdkManager.Instance.EventBus;
            if (eventBus != null)
            {
                eventBus.Publish(new SquishyHapticTriggeredEvent { Level = intensity <= 0.33f ? 1 : (intensity <= 0.66f ? 2 : 3) });
            }

            _hapticCooldownTimer = cooldown;
        }

        private void DetectBounceHaptic()
        {
            if (_rawTouches.Count > 0 || _simulation.Vertices == null) return;

            // If no active touch exists, verify node acceleration shifts to trigger bounce click
            float maxVelocityMagnitude = 0f;
            int count = _simulation.Vertices.Length;
            for (int i = 0; i < count; i++)
            {
                float vMag = _simulation.Vertices[i].Velocity.sqrMagnitude;
                if (vMag > maxVelocityMagnitude)
                {
                    maxVelocityMagnitude = vMag;
                }
            }

            // A high velocity bounce transition (e.g. spring overshoot snapping)
            if (maxVelocityMagnitude > 180f)
            {
                float hapticIntensity = 0.5f;
                if (_presetController != null && _presetController.CurrentPreset != null)
                {
                    hapticIntensity = _presetController.CurrentPreset.Haptic.BounceIntensity;
                }
                TriggerHapticFeedback(hapticIntensity);

                if (_audioService != null)
                {
                    _audioService.PlayBounce(new SquishyInteractionContext
                    {
                        Speed = Mathf.Sqrt(maxVelocityMagnitude),
                        Duration = 0f,
                        Intensity = hapticIntensity,
                        UV = Vector2.zero
                    });
                }
            }
        }

        private void OnDisable()
        {
            if (_transitionCoroutine != null)
            {
                StopCoroutine(_transitionCoroutine);
                _transitionCoroutine = null;
            }
            ResetSurface();
        }

        public void ApplyParameters(SquishyRuntimeParameters parameters, MaterialTransitionOptions transitionOptions)
        {
            if (_transitionCoroutine != null)
            {
                StopCoroutine(_transitionCoroutine);
                _transitionCoroutine = null;
            }

            if (transitionOptions.Animate && transitionOptions.Duration > 0.001f)
            {
                _transitionCoroutine = StartCoroutine(TransitionCoroutine(parameters, transitionOptions));
            }
            else
            {
                ApplyParametersDirectly(parameters);
                if (!transitionOptions.PreserveCurrentDeformation)
                {
                    ResetSurface();
                }
            }
        }

        private void ApplyParametersDirectly(SquishyRuntimeParameters targetParams)
        {
            var settings = _simulation.Settings;
            settings.TouchRadius = targetParams.TouchRadius;
            settings.TouchStrength = targetParams.TouchStrength;
            settings.DragStrength = targetParams.DragStrength;
            settings.SpringStrength = targetParams.SpringStrength;
            settings.NeighborSpringStrength = targetParams.NeighborSpringStrength;
            settings.Damping = targetParams.Damping;
            settings.Mass = targetParams.Mass;
            settings.MaxDisplacement = targetParams.MaxDisplacement;
            settings.EdgeResistance = targetParams.EdgeResistance;
            settings.MultiTouchForceLimit = targetParams.MultiTouchForceLimit;
            settings.WobbleAmount = targetParams.WobbleAmount;
            settings.WobbleFrequency = targetParams.WobbleFrequency;
            settings.RecoveryMultiplier = targetParams.RecoverySpeed;
            settings.CreepRate = targetParams.CreepRate;
            settings.CreepRecoveryRate = targetParams.CreepRecoveryRate;

            _currentParameters = targetParams;
        }

        private void UpdateCurrentParameters()
        {
            var settings = _simulation.Settings;
            _currentParameters = new SquishyRuntimeParameters
            {
                TouchRadius = settings.TouchRadius,
                TouchStrength = settings.TouchStrength,
                DragStrength = settings.DragStrength,
                SpringStrength = settings.SpringStrength,
                NeighborSpringStrength = settings.NeighborSpringStrength,
                Damping = settings.Damping,
                Mass = settings.Mass,
                MaxDisplacement = settings.MaxDisplacement,
                EdgeResistance = settings.EdgeResistance,
                MultiTouchForceLimit = settings.MultiTouchForceLimit,
                WobbleAmount = settings.WobbleAmount,
                WobbleFrequency = settings.WobbleFrequency,
                RecoverySpeed = settings.RecoveryMultiplier,
                CreepRate = settings.CreepRate,
                CreepRecoveryRate = settings.CreepRecoveryRate
            };
        }

        private System.Collections.IEnumerator TransitionCoroutine(SquishyRuntimeParameters targetParams, MaterialTransitionOptions options)
        {
            float elapsed = 0f;
            var startParams = _currentParameters;

            while (elapsed < options.Duration)
            {
                elapsed += Time.deltaTime;
                float t = Mathf.Clamp01(elapsed / options.Duration);
                if (options.Curve != null)
                {
                    t = options.Curve.Evaluate(t);
                }

                var stepParams = new SquishyRuntimeParameters
                {
                    TouchRadius = Mathf.Lerp(startParams.TouchRadius, targetParams.TouchRadius, t),
                    TouchStrength = Mathf.Lerp(startParams.TouchStrength, targetParams.TouchStrength, t),
                    DragStrength = Mathf.Lerp(startParams.DragStrength, targetParams.DragStrength, t),
                    SpringStrength = Mathf.Lerp(startParams.SpringStrength, targetParams.SpringStrength, t),
                    NeighborSpringStrength = Mathf.Lerp(startParams.NeighborSpringStrength, targetParams.NeighborSpringStrength, t),
                    Damping = Mathf.Lerp(startParams.Damping, targetParams.Damping, t),
                    Mass = Mathf.Lerp(startParams.Mass, targetParams.Mass, t),
                    MaxDisplacement = Mathf.Lerp(startParams.MaxDisplacement, targetParams.MaxDisplacement, t),
                    EdgeResistance = Mathf.Lerp(startParams.EdgeResistance, targetParams.EdgeResistance, t),
                    MultiTouchForceLimit = Mathf.Lerp(startParams.MultiTouchForceLimit, targetParams.MultiTouchForceLimit, t),
                    WobbleAmount = Mathf.Lerp(startParams.WobbleAmount, targetParams.WobbleAmount, t),
                    WobbleFrequency = Mathf.Lerp(startParams.WobbleFrequency, targetParams.WobbleFrequency, t),
                    RecoverySpeed = Mathf.Lerp(startParams.RecoverySpeed, targetParams.RecoverySpeed, t),
                    CreepRate = Mathf.Lerp(startParams.CreepRate, targetParams.CreepRate, t),
                    CreepRecoveryRate = Mathf.Lerp(startParams.CreepRecoveryRate, targetParams.CreepRecoveryRate, t)
                };

                ApplyParametersDirectly(stepParams);
                yield return null;
            }

            ApplyParametersDirectly(targetParams);
            _transitionCoroutine = null;
        }
    }
}
