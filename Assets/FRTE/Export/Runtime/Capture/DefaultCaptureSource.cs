using UnityEngine;

namespace FRTE.Export
{
    /// <summary>
    /// Fallback ICaptureSource implementation utilizing the Main Camera and full screen dimensions.
    /// </summary>
    public sealed class DefaultCaptureSource : ICaptureSource
    {
        public Camera CaptureCamera
        {
            get
            {
                var main = Camera.main;
                if (main != null) return main;

                // Fallback scan
                var cams = Object.FindObjectsByType<Camera>(FindObjectsSortMode.None);
                if (cams.Length > 0) return cams[0];

                // Create dummy camera to prevent null reference errors
                var go = new GameObject("CaptureCameraFallback");
                var dummy = go.AddComponent<Camera>();
                dummy.enabled = false;
                return dummy;
            }
        }

        public RectInt CapturePixelRect => new RectInt(0, 0, Screen.width > 0 ? Screen.width : 1080, Screen.height > 0 ? Screen.height : 1920);
        
        public bool IsReady => CaptureCamera != null;
    }
}
