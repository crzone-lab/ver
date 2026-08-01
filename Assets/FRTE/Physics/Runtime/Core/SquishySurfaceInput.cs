using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Configuration inputs required to initialize or rebuild a squishy surface simulation.
    /// </summary>
    public struct SquishySurfaceInput
    {
        public Texture2D SourceTexture;
        public float Width;
        public float Height;
        public SquishyMeshQuality Quality;
        public Camera TargetCamera;
        public RectTransform ContainerRect;
    }
}
