using UnityEngine;

namespace FRTE.Export
{
    /// <summary>
    /// Contract providing the target capture camera and region for rendering.
    /// Excludes overlay UI canvas layers to capture only content composition.
    /// </summary>
    public interface ICaptureSource
    {
        /// <summary>
        /// Gets the dedicated rendering camera.
        /// </summary>
        Camera CaptureCamera { get; }

        /// <summary>
        /// Gets the pixel crop boundary dimensions of the capture content.
        /// </summary>
        RectInt CapturePixelRect { get; }

        /// <summary>
        /// Gets whether the capture camera is fully configured and ready.
        /// </summary>
        bool IsReady { get; }
    }
}
