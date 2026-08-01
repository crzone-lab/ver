namespace FRTE.Physics
{
    /// <summary>
    /// Contract for the core spring-damper physical simulation.
    /// Handles updating simulation frames and resetting state.
    /// </summary>
    public interface ISquishySimulation
    {
        /// <summary>
        /// Executes a single simulation step.
        /// </summary>
        /// <param name="deltaTime">Elapsed frame time.</param>
        void Step(float deltaTime);

        /// <summary>
        /// Resets the simulation grid nodes back to their resting states.
        /// </summary>
        void ResetSimulation();
    }
}
