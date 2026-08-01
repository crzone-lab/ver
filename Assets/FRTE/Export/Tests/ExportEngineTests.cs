using System.IO;
using System.Threading.Tasks;
using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Export.Tests
{
    [TestFixture]
    public class ExportEngineTests
    {
        private FRTEContainer _container;
        private AsyncExporter _exporter;
        private RenderTexture _dummyRT;
        private string _tempFilePath;

        [SetUp]
        public void SetUp()
        {
            _container = new FRTEContainer();
            _exporter = new AsyncExporter();
            _exporter.Initialize(_container);
            _exporter.Enable();

            _dummyRT = new RenderTexture(16, 16, 0, RenderTextureFormat.ARGB32);
            _dummyRT.Create();

            _tempFilePath = Path.Combine(Application.temporaryCachePath, "frte_test_export.png");
            if (File.Exists(_tempFilePath))
            {
                File.Delete(_tempFilePath);
            }
        }

        [TearDown]
        public void TearDown()
        {
            _exporter.Disable();
            if (_dummyRT != null)
            {
                _dummyRT.Release();
                Object.DestroyImmediate(_dummyRT);
            }
            if (File.Exists(_tempFilePath))
            {
                File.Delete(_tempFilePath);
            }
            _container.Clear();
        }

        [Test]
        public async Task ExportPNG_SavesFileToDiskCorrectly()
        {
            Assert.IsFalse(File.Exists(_tempFilePath));

            // Execute export
            await _exporter.ExportPNGAsync(_dummyRT, _tempFilePath);

            // Verify file exists
            Assert.IsTrue(File.Exists(_tempFilePath));
            Assert.Greater(new FileInfo(_tempFilePath).Length, 0);
        }
    }
}
