namespace FRTE.Materials
{
    /// <summary>
    /// Contract for playing structural touch/drag/release/bounce effects.
    /// Utilizes pre-allocated AudioSource voice pooling.
    /// </summary>
    public interface ISquishyAudioService
    {
        /// <summary>
        /// Plays a sound effect when a touch began interaction starts.
        /// </summary>
        void PlayTouch(SquishyInteractionContext context);

        /// <summary>
        /// Plays a sliding friction sound when a pointer drags across the surface.
        /// </summary>
        void PlayDrag(SquishyInteractionContext context);

        /// <summary>
        /// Plays a release sound when a finger is lifted.
        /// </summary>
        void PlayRelease(SquishyInteractionContext context);

        /// <summary>
        /// Plays an impact sound on spring-damping wobble peaks.
        /// </summary>
        void PlayBounce(SquishyInteractionContext context);

        /// <summary>
        /// Configures active audio parameters (Clips, Volume, Pitch, Cooldowns).
        /// </summary>
        void SetAudioParameters(SquishyAudioParameters parameters);

        /// <summary>
        /// Stops all active sound effects.
        /// </summary>
        void StopAll();
    }
}
