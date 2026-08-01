using System;
using System.Threading;
using System.Threading.Tasks;

namespace FRTE.Export
{
    /// <summary>
    /// Configuration options for local GIF generation.
    /// </summary>
    [Serializable]
    public struct GifExportOptions
    {
        public int Width;
        public int Height;
        public int FrameRate;
        public float DurationSeconds;
        public int ColorCount;
        public bool Loop;
    }

    /// <summary>
    /// Contract for exporting recorded frame sequences into standard anim-GIFs.
    /// </summary>
    public interface IGifExporter
    {
        /// <summary>
        /// Gets if local GIF encoding is supported on current platform.
        /// </summary>
        bool IsSupported { get; }

        /// <summary>
        /// Compiles a buffered frame sequence into a loopable GIF file.
        /// </summary>
        Task<ExportResult> ExportGifAsync(
            GifExportOptions options,
            CancellationToken cancellationToken);
    }
}
