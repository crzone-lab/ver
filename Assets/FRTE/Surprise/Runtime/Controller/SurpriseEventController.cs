using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;
using FRTE.Physics;
using FRTE.Materials;

namespace FRTE.Surprise
{
    /// <summary>
    /// Implements ISurpriseEventController.
    /// Tracks tap counts, hold durations, and triggers corresponding surprise effect presets.
    /// </summary>
    public sealed class SurpriseEventController : ISurpriseEventController
    {
        private bool _isEnabled = true;
        private readonly List<SurpriseEventPreset> _presets = new List<SurpriseEventPreset>();
        private readonly Dictionary<string, float> _cooldowns = new Dictionary<string, float>();
        private readonly Dictionary<int, float> _touchStartTimes = new Dictionary<int, float>();

        // Session counters
        private int _totalTaps;
        private int _consecutiveTaps;
        private float _lastTapTime;
        private float _globalCooldownTimer;

        private const float GlobalCooldown = 5.0f;
        private const int MaxActiveEffects = 2;
        private readonly List<ISurpriseEffect> _activeEffects = new List<ISurpriseEffect>();

        public bool IsEnabled
        {
            get => _isEnabled;
            set => _isEnabled = value;
        }

        public SurpriseEventController()
        {
            // Initialize event list
            _presets = CreateFallbackEvents();

            // Listen to Events
            var bus = FRTESdkManager.Instance.EventBus;
            if (bus != null)
            {
                bus.Subscribe<SquishyTouchStartedEvent>(OnTouchStarted);
                bus.Subscribe<SquishyTouchReleasedEvent>(OnTouchReleased);
            }
        }

        public void RegisterInteraction(SquishyInteractionContext context)
        {
            // Manual trigger check if needed
        }

        public bool TryTriggerEvent()
        {
            return false;
        }

        public void CancelActiveEvents()
        {
            var pool = FRTESdkManager.Instance.Container.Resolve<ISurpriseEffectPool>();
            for (int i = 0; i < _activeEffects.Count; i++)
            {
                if (pool != null) pool.Return(_activeEffects[i]);
            }
            _activeEffects.Clear();
        }

        public void ResetSessionProgress()
        {
            _totalTaps = 0;
            _consecutiveTaps = 0;
            _cooldowns.Clear();
            _touchStartTimes.Clear();
            CancelActiveEvents();
        }

        private void OnTouchStarted(SquishyTouchStartedEvent evt)
        {
            if (!_isEnabled) return;

            // Track tap count
            _totalTaps++;
            _touchStartTimes[evt.TouchId] = evt.TimeStamp;

            // Track consecutive taps (within 0.4 seconds)
            if (Time.time - _lastTapTime < 0.4f)
            {
                _consecutiveTaps++;
            }
            else
            {
                _consecutiveTaps = 1;
            }
            _lastTapTime = Time.time;

            // Evaluate triggers
            EvaluateTriggers(evt.UV, SurpriseTriggerType.TapCount, _totalTaps);
            EvaluateTriggers(evt.UV, SurpriseTriggerType.ConsecutiveTap, _consecutiveTaps);
        }

        private void OnTouchReleased(SquishyTouchReleasedEvent evt)
        {
            if (!_isEnabled) return;

            if (_touchStartTimes.TryGetValue(evt.TouchId, out float start))
            {
                float hold = Time.time - start;
                _touchStartTimes.Remove(evt.TouchId);

                if (hold >= 1.5f)
                {
                    EvaluateTriggers(evt.UV, SurpriseTriggerType.LongPress, hold);
                }
            }
        }

        private void EvaluateTriggers(Vector2 uv, SurpriseTriggerType type, float currentProgress)
        {
            if (Time.time < _globalCooldownTimer) return;
            if (_activeEffects.Count >= MaxActiveEffects) return;

            // Check settings check (if UI mode prevents surprises)
            var modeController = FRTESdkManager.Instance.Container.Resolve<IAppModeController>();
            if (modeController != null && modeController.CurrentMode != SquishyAppMode.SquishyPlay)
            {
                return; // Suppress during Decoration/PhotoZone/Collection edit
            }

            for (int i = 0; i < _presets.Count; i++)
            {
                var preset = _presets[i];
                if (IsOnCooldown(preset.Id)) continue;

                bool conditionMet = false;
                for (int j = 0; j < preset.Triggers.Length; j++)
                {
                    var trigger = preset.Triggers[j];
                    if (trigger.TriggerType == type)
                    {
                        if (currentProgress >= trigger.FloatValue)
                        {
                            conditionMet = true;
                            break;
                        }
                    }

                    // Material Specific Trigger check
                    if (trigger.TriggerType == SurpriseTriggerType.MaterialSpecific)
                    {
                        var matCtrl = FRTESdkManager.Instance.Container.Resolve<IMaterialPresetController>();
                        if (matCtrl != null && matCtrl.CurrentPreset != null && matCtrl.CurrentPreset.Id == trigger.TargetId)
                        {
                            conditionMet = true;
                            break;
                        }
                    }

                    // PhotoZone Specific Trigger check
                    if (trigger.TriggerType == SurpriseTriggerType.PhotoZoneSpecific)
                    {
                        var zoneCtrl = FRTESdkManager.Instance.Container.Resolve<IPhotoZoneController>();
                        if (zoneCtrl != null && zoneCtrl.CurrentPreset != null && zoneCtrl.CurrentPreset.Id == trigger.TargetId)
                        {
                            conditionMet = true;
                            break;
                        }
                    }
                }

                if (conditionMet)
                {
                    TriggerEvent(preset, uv);
                    break; // Trigger only one event per frame evaluation
                }
            }
        }

