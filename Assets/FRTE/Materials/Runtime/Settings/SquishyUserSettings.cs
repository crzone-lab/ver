using System;

namespace FRTE.Materials
{
    /// <summary>
    /// Holds the user's localized customization configuration parameters.
    /// </summary>
    [Serializable]
    public sealed class SquishyUserSettings
    {
        public string SelectedPresetId = "basic.jelly";
        public bool AudioEnabled = true;
        public float AudioVolume = 1f;
        public bool HapticEnabled = true;
        public bool VisualEffectsEnabled = true;
        public float VisualEffectsStrength = 1f;
        public string MeshQuality = "Medium";
    }
}
