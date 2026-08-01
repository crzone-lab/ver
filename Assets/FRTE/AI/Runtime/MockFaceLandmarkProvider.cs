using UnityEngine;
using FRTE.Core;

namespace FRTE.AI
{
    /// <summary>
    /// Implements IFaceLandmarkProvider with options for manual point overrides.
    /// Supports automatic mock face placement when no manual markers are set.
    /// </summary>
    public sealed class MockFaceLandmarkProvider : IFaceLandmarkProvider
    {
        private FaceLandmarkData _manualLandmarks;
        private bool _hasManualOverride;

        public bool HasValidFace => _hasManualOverride || true; // always valid for mock fallbacks

        public void SetManualOverride(FaceLandmarkData data)
        {
            _manualLandmarks = data;
            _hasManualOverride = true;
        }

        public void ClearManualOverride()
        {
            _hasManualOverride = false;
        }

        public bool TryGetLandmarks(out FaceLandmarkData landmarks)
        {
            if (_hasManualOverride)
            {
                landmarks = _manualLandmarks;
                return true;
            }

            // Fallback default mock landmark placements
            landmarks = new FaceLandmarkData
            {
                FaceCenter = Vector2.zero,
                LeftEye = new Vector2(-0.1f, 0.05f),
                RightEye = new Vector2(0.1f, 0.05f),
                LeftCheek = new Vector2(-0.15f, -0.05f),
                RightCheek = new Vector2(0.15f, -0.05f),
                Chin = new Vector2(0f, -0.2f),
                Forehead = new Vector2(0f, 0.2f),
                HeadTop = new Vector2(0f, 0.35f),
                FaceRotation = 0f,
                FaceWidth = 0.5f,
                FaceHeight = 0.6f
            };
            return true;
        }
    }
}
