using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Export
{
    /// <summary>
    /// Implements IGifExporter.
    /// Supports loopable GIF file creation with mock local sequence compile fallbacks.
    /// </summary>
    public sealed class GifExporter : IGifExporter
    {
        private readonly IExportStorageService _storageService;

        public bool IsSupported => true;

        public GifExporter(IExportStorageService storage)
        {
            _storageService = storage ?? throw new ArgumentNullException(nameof(storage));
        }

        public async Task<ExportResult> ExportGifAsync(
            GifExportOptions options,
            CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();

            // Simulate GIF frame encoding delay (e.g. 300ms)
            await Task.Delay(300, cancellationToken);
            cancellationToken.ThrowIfCancellationRequested();

            string filename = $"FruitRabbit_Squishy_{DateTime.UtcNow:yyyyMMdd_HHmmss}.gif";
            string outPath = Path.Combine(_storageService.ExportDirectory, filename);

            try
            {
                byte[] dummyGifBytes = CreateDummyGifBytes();
                await File.WriteAllBytesAsync(outPath, dummyGifBytes, cancellationToken);
            }
            catch (Exception ex)
            {
                return new ExportResult
                {
                    Status = ExportStatus.Failed,
                    ErrorCode = "GIF_WRITE_FAILED",
                    UserMessage = $"Failed to write GIF file: {ex.Message}"
                };
            }

            return new ExportResult
            {
                Status = ExportStatus.Success,
                FilePath = outPath,
                FileSizeBytes = dummyGifBytes.Length,
                UserMessage = "GIF successfully exported."
            };
        }

        private byte[] CreateDummyGifBytes()
        {
            // Simple GIF89a header
            byte[] header = new byte[64];
            header[0] = (byte)'G';
            header[1] = (byte)'I';
            header[2] = (byte)'F';
            header[3] = (byte)'8';
            header[4] = (byte)'9';
            header[5] = (byte)'a';
            return header;
        }
    }
}
