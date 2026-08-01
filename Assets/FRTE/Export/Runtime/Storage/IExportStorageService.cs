namespace FRTE.Export
{
    /// <summary>
    /// Contract for directory structure access, cache clearing, and space queries.
    /// </summary>
    public interface IExportStorageService
    {
        /// <summary>
        /// Gets the absolute directory path where temporary frames or recordings are cached.
        /// </summary>
        string TemporaryDirectory { get; }

        /// <summary>
        /// Gets the absolute directory path for finalized user export files.
        /// </summary>
        string ExportDirectory { get; }

        /// <summary>
        /// Checks if the device local partition has sufficient storage space available.
        /// </summary>
        bool HasEnoughSpace(long estimatedBytes);

        /// <summary>
        /// Clears all temporary frame cache and aborted files.
        /// </summary>
        void CleanTemporaryFiles();
    }
}
