using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Struct representing the physical state of a single mesh vertex node.
    /// Packed into flat structures to ensure memory locality and prevent heap allocations.
    /// </summary>
    public struct SquishyVertexState
    {
        public Vector3 InitialPosition;  // Immutable starting rest position
        public Vector3 OriginalPosition; // Mutable rest position (relaxing over time)
        public Vector3 CurrentPosition;
        public Vector3 Velocity;
        public Vector3 AccumulatedForce;
        public float EdgeWeight; // 0.0 at center, up to 1.0 at edges and 1.414 at corners
    }
}
