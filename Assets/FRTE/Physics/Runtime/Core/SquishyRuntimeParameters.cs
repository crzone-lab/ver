using System;

namespace FRTE.Physics
{
    /// <summary>
    /// Packaged runtime physical parameters passed to the simulation engine.
    /// Maps from Material Preset definitions.
    /// </summary>
    [Serializable]
    public struct SquishyRuntimeParameters
    {
        public float TouchRadius;
        public float TouchStrength;
        public float DragStrength;
        public float SpringStrength;
        public float NeighborSpringStrength;
        public float Damping;
        public float Mass;
        public float MaxDisplacement;
        public float EdgeResistance;
        public float MultiTouchForceLimit;
        public float WobbleAmount;
        public float WobbleFrequency;
        public float RecoverySpeed;
        public float CreepRate;
        public float CreepRecoveryRate;
    }
}
