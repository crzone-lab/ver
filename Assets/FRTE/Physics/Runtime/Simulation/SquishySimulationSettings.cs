using System;
using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Configurable spring-damper parameters for the squishy physics engine.
    /// Exposed to the inspector and runtime script controllers.
    /// </summary>
    [Serializable]
    public class SquishySimulationSettings
    {
        [Range(0.01f, 1f)] public float TouchRadius = 0.15f;
        [Range(0.1f, 50f)] public float TouchStrength = 15f;
        [Range(0.1f, 50f)] public float DragStrength = 20f;
        [Range(1f, 200f)] public float SpringStrength = 40f;
        [Range(1f, 200f)] public float NeighborSpringStrength = 25f;
        [Range(0.1f, 50f)] public float Damping = 5f;
        [Range(0.1f, 5f)] public float Mass = 1.0f;
        [Range(0.01f, 1f)] public float MaxDisplacement = 0.15f;
        [Range(0.1f, 10f)] public float RecoveryMultiplier = 2.0f;
        [Range(0f, 5f)] public float WobbleAmount = 0.8f;
        [Range(0f, 20f)] public float WobbleFrequency = 8.0f;
        [Range(1f, 5f)] public float EdgeResistance = 2.0f;
        [Range(1f, 100f)] public float MultiTouchForceLimit = 50f;
        [Range(0f, 10f)] public float CreepRate = 1.2f;
        [Range(0f, 10f)] public float CreepRecoveryRate = 2.0f;
    }
}
