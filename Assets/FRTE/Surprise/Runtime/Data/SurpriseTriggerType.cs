namespace FRTE.Surprise
{
    /// <summary>
    /// Enumerates touch interaction triggers capable of firing surprise events.
    /// </summary>
    public enum SurpriseTriggerType
    {
        TapCount,
        ConsecutiveTap,
        LongPress,
        StrongPull,
        SpecificArea,
        RandomChance,
        MaterialSpecific,
        PhotoZoneSpecific
    }
}
