using System;

namespace FRTE.Core
{
    /// <summary>
    /// Material haptic feedback mapping parameters.
    /// </summary>
    [Serializable]
    public struct SquishyHapticParameters
    {
        public bool Enabled;
        public float TouchIntensity;
        public float DragIntensity;
        public float ReleaseIntensity;
        public float BounceIntensity;
        public float MinInterval;
    }
}
