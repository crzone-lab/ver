using System.Collections;
using System.IO;
using System.Threading;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using FRTE.Core;

namespace FRTE.Export.Tests
{
    [TestFixture]
    public sealed class ExportPlayModeTests
    {
        private ExportStorageService _storage;
        private ImageExporter _imageExporter;
        private VideoExporter _videoExporter;
        private SquishyProjectRepository _sessionRepo;

        [SetUp]
        public void SetUp()
        {
            _storage = new ExportStorageService();
            _imageExporter = new ImageExporter(_storage);
            _videoExporter = new VideoExporter(_storage);
            _sessionRepo = new SquishyProjectRepository();

            var container = FRTESdkManager.Instance.Container;
            if (!container.TryResolve<ICaptureSource>(out _))
            {
                container.Register<ICaptureSource>(new DefaultCaptureSource());
            }
        }

        [TearDown]
        public void TearDown()
        {
            _storage.CleanTemporaryFiles();
            var task = _sessionRepo.DeleteAsync(CancellationToken.None);
            while (!task.IsCompleted) { }
        }

        [UnityTest]
        public IEnumerator ImageExporter_CapturePng_SavesFileToDisk()
        {
            var options = new ImageExportOptions
            {
                AspectRatio = ImageAspectRatio.Ratio1_1,
                Quality = ImageResolutionQuality.Standard,
                TransparentBackground = false
            };

            var task = _imageExporter.ExportPngAsync(options, CancellationToken.None);
            yield return new WaitUntil(() => task.IsCompleted);

            var result = task.Result;
            Assert.AreEqual(ExportStatus.Success, result.Status);
            Assert.IsNotEmpty(result.FilePath);
            Assert.IsTrue(File.Exists(result.FilePath));
        }

        [UnityTest]
        public IEnumerator VideoExporter_RecordingSequence_TransitionsCorrectly()
        {
            Assert.AreEqual(RecordingState.Idle, _videoExporter.CurrentState);

            var options = new VideoExportOptions
            {
                Width = 720,
                Height = 1280,
                FrameRate = 30,
                MaxDurationSeconds = 1f,
                IncludeAudio = false
            };

            // Start recording
            var startTask = _videoExporter.StartRecordingAsync(options, CancellationToken.None);
            yield return new WaitUntil(() => startTask.IsCompleted);
            Assert.AreEqual(RecordingState.Recording, _videoExporter.CurrentState);

            // Wait 1.1s to allow auto-stop
            yield return new WaitForSeconds(1.2f);
            Assert.AreEqual(RecordingState.Completed, _videoExporter.CurrentState);
        }

        [UnityTest]
        public IEnumerator SessionRepository_SaveAndRestore_MaintainsData()
        {
            var session = new SquishyProjectSessionData
            {
                CurrentMaterialId = "fruit.watermelon",
                CurrentPhotoZoneId = "photozone.watermelon_beach",
                LastMode = SquishyAppMode.SquishyPlay
            };

            var saveTask = _sessionRepo.SaveAsync(session, CancellationToken.None);
            yield return new WaitUntil(() => saveTask.IsCompleted);
            Assert.IsTrue(_sessionRepo.HasRecoverableProject);

            var loadTask = _sessionRepo.LoadAsync(CancellationToken.None);
            yield return new WaitUntil(() => loadTask.IsCompleted);

            var restored = loadTask.Result;
            Assert.IsNotNull(restored);
            Assert.AreEqual("fruit.watermelon", restored.CurrentMaterialId);
            Assert.AreEqual(SquishyAppMode.SquishyPlay, restored.LastMode);
        }
    }
}
