using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for the Photo Engine plugin. Handles GPU-based photo operations
    /// (Load, Crop, Rotate, Scale) keeping operations on the GPU to minimize CPU copying.
    /// </summary>
    public interface IPhotoEngine
    {
        RenderTexture WorkingTexture { get; }
        int OriginalWidth { get; }
        int OriginalHeight { get; }
        void LoadPhoto(Texture2D texture);
        void Crop(Rect normalizedRect);
        void Rotate(float angleDegrees);
        void Scale(Vector2 scale);
        void Reset();
    }
}
