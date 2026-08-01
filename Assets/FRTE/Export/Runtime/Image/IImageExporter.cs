using System;
using System.Threading;
using System.Threading.Tasks;

namespace FRTE.Export
{
    /// <summary>
    /// Aspect ratio options for cropping captured images.
    /// </summary>
    public enum ImageAspectRatio
    {
        Original,
        Ratio1_1,
        Ratio4_5,
        Ratio9_16,
        Ratio16_9
    }

    /// <summary>
    /// Output resolution options.
    /// </summary>
    public enum ImageResolutionQuality
    {
        Standard,
        High
    }

    /// <summary>
    /// Configuration options for image rendering exports.
    /// </summary>
    [Serializable]
    public struct ImageExportOptions
    {
        public ImageAspectRatio AspectRatio;
        public ImageResolutionQuality Quality;
        public bool TransparentBackground;
    }

    /// <summary>
    /// Contract for rendering static images from capture cameras.
    /// </summary>
    public interface IImageExporter
    {
        /// <summary>
        /// Executes asynchronous static rendering to transparent or opaque PNG.
        /// </summary>
        Task<ExportResult> ExportPngAsync(
            ImageExportOptions options,
            CancellationToken cancellationToken);
    }
}
