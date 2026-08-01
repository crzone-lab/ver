using System;
using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Configures transition interpolation options when switching surface materials.
    /// </summary>
    [Serializable]
    public struct MaterialTransitionOptions
    {
        public bool Animate;
        public float Duration;
        public AnimationCurve Curve;
        public bool PreserveCurrentDeformation;
    }
}
