using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Data structure representing a detected AI landmark.
    /// Positions are normalized relative to the source image [0.0 - 1.0].
    /// </summary>
    public struct LandmarkData
    {
        public LandmarkType Type { get; }
        public Vector2 Position { get; }
        public float Confidence { get; }

        public LandmarkData(LandmarkType type, Vector2 position, float confidence)
        {
            Type = type;
            Position = position;
            Confidence = confidence;
        }
    }
}
