using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Surprise.Tests
{
    [TestFixture]
    public sealed class SurpriseEditModeTests
    {
        [Test]
        public void Preset_InitializesWithValidValues()
        {
            var triggers = new[] { new SurpriseTriggerDefinition { TriggerType = SurpriseTriggerType.TapCount, FloatValue = 10f } };
            var effects = new[] { new SurpriseEffectDefinition { EffectId = "effect.fruit_pop", Duration = 1f } };

            var preset = ScriptableObject.CreateInstance<SurpriseEventPreset>();
            preset.SetTestValues("test.event", "Fruit Pop Test", triggers, effects, 5f, "strawberry");

            Assert.AreEqual("test.event", preset.Id);
            Assert.AreEqual(1, preset.Triggers.Length);
            Assert.AreEqual(SurpriseTriggerType.TapCount, preset.Triggers[0].TriggerType);
            Assert.AreEqual(10f, preset.Triggers[0].FloatValue);
            Assert.AreEqual("effect.fruit_pop", preset.Effects[0].EffectId);
        }
    }
}
