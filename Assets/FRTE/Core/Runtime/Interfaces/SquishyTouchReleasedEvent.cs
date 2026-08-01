using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Event broadcast when a screen pointer ends touch interaction.
    /// </summary>
    public struct SquishyTouchReleasedEvent
    {
        public int TouchId;
        public Vector2 UV;
        public float Duration;
    }
}