        private void TriggerEvent(SurpriseEventPreset preset, Vector2 uv)
        {
            var pool = FRTESdkManager.Instance.Container.Resolve<ISurpriseEffectPool>();
            if (pool == null) return;

            // Play effects
            for (int i = 0; i < preset.Effects.Length; i++)
            {
                var effectDef = preset.Effects[i];
                var eff = pool.Rent(effectDef.EffectId);
                if (eff != null)
                {
                    eff.Play(uv, effectDef.Duration);
                    _activeEffects.Add(eff);
                    
                    // Prune expired active effects
                    var captureEff = eff;
                    FRTESdkManager.Instance.StartCoroutine(ReturnEffectDelayed(pool, captureEff, effectDef.Duration));
                }
            }

            // Set cooldowns
            _cooldowns[preset.Id] = Time.time + preset.CooldownSeconds;
            _globalCooldownTimer = Time.time + GlobalCooldown;

            // Broadcast trigger & discovered events
            FRTESdkManager.Instance.EventBus?.Publish(new SurpriseEventTriggeredEvent { EventId = preset.Id });
            FRTESdkManager.Instance.EventBus?.Publish(new SurpriseEventDiscoveredEvent { EventId = preset.Id, RelatedFruitId = preset.RelatedFruitId });
        }

        private System.Collections.IEnumerator ReturnEffectDelayed(ISurpriseEffectPool pool, ISurpriseEffect effect, float delay)
        {
            yield return new WaitForSeconds(delay);
            pool.Return(effect);
            _activeEffects.Remove(effect);
            FRTESdkManager.Instance.EventBus?.Publish(new SurpriseEventCompletedEvent { EventId = effect.EffectId });
        }

        private bool IsOnCooldown(string eventId)
        {
            if (_cooldowns.TryGetValue(eventId, out float releaseTime))
            {
                return Time.time < releaseTime;
            }
            return false;
        }

        private List<SurpriseEventPreset> CreateFallbackEvents()
        {
            var list = new List<SurpriseEventPreset>();

            // 1. Fruit Pop (Tap count > 10)
            list.Add(CreatePreset("event.fruit_pop", "Fruit Pop", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.TapCount, FloatValue = 10 } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.fruit_pop", Duration = 1.5f } }, 6f));

            // 2. Heart Burst (Consecutive taps > 5)
            list.Add(CreatePreset("event.heart_burst", "Heart Burst", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.ConsecutiveTap, FloatValue = 5 } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.heart_burst", Duration = 1.2f } }, 8f));

            // 3. Star Spin (Long press > 1.5s)
            list.Add(CreatePreset("event.star_spin", "Star Spin", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.LongPress, FloatValue = 1.5f } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.star_spin", Duration = 2.0f } }, 10f));

            // 4. Character Peek (Tap count > 30)
            list.Add(CreatePreset("event.peek", "FruitRabbit Peek", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.TapCount, FloatValue = 30 } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.peek", Duration = 2.5f } }, 15f));

            // 5. Juice Ripple (Any tap with specific chance)
            list.Add(CreatePreset("event.juice_ripple", "Juice Ripple", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.TapCount, FloatValue = 5 } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.juice_ripple", Duration = 1.5f } }, 5f));

            // 6. Speech Bubble (Consecutive tap > 8)
            list.Add(CreatePreset("event.speech_bubble", "Surprise Speech Bubble", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.ConsecutiveTap, FloatValue = 8 } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.speech_bubble", Duration = 1.8f } }, 10f));

            // 7. Strawberry Discovery (On Strawberry material)
            list.Add(CreatePreset("event.strawberry_discovery", "Strawberry Discovery", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.MaterialSpecific, TargetId = "fruit.strawberry" } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.strawberry_discovery", Duration = 1.5f } }, 10f, "strawberry"));

            // 8. Watermelon Wave (On Watermelon material)
            list.Add(CreatePreset("event.watermelon_wave", "Watermelon Wave", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.MaterialSpecific, TargetId = "fruit.watermelon" } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.watermelon_wave", Duration = 2.5f } }, 12f, "watermelon"));

            // 9. Grape Bounce (On Grape material)
            list.Add(CreatePreset("event.grape_bounce", "Grape Bounce", 
                new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.MaterialSpecific, TargetId = "fruit.grape" } },
                new[] { new SurpriseEffectDefinition { EffectId = "effect.grape_bounce", Duration = 1.5f } }, 8f, "grape"));

            return list;
        }

        private SurpriseEventPreset CreatePreset(
            string id, 
            string name, 
            SurpriseTriggerDefinition[] triggers, 
            SurpriseEffectDefinition[] effects, 
            float cooldown, 
            string fruitId = "")
        {
            var p = ScriptableObject.CreateInstance<SurpriseEventPreset>();
            p.SetTestValues(id, name, triggers, effects, cooldown, fruitId);
            return p;
        }
    }

    // --- SURPRISE EVENTS ---
    public struct SurpriseEventTriggeredEvent { public string EventId; }
    public struct SurpriseEventCompletedEvent { public string EventId; }
    public struct SurpriseEventDiscoveredEvent { public string EventId; public string RelatedFruitId; }
}
