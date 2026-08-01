using System;

namespace FRTE.Core
{
    /// <summary>
    /// Material physical configuration parameters.
    /// Values are validated and mapped to the physics simulation step settings.
    /// </summary>
    [Serializable]
    public struct SquishyPhysicsParameters
    {
        public float TouchRadiusMultiplier;
        public float TouchStrengthMultiplier;
        public float DragStrengthMultiplier;

        public float SpringStrength;
        public float NeighborSpringStrength;
        public float Damping;
        public float Mass;

        public float Compression;
        public float Stretch;
        public float Viscosity;
        public float Elasticity;

        public float RecoverySpeed;
        public float Bounce;
        public float WobbleAmount;
        public float WobbleFrequency;

        public float MaxDisplacementMultiplier;
        public float EdgeResistanceMultiplier;
        public float MultiTouchForceLimitMultiplier;

        public float HoldResponse;
        public float FastTapImpulse;
        public float DragFollowDelay;
    }
}
