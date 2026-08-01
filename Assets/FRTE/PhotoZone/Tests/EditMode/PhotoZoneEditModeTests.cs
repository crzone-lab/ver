using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.PhotoZone.Tests
{
    [TestFixture]
    public sealed class PhotoZoneEditModeTests
    {
        private PhotoZoneLibrary _library;

        [SetUp]
        public void SetUp()
        {
            _library = ScriptableObject.CreateInstance<PhotoZoneLibrary>();
        }

        [TearDown]
        public void TearDown()
        {
            if (_library != null) Object.DestroyImmediate(_library);
        }

        [Test]
        public void Provider_ReturnsFivePresetsSorted()
        {
            var presets = _library.GetAll();
            Assert.AreEqual(5, presets.Count);

            // Verify order matches
            Assert.AreEqual("photozone.strawberry_farm", presets[0].Id);
            Assert.AreEqual("photozone.grape_tunnel", presets[4].Id);
        }

        [Test]
        public void Provider_GetDefault_ReturnsStrawberryFarm()
        {
            var def = _library.GetDefault();
            Assert.IsNotNull(def);
            Assert.AreEqual("photozone.strawberry_farm", def.Id);
        }
    }
}
