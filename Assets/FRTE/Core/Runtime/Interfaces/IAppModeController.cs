namespace FRTE.Core
{
    /// <summary>
    /// Contract for controlling the active app mode (PhotoEdit, Play, Decoration, PhotoZone, Collection).
    /// Resolves conflicts in screen-touch and drag handlers.
    /// </summary>
    public interface IAppModeController
    {
        /// <summary>
        /// Gets the current active mode.
        /// </summary>
        SquishyAppMode CurrentMode { get; }

        /// <summary>
        /// Requests state transition to a new app mode.
        /// </summary>
        bool ChangeMode(SquishyAppMode mode);

        /// <summary>
        /// Checks if transition is allowed under current session state.
        /// </summary>
        bool CanChangeMode(SquishyAppMode mode);
    }
}
