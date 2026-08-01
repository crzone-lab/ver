using System;
using System.Threading;
using System.Threading.Tasks;

namespace FRTE.Export
{
    /// <summary>
    /// Lifecycle states for video recording sequences.
    /// </summary>
    public enum RecordingState
    {
        Idle,
        Preparing,
        Countdown,
        Recording,
        Stopping,
        Encoding,
        Completed,
        Failed,
        Cancelled
    }

    /// <summary>
    /// Configuration options for video encoding.
    /// </summary>
    [Serializable]
    public struct VideoExportOptions
    {
        public int Width;
        public int Height;
        public int FrameRate;
        public float MaxDurationSeconds;
        public bool IncludeAudio;
    }

    /// <summary>
    /// Contract for recording local gameplay interaction and encoding to MP4.
    /// </summary>
    public interface IVideoExporter
    {
        /// <summary>
        /// Gets if video recording encoding is supported on current hardware platform.
        /// </summary>
        bool IsSupported { get; }

        /// <summary>
        /// Gets the current lifecycle recording state.
        /// </summary>
        RecordingState CurrentState { get; }

        /// <summary>
        /// Initiates recording of the target capture stream.
        /// </summary>
        Task<ExportResult> StartRecordingAsync(
            VideoExportOptions options,
            CancellationToken cancellationToken);

        /// <summary>
        /// Gracefully finishes recording and triggers local MP4 encoding.
        /// </summary>
        Task<ExportResult> StopRecordingAsync(
            CancellationToken cancellationToken);

        /// <summary>
        /// Aborts recording and cleans up temporary file buffers immediately.
        /// </summary>
        void CancelRecording();
    }
}
