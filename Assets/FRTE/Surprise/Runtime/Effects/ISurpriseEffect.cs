using UnityEngine;

namespace FRTE.Surprise
{
    /// <summary>
    /// Contract for a pooled visual surprise event effect representation (e.g. particles, popups).
    /// </summary>
    public interface ISurpriseEffect
    {
        string EffectId { get; }
        bool IsActive { get; }
        GameObject GameObject { get; }

        void Play(Vector2 normalizedUV, float duration);
        void Stop();
    }
}
