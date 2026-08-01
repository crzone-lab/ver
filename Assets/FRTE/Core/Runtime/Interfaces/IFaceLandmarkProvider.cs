namespace FRTE.Core
{
    /// <summary>
    /// Contract for providing AI facial landmark points on the current photo.
    /// Can fallback to Mock data or manual alignment markers.
    /// </summary>
    public interface IFaceLandmarkProvider
    {
        /// <summary>
        /// True if a face has been resolved and landmarks are valid.
        /// </summary>
        bool HasValidFace { get; }

        /// <summary>
        /// Attempts to get the detected landmark data.
        /// </summary>
        bool TryGetLandmarks(out FaceLandmarkData landmarks);
    }
}
