using System.Threading.Tasks;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Core interface for AI landmark detection providers.
    /// Enables integration with native iOS (CoreML/Vision) and Android (MLKit) SDKs.
    /// </summary>
    public interface IAIDetectionProvider
    {
        bool IsSupported { get; }
        Task<LandmarkData[]> DetectLandmarksAsync(Texture texture);
    }
}
