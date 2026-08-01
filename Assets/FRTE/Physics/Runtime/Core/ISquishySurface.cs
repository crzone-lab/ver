namespace FRTE.Physics
{
    /// <summary>
    /// Core interface representing a squishy deform surface.
    /// Exposes state management and controls rebuilding/resetting layout.
    /// </summary>
    public interface ISquishySurface
    {
        /// <summary>
        /// Gets a value indicating whether the surface has been initialized.
        /// </summary>
        bool IsInitialized { get; }

        /// <summary>
        /// Initializes the surface simulation with configuration inputs.
        /// </summary>
        /// <param name="input">Configuration parameters.</param>
        void Initialize(SquishySurfaceInput input);

        /// <summary>
        /// Resets the physics simulation state and mesh vertices.
        /// </summary>
        void ResetSurface();

        /// <summary>
        /// Rebuilds the surface (e.g. on photo swap or resolution change).
        /// </summary>
        /// <param name="input">New configuration parameters.</param>
        void RebuildSurface(SquishySurfaceInput input);
    }
}
