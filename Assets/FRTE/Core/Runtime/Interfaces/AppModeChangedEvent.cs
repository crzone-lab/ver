namespace FRTE.Core
{
    /// <summary>
    /// Event broadcast when the application switches state.
    /// Used by Physics and UI components to lock inputs.
    /// </summary>
    public struct AppModeChangedEvent
    {
        public SquishyAppMode PreviousMode;
        public SquishyAppMode CurrentMode;
    }
}
