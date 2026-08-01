using System.Threading.Tasks;
using UnityEngine;
using FRTE.Core;

namespace FRTE.AI
{
    /// <summary>
    /// Mock AI provider for editor testing and platform fallback.
    /// Simulates facial landmark positions on loaded images.
    /// </summary>
    public sealed class MockAIDetectionProvider : IAIDetectionProvider, IPlugin
    {
        public string PluginId => "FRTE.MockAIDetection";
        public bool IsEnabled { get; private set; }
        public bool IsSupported => true;

        public void Initialize(FRTEContainer container)
        {
            container.Register<IAIDetectionProvider>(this);
            container.Register<ISubjectMaskProvider>(new MockSubjectMaskProvider());
            container.Register<IFaceLandmarkProvider>(new MockFaceLandmarkProvider());
        }

        public void Enable()
        {
            IsEnabled = true;
        }

        public void Disable()
        {
            IsEnabled = false;
        }

        public Task<LandmarkData[]> DetectLandmarksAsync(Texture texture)
        {
            // Simulate processing time
            if (texture == null)
            {
                return Task.FromResult(System.Array.Empty<LandmarkData>());
            }

            // Create mocked facial landmark data centered on the texture
            var landmarks = new LandmarkData[]
            {
                new LandmarkData(LandmarkType.FaceCenter, new Vector2(0.5f, 0.5f), 0.98f),
                new LandmarkData(LandmarkType.LeftEye, new Vector2(0.42f, 0.55f), 0.95f),
                new LandmarkData(LandmarkType.RightEye, new Vector2(0.58f, 0.55f), 0.95f),
                new LandmarkData(LandmarkType.NoseBridge, new Vector2(0.5f, 0.52f), 0.92f),
                new LandmarkData(LandmarkType.NoseTip, new Vector2(0.5f, 0.47f), 0.96f),
                new LandmarkData(LandmarkType.MouthCenter, new Vector2(0.5f, 0.38f), 0.94f),
                new LandmarkData(LandmarkType.LeftMouthCorner, new Vector2(0.44f, 0.38f), 0.90f),
                new LandmarkData(LandmarkType.RightMouthCorner, new Vector2(0.56f, 0.38f), 0.90f),
                new LandmarkData(LandmarkType.JawLine, new Vector2(0.5f, 0.25f), 0.85f),
                new LandmarkData(LandmarkType.HairLine, new Vector2(0.5f, 0.75f), 0.80f),
                new LandmarkData(LandmarkType.LeftEar, new Vector2(0.32f, 0.52f), 0.88f),
                new LandmarkData(LandmarkType.RightEar, new Vector2(0.68f, 0.52f), 0.88f)
            };

            return Task.FromResult(landmarks);
        }
    }
}
