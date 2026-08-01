using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration.Tests
{
    [TestFixture]
    public sealed class DecorationEditModeTests
    {
        private DecorationLibrary _library;

        [SetUp]
        public void SetUp()
        {
            _library = ScriptableObject.CreateInstance<DecorationLibrary>();
        }

        [TearDown]
        public void TearDown()
        {
            if (_library != null) Object.DestroyImmediate(_library);
        }

        [Test]
        public void Library_DuplicateId_FiltersOut()
        {
            var p1 = ScriptableObject.CreateInstance<DecorationPreset>();
            p1.SetTestValues("dup", "Ears A", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop);
            var p2 = ScriptableObject.CreateInstance<DecorationPreset>();
            p2.SetTestValues("dup", "Ears B", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop);

            _library.SetTestPresets(new List<DecorationPreset> { p1, p2 });

            Assert.AreEqual(1, _library.GetAll().Count);
        }

        [Test]
        public void Preset_LimitsScaleClamps()
        {
            var controller = new DecorationController(_library);
            _library.InitializeLibrary();

            string instId = controller.AddDecoration("ear.strawberry");
            Assert.IsNotEmpty(instId);

            // Scale down excessively
            controller.ScaleDecoration(instId, new Vector2(-2f, -2f));
            var inst = controller.CurrentDecorations[0];
            Assert.GreaterOrEqual(inst.Scale.x, 0.1f);
        }
    }
}
