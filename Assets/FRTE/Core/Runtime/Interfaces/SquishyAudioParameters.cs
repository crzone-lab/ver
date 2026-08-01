using System;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Material sound effects mapping and mixing parameters.
    /// </summary>
    [Serializable]
    public struct SquishyAudioParameters
    {
        public AudioClip[] TouchClips;
        public AudioClip[] DragClips;
        public AudioClip[] ReleaseClips;
        public AudioClip[] BounceClips;

        public float Volume;
        public Vector2 PitchRange;
        public float MinInterval;
        public int MaxConcurrentVoices;
    }
}
