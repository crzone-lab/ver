namespace FRTE.Physics
{
    /// <summary>
    /// Contract for physics components capable of receiving dynamic parameter overrides.
    /// Used by the Material preset controller to apply structural settings smoothly.
    /// </summary>
    public interface ISquishyParameterReceiver
    {
        /// <summary>
        /// Gets the current active runtime parameters.
        /// </summary>
        SquishyRuntimeParameters CurrentParameters { get; }

        /// <summary>
        /// Applies new physical parameters with transition interpolation options.
        /// </summary>
        /// <param name="parameters">The target configuration parameters.</param>
        /// <param name="transitionOptions">The transition duration and curves.</param>
        void ApplyParameters(SquishyRuntimeParameters parameters, MaterialTransitionOptions transitionOptions);
    }
}
