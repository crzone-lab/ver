using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Implements active App Mode manager coordinating inputs and transitions.
    /// Registers to Core DI.
    /// </summary>
    public sealed class AppModeController : IAppModeController
    {
        public SquishyAppMode CurrentMode { get; private set; } = SquishyAppMode.PhotoEdit;

        public bool ChangeMode(SquishyAppMode mode)
        {
            if (!CanChangeMode(mode)) return false;

            var oldMode = CurrentMode;
            CurrentMode = mode;

            // Broadcast mode change event
            var eventBus = FRTESdkManager.Instance.EventBus;
            if (eventBus != null)
            {
                eventBus.Publish(new AppModeChangedEvent
                {
                    PreviousMode = oldMode,
                    CurrentMode = mode
                });
            }

            Debug.Log($"[AppMode] State transitioned from {oldMode} to {mode}");
            return true;
        }

        public bool CanChangeMode(SquishyAppMode mode)
        {
            // Transition checks
            return true;
        }
    }
}
