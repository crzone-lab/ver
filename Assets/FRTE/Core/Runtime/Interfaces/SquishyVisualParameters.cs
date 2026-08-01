using System;

namespace FRTE.Core
{
    /// <summary>
    /// Material visual rendering attributes applied to the mesh shader.
    /// </summary>
    [Serializable]
    public struct SquishyVisualParameters
    {
        public float HighlightStrength;
        public float Glossiness;
        public float RimStrength;
        public float TransparencyEffect;
        public float RefractionStrength;
        public float SurfaceNoiseStrength;
        public float SaturationMultiplier;
        public float BrightnessMultiplier;
        public float OverlayOpacity;
    }
}
