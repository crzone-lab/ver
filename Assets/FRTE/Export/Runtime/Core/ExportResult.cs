using System;

namespace FRTE.Export
{
    /// <summary>
    /// Type of exported content format.
    /// </summary>
    public enum ExportType
    {
        Png,
        Mp4,
        Gif
    }

    /// <summary>
    /// Status code of the export operations.
    /// </summary>
    public enum ExportStatus
    {
        Success,
        Failed,
        Cancelled,
        Unsupported
    }

    /// <summary>
    /// Holds the packaged outcome of a rendering export action.
    /// </summary>
    [Serializable]
    public struct ExportResult
    {
        /// <summary>
        /// Gets the final completion status.
        /// </summary>
        public ExportStatus Status;

        /// <summary>
        /// Gets the local absolute path of the generated file.
        /// </summary>
        public string FilePath;

        /// <summary>
        /// Technical diagnosis error code (for logs).
        /// </summary>
        public string ErrorCode;

        /// <summary>
        /// Clean user-facing translation explanation message.
        /// </summary>
        public string UserMessage;

        /// <summary>
        /// Size of the output file in bytes.
        /// </summary>
        public long FileSizeBytes;
    }
}
