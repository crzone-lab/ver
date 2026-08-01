using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Event broadcast when a screen pointer begins touch interaction.
    /// </summary>
    public struct SquishyTouchStartedEvent
    {
        public int TouchId;
        public Vector2 UV;
        public float TimeStamp;
    }
}
