namespace FRTE.Physics
{
    /// <summary>
    /// Decoupled interface to play tactile haptic feedback impulses.
    /// Adapters execute native platforms (iOS/Android) APIs.
    /// </summary>
    public interface IHapticService
    {
        /// <summary>
        /// Plays a light tactile haptic click.
        /// </summary>
        void PlayLight();

        /// <summary>
        /// Plays a medium strength tactile haptic click.
        /// </summary>
        void PlayMedium();

        /// <summary>
        /// Plays a heavy tactile haptic impact.
        /// </summary>
        void PlayStrong();
    }
}
