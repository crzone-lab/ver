using UnityEngine;

namespace FRTE.Materials
{
    /// <summary>
    /// Details the touch interaction properties passed to the audio service
    /// to modulate pitch, volume, and trigger thresholds dynamically.
    /// </summary>
    public struct SquishyInteractionContext
    {
        public float Speed;
        public float Duration;
        public float Intensity; // Normalized pressure or impact velocity [0.0 - 1.0]
        public Vector2 UV;
    }
}
