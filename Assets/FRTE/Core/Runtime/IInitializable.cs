namespace FRTE.Core
{
    /// <summary>
    /// Lifecycle interface for services that require custom startup initialization.
    /// </summary>
    public interface IInitializable
    {
        /// <summary>
        /// Initializes the service.
        /// </summary>
        void Initialize();
    }
}
