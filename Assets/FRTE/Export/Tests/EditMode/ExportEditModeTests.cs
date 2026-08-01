using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Export.Tests
{
    [TestFixture]
    public sealed class ExportEditModeTests
    {
        [Test]
        public void ImageExportOptions_VerifyResolutionSettings()
        {
            var options = new ImageExportOptions
            {
                Quality = ImageResolutionQuality.High,
                AspectRatio = ImageAspectRatio.Ratio9_16,
                TransparentBackground = true
            };

            Assert.AreEqual(ImageResolutionQuality.High, options.Quality);
            Assert.AreEqual(ImageAspectRatio.Ratio9_16, options.AspectRatio);
            Assert.IsTrue(options.TransparentBackground);
        }

        [Test]
        public void VideoExportOptions_VerifyDurationSettings()
        {
            var options = new VideoExportOptions
            {
                Width = 1080,
                Height = 1920,
                FrameRate = 30,
                MaxDurationSeconds = 15f,
                IncludeAudio = true
            };

            Assert.AreEqual(15f, options.MaxDurationSeconds);
            Assert.AreEqual(30, options.FrameRate);
            Assert.IsTrue(options.IncludeAudio);
        }

        [Test]
        public void ProjectSession_Serialization_RoundtripsSuccessfully()
        {
            var original = new SquishyProjectSessionData
            {
                CurrentMaterialId = "fruit.lemon",
                CurrentPhotoZoneId = "photozone.lemon_garden",
                LastMode = SquishyAppMode.Decoration
            };

            string json = JsonUtility.ToJson(original);
            Assert.IsNotEmpty(json);

            var restored = JsonUtility.FromJson<SquishyProjectSessionData>(json);
            Assert.IsNotNull(restored);
            Assert.AreEqual(original.CurrentMaterialId, restored.CurrentMaterialId);
            Assert.AreEqual(original.CurrentPhotoZoneId, restored.CurrentPhotoZoneId);
            Assert.AreEqual(original.LastMode, restored.LastMode);
        }
    }
}
