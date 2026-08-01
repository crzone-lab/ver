using FRTE.Materials;

namespace FRTE.Surprise
{
    /// <summary>
    /// Contract for evaluating, cooldown caching, and triggering surprise events.
    /// Tracks session interaction progress.
    /// </summary>
    public interface ISurpriseEventController
    {
        bool IsEnabled { get; set; }

        void RegisterInteraction(SquishyInteractionContext context);
        bool TryTriggerEvent();
        void CancelActiveEvents();
        void ResetSessionProgress();
    }
}
