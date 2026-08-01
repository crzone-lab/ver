using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Photo.Tests
{
    [TestFixture]
    public class PhotoEngineTests
    {
        private FRTEContainer _container;
        private GPUPhotoManager _photoManager;
        private Texture2D _dummyTexture;

        [SetUp]
        public void SetUp()
        {
            _container = new FRTEContainer();
            _photoManager = new GPUPhotoManager();
            _photoManager.Initialize(_container);
            _photoManager.Enable();

            // Create a small 64x64 texture for testing
            _dummyTexture = new Texture2D(64, 64, TextureFormat.RGBA32, false);
            for (int y = 0; y < 64; y++)
            {
                for (int x = 0; x < 64; x++)
                {
                    _dummyTexture.SetPixel(x, y, Color.red);
                }
            }
            _dummyTexture.Apply();
        }

        [TearDown]
        public void TearDown()
        {
            _photoManager.Disable();
            if (_dummyTexture != null)
            {
                Object.DestroyImmediate(_dummyTexture);
            }
            _container.Clear();
        }

        [Test]
        public void LoadPhoto_AllocatesWorkingTextureWithCorrectDimensions()
        {
            _photoManager.LoadPhoto(_dummyTexture);

            Assert.IsNotNull(_photoManager.WorkingTexture);
            Assert.AreEqual(64, _photoManager.WorkingTexture.width);
            Assert.AreEqual(64, _photoManager.WorkingTexture.height);
            Assert.AreEqual(64, _photoManager.OriginalWidth);
            Assert.AreEqual(64, _photoManager.OriginalHeight);
        }

        [Test]
        public void RotateAndScale_DoesNotThrowExceptions()
        {
            _photoManager.LoadPhoto(_dummyTexture);

            Assert.DoesNotThrow(() => _photoManager.Rotate(90f));
            Assert.DoesNotThrow(() => _photoManager.Scale(new Vector2(2f, 0.5f)));
            Assert.DoesNotThrow(() => _photoManager.Crop(new Rect(0.25f, 0.25f, 0.5f, 0.5f)));

            Assert.IsNotNull(_photoManager.WorkingTexture);
        }
    }
}
