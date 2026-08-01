using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using FRTE.Core;

namespace FRTE.PhotoZone.Tests
{
    [TestFixture]
    public sealed class PhotoZonePlayModeTests
    {
        private PhotoZoneLibrary _library;
        private PhotoZoneController _controller;

        [SetUp]
        public void SetUp()
        {
            _library = ScriptableObject.CreateInstance<PhotoZoneLibrary>();
            _library.InitializeLibrary();

            _controller = new PhotoZoneController(_library);
        }

        [TearDown]
        public void TearDown()
        {
            if (_library != null) Object.DestroyImmediate(_library);
        }

        [UnityTest]
        public IEnumerator PhotoZoneController_ApplyAndClear_WorksCorrectly()
        {
            Assert.IsNull(_controller.CurrentPreset);

            // Apply Strawberry Farm
            bool ok = _controller.ApplyPhotoZone("photozone.strawberry_farm");
            Assert.IsTrue(ok);
            Assert.IsNotNull(_controller.CurrentPreset);
            Assert.AreEqual("photozone.strawberry_farm", _controller.CurrentPreset.Id);

            // Toggle Layer
            Assert.IsTrue(_controller.IsLayerVisible(PhotoZoneLayer.Background));
            _controller.SetLayerVisibility(PhotoZoneLayer.Background, false);
            Assert.IsFalse(_controller.IsLayerVisible(PhotoZoneLayer.Background));

            // Clear
            _controller.ClearPhotoZone();
            Assert.IsNull(_controller.CurrentPreset);

            yield return null;
        }
    }
}
