using System.Threading;
using System.Threading.Tasks;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for saving, restoring, and clearing active editor sessions to/from persistent local memory.
    /// Uses transactional writes to prevent file corruption.
    /// </summary>
    public interface ISquishyProjectRepository
    {
        /// <summary>
        /// Gets whether a recoverable session is stored.
        /// </summary>
        bool HasRecoverableProject { get; }

        /// <summary>
        /// Saves the active project session.
        /// </summary>
        Task SaveAsync(
            SquishyProjectSessionData session,
            CancellationToken cancellationToken);

        /// <summary>
        /// Restores the last active project session.
        /// </summary>
        Task<SquishyProjectSessionData> LoadAsync(
            CancellationToken cancellationToken);

        /// <summary>
        /// Deletes the cached active project session.
        /// </summary>
        Task DeleteAsync(
            CancellationToken cancellationToken);
    }
}
