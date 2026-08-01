using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Represents structural information for an active touch point.
    /// Used to pass screen touch state to coordinate transformer and simulation.
    /// </summary>
    public struct SquishyTouchData
    {
        public int TouchId;
        public Vector2 ScreenPosition;
        public Vector2 PreviousScreenPosition;
        public Vector2 Delta;
        public float Duration;
        public float Speed;
        public SquishyTouchPhase Phase;
    }
}
