namespace FRTE.Core
{
    /// <summary>
    /// Contract for the active material preset manager.
    /// Drives physics parameter receivers, audio services, and haptic adjustments.
    /// </summary>
    public interface IMaterialPresetController
    {
        SquishyMaterialPreset CurrentPreset { get; }
        bool ApplyPreset(string presetId);
        bool ApplyPreset(SquishyMaterialPreset preset, bool animateTransition);
        void ApplyDefaultPreset();
    }
}
