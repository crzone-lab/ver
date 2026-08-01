namespace FRTE.Physics
{
    /// <summary>
    /// Event broadcast when haptic feedback triggers.
    /// Used for diagnostic and automated PlayMode validation.
    /// </summary>
    public struct SquishyHapticTriggeredEvent
    {
        public int Level; // 1 = Light, 2 = Medium, 3 = Strong
    }
}
