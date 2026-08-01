namespace FRTE.Core
{
    /// <summary>
    /// Lifecycle interface for services that require cleanup when the application or scene terminates.
    /// </summary>
    public interface IDisposableService : IService
    {
        /// <summary>
        /// Cleans up service allocations and registrations.
        /// </summary>
        void Dispose();
    }
}
