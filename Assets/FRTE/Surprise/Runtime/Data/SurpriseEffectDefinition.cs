using System;
using UnityEngine;

namespace FRTE.Surprise
{
    /// <summary>
    /// Configures visual asset properties and parameters for surprise event effects.
    /// </summary>
    [Serializable]
    public struct SurpriseEffectDefinition
    {
        public string EffectId; // e.g. "effect.fruit_pop", "effect.heart_burst"
        public float Duration;
        public Vector2 Scale;
        public float ParticleCount;
        public Color CustomColor;
    }
}
