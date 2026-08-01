using System;
using System.Threading;
using System.Threading.Tasks;

namespace FRTE.Export
{
    /// <summary>
    /// Share operation result status.
    /// </summary>
    public enum ShareStatus
    {
        Success,
        ShareSheetOpened,
        Cancelled,
        Failed
    }

    /// <summary>
    /// Holds the outcome of a platform sharing action.
    /// </summary>
    [Serializable]
    public struct ShareResult
    {
        public ShareStatus Status;
        public string ErrorCode;
        public string UserMessage;
    }

    /// <summary>
    /// Contract for invoking Android/iOS system Share Sheets.
    /// </summary>
    public interface IShareService
    {
        /// <summary>
        /// Gets if platform sharing sheet invocation is supported.
        /// </summary>
        bool IsSupported { get; }

        /// <summary>
        /// Opens native system sheet to share the exported file.
        /// </summary>
        Task<ShareResult> ShareFileAsync(
            string filePath,
            string mimeType,
            CancellationToken cancellationToken);
    }
}
