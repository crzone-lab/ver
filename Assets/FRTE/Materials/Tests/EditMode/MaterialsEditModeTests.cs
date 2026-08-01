using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Materials.Tests
{
    [TestFixture]
    public sealed class MaterialsEditModeTests
    {
        private SquishyMaterialLibrary _library;

        [SetUp]
        public void SetUp()
        {
            _library = ScriptableObject.CreateInstance<SquishyMaterialLibrary>();
        }

        [TearDown]
        public void TearDown()
        {
            if (_library != null)
            {
                Object.DestroyImmediate(_library);
            }
        }

        [Test]
        public void Library_EmptySlot_GracefullyBypasses()
        {
            var presets = new List<SquishyMaterialPreset> { null };
            _library.SetTestPresets(presets);

            Assert.AreEqual(0, _library.GetAll().Count);
        }

        [Test]
        public void Library_DuplicateId_FiltersOutDuplicate()
        {
            var p1 = ScriptableObject.CreateInstance<SquishyMaterialPreset>();
            p1.SetTestValues("dup.id", "Mochi", MaterialCategory.Basic, default, default, default, default);

            var p2 = ScriptableObject.CreateInstance<SquishyMaterialPreset>();
            p2.SetTestValues("dup.id", "Slime", MaterialCategory.Basic, default, default, default, default);

            var presets = new List<SquishyMaterialPreset> { p1, p2 };
            _library.SetTestPresets(presets);

            // Filters duplicate ID
            Assert.AreEqual(1, _library.GetAll().Count);
        }

        [Test]
        public void Library_GetDefault_ReturnsJellyPreset()
        {
            _library.InitializeLibrary(); // Triggers standard 12 loading
            var def = _library.GetDefault();

            Assert.IsNotNull(def);
            Assert.AreEqual("basic.jelly", def.Id);
        }

        [Test]
        public void SettingsRepository_CorruptedJson_RestoresDefaults()
        {
            var repo = new SquishySettingsRepository();
            repo.Reset(); // Clear old prefs

            // Save corrupted JSON string
            PlayerPrefs.SetString("FRTE_SquishyUserSettings", "{corrupted_json:[[");
            PlayerPrefs.Save();

            var settings = repo.Load();
            Assert.IsNotNull(settings);
            Assert.AreEqual("basic.jelly", settings.SelectedPresetId);
            Assert.AreEqual(1f, settings.AudioVolume);
        }

        [Test]
        public void PhysicsParameters_LimitsSafetyRanges()
        {
            // Verify factory presets have valid bounds
            var presets = SquishyMaterialPresetsFactory.CreateAllPresets();
            Assert.AreEqual(12, presets.Count);

            for (int i = 0; i < presets.Count; i++)
            {
                var p = presets[i].Physics;
                Assert.GreaterOrEqual(p.TouchRadiusMultiplier, 0.05f);
                Assert.GreaterOrEqual(p.SpringStrength, 1f);
                Assert.GreaterOrEqual(p.Damping, 0.1f);
                Assert.GreaterOrEqual(p.Mass, 0.05f);
            }
        }
    }
}
