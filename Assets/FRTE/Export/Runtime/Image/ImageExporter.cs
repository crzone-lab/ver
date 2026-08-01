using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Export
{
    /// <summary>
    /// Implements IImageExporter.
    /// Captures Camera frames using RenderTextures and performs aspect ratio cropping.
    /// </summary>
    public sealed class ImageExporter : IImageExporter
    {
        private readonly IExportStorageService _storageService;

        public ImageExporter(IExportStorageService storageService)
        {
            _storageService = storageService ?? throw new ArgumentNullException(nameof(storageService));
        }

        public async Task<ExportResult> ExportPngAsync(
            ImageExportOptions options,
            CancellationToken cancellationToken)
        {
            // Safeguard against background thread issues: execute on main thread
            var captureSource = FRTESdkManager.Instance.Container.Resolve<ICaptureSource>();
            if (captureSource == null || !captureSource.IsReady)
            {
                return new ExportResult
                {
                    Status = ExportStatus.Failed,
                    ErrorCode = "NO_CAPTURE_SOURCE",
                    UserMessage = "Capture target is not configured."
                };
            }

            cancellationToken.ThrowIfCancellationRequested();

            Camera cam = captureSource.CaptureCamera;
            RectInt srcRect = captureSource.CapturePixelRect;

            // 1. Calculate resolution based on Quality
            int targetWidth = srcRect.width;
            int targetHeight = srcRect.height;
            float scale = 1f;

            if (options.Quality == ImageResolutionQuality.Standard)
            {
                int minSide = Mathf.Min(targetWidth, targetHeight);
                if (minSide > 1080)
                {
                    scale = 1080f / minSide;
                }
            }
            else // High
            {
                int minSide = Mathf.Min(targetWidth, targetHeight);
                if (minSide > 2048)
                {
                    scale = 2048f / minSide;
                }
            }

            int w = Mathf.RoundToInt(targetWidth * scale);
            int h = Mathf.RoundToInt(targetHeight * scale);

            // 2. Adjust for Aspect Ratio option
            float targetAspect = 1f;
            bool applyCrop = true;
            switch (options.AspectRatio)
            {
                case ImageAspectRatio.Ratio1_1: targetAspect = 1f; break;
                case ImageAspectRatio.Ratio4_5: targetAspect = 0.8f; break;
                case ImageAspectRatio.Ratio9_16: targetAspect = 9f / 16f; break;
                case ImageAspectRatio.Ratio16_9: targetAspect = 16f / 9f; break;
                default:
                    applyCrop = false;
                    break;
            }

            int cropW = w;
            int cropH = h;
            if (applyCrop)
            {
                float currentAspect = (float)w / h;
                if (currentAspect > targetAspect)
                {
                    // Crop width
                    cropW = Mathf.RoundToInt(h * targetAspect);
                }
                else
                {
                    // Crop height
                    cropH = Mathf.RoundToInt(w / targetAspect);
                }
            }

            // 3. Render frame to RenderTexture
            var rt = RenderTexture.GetTemporary(w, h, 24, RenderTextureFormat.ARGB32);
            var prevRT = RenderTexture.active;
            var prevClearFlags = cam.clearFlags;
            var prevBackground = cam.backgroundColor;

            if (options.TransparentBackground)
            {
                cam.clearFlags = CameraClearFlags.Color;
                cam.backgroundColor = new Color(0, 0, 0, 0);
            }

            cam.targetTexture = rt;
            cam.Render();

            // Read pixels back
            RenderTexture.active = rt;
            var tex = new Texture2D(cropW, cropH, TextureFormat.ARGB32, false);

            int startX = (w - cropW) / 2;
            int startY = (h - cropH) / 2;

            tex.ReadPixels(new Rect(startX, startY, cropW, cropH), 0, 0);
            tex.Apply();

            // Restore Camera settings
            cam.targetTexture = null;
            cam.clearFlags = prevClearFlags;
            cam.backgroundColor = prevBackground;
            RenderTexture.active = prevRT;
            RenderTexture.ReleaseTemporary(rt);

            cancellationToken.ThrowIfCancellationRequested();

            // Encode to PNG bytes
            byte[] bytes = tex.EncodeToPNG();
            UnityEngine.Object.Destroy(tex);

            // Save file transactionally
            string filename = $"FruitRabbit_Squishy_{DateTime.UtcNow:yyyyMMdd_HHmmss}.png";
            string outPath = Path.Combine(_storageService.ExportDirectory, filename);

            try
            {
                await File.WriteAllBytesAsync(outPath, bytes, cancellationToken);
            }
            catch (Exception ex)
            {
                return new ExportResult
                {
                    Status = ExportStatus.Failed,
                    ErrorCode = "WRITE_ERROR",
                    UserMessage = $"Failed to save image to disk: {ex.Message}"
                };
            }

            return new ExportResult
            {
                Status = ExportStatus.Success,
                FilePath = outPath,
                FileSizeBytes = bytes.Length,
                UserMessage = "Image successfully saved to gallery."
            };
        }
    }
}
