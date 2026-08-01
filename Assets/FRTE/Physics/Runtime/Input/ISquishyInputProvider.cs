using System.Collections.Generic;

namespace FRTE.Physics
{
    /// <summary>
    /// Provider interface for collecting active touch pointer data.
    /// Decoupled from native Input System to ease unit testing and editor simulation.
    /// </summary>
    public interface ISquishyInputProvider
    {
        /// <summary>
        /// Gets the current number of active touches.
        /// </summary>
        int ActiveTouchCount { get; }

        /// <summary>
        /// Populates a list with structural touch payloads currently active on screen.
        /// </summary>
        /// <param name="results">List to write active touches to.</param>
        void GetActiveTouches(List<SquishyTouchData> results);
    }
}
