using UnityEngine;

namespace FRTE.Materials
{
    /// <summary>
    /// Implements the zero-allocation AudioSource voice pool manager.
    /// Handles random pitch modulation, volume shifts, and interval timers.
    /// </summary>
    public sealed class SquishyAudioService : MonoBehaviour, ISquishyAudioService
    {
        private const int PoolSize = 12;
        private AudioSource[] _voicePool;
        private int _currentVoiceIndex;

        private SquishyAudioParameters _params;
        private bool _hasParams;

        // Category cooldown timers
        private float _lastTouchTime;
        private float _lastDragTime;
        private float _lastReleaseTime;
        private float _lastBounceTime;

        private void Awake()
        {
            // Pre-allocate voice pool
            _voicePool = new AudioSource[PoolSize];
            for (int i = 0; i < PoolSize; i++)
            {
                var sourceGo = new GameObject($"FRTE_Voice_{i}");
                sourceGo.transform.SetParent(transform, false);
                var source = sourceGo.AddComponent<AudioSource>();
                source.playOnAwake = false;
                source.spatialBlend = 0f; // 2D flat sound
                _voicePool[i] = source;
            }
        }

        public void SetAudioParameters(SquishyAudioParameters parameters)
        {
            _params = parameters;
            _hasParams = true;
        }

        public void PlayTouch(SquishyInteractionContext context)
        {
            if (!_hasParams || _params.TouchClips == null || _params.TouchClips.Length == 0) return;
            if (Time.time - _lastTouchTime < _params.MinInterval) return;

            var clip = GetRandomClip(_params.TouchClips);
            if (clip == null) return;

            PlaySound(clip, context.Intensity);
            _lastTouchTime = Time.time;
        }

        public void PlayDrag(SquishyInteractionContext context)
        {
            if (!_hasParams || _params.DragClips == null || _params.DragClips.Length == 0) return;
            if (Time.time - _lastDragTime < _params.MinInterval) return;

            // Only play if moving at significant speed
            if (context.Speed < 0.1f) return;

            var clip = GetRandomClip(_params.DragClips);
            if (clip == null) return;

            // Modulate pitch and volume based on speed
            float pitchMod = Mathf.Clamp(context.Speed * 0.2f, 0.9f, 1.25f);
            float volumeMod = Mathf.Clamp01(context.Speed * 0.5f);

            PlaySound(clip, context.Intensity * volumeMod, pitchMod);
            _lastDragTime = Time.time;
        }

        public void PlayRelease(SquishyInteractionContext context)
        {
            if (!_hasParams || _params.ReleaseClips == null || _params.ReleaseClips.Length == 0) return;
            if (Time.time - _lastReleaseTime < _params.MinInterval) return;

            // Prevent overlapping with Touch sounds if touch was extremely brief
            if (context.Duration < 0.08f) return;

            var clip = GetRandomClip(_params.ReleaseClips);
            if (clip == null) return;

            PlaySound(clip, context.Intensity);
            _lastReleaseTime = Time.time;
        }

        public void PlayBounce(SquishyInteractionContext context)
        {
            if (!_hasParams || _params.BounceClips == null || _params.BounceClips.Length == 0) return;
            if (Time.time - _lastBounceTime < _params.MinInterval) return;

            var clip = GetRandomClip(_params.BounceClips);
            if (clip == null) return;

            PlaySound(clip, context.Intensity);
            _lastBounceTime = Time.time;
        }

        public void StopAll()
        {
            for (int i = 0; i < PoolSize; i++)
            {
                if (_voicePool[i] != null && _voicePool[i].isPlaying)
                {
                    _voicePool[i].Stop();
                }
            }
        }

        /// <summary>
        /// Gets the current number of active playing AudioSources.
        /// </summary>
        public int ActiveVoiceCount
        {
            get
            {
                int count = 0;
                if (_voicePool != null)
                {
                    for (int i = 0; i < PoolSize; i++)
                    {
                        if (_voicePool[i] != null && _voicePool[i].isPlaying) count++;
                    }
                }
                return count;
            }
        }

        private void PlaySound(AudioClip clip, float intensity, float customPitchFactor = 1f)
        {
            // Find next available AudioSource
            var source = FindIdleVoice();
            if (source == null) return;

            // Set Clip
            source.clip = clip;

            // Apply Pitch Randomization within PitchRange
            float minPitch = _params.PitchRange.x > 0.1f ? _params.PitchRange.x : 0.9f;
            float maxPitch = _params.PitchRange.y > 0.1f ? _params.PitchRange.y : 1.1f;
            source.pitch = Random.Range(minPitch, maxPitch) * customPitchFactor;

            // Apply Volume Scaling
            float baseVol = _params.Volume > 0.001f ? _params.Volume : 1f;
            source.volume = baseVol * Mathf.Clamp01(intensity) * Random.Range(0.92f, 1.08f);

            source.Play();

            // Notify Event Bus for debug logging / testing
            var eventBus = FRTE.Core.FRTESdkManager.Instance.EventBus;
            if (eventBus != null)
            {
                eventBus.Publish(new SquishyAudioPlayedEvent { ClipName = clip.name, Pitch = source.pitch, Volume = source.volume });
            }
        }

        private AudioSource FindIdleVoice()
        {
            int concurrentLimit = _params.MaxConcurrentVoices > 0 ? _params.MaxConcurrentVoices : PoolSize;

            // 1. Try to find a non-playing source within limit
            int activeCount = 0;
            for (int i = 0; i < PoolSize; i++)
            {
                if (_voicePool[i].isPlaying) activeCount++;
            }

            if (activeCount >= concurrentLimit)
            {
                // Voice limit reached; skip to prevent sound clutter
                return null;
            }

            // 2. Scan sequentially for a free source
            for (int i = 0; i < PoolSize; i++)
            {
                int idx = (_currentVoiceIndex + i) % PoolSize;
                if (!_voicePool[idx].isPlaying)
                {
                    _currentVoiceIndex = (idx + 1) % PoolSize;
                    return _voicePool[idx];
                }
            }

            // 3. Fallback: override oldest voice if pool is full
            int overrideIndex = _currentVoiceIndex;
            _currentVoiceIndex = (_currentVoiceIndex + 1) % PoolSize;
            return _voicePool[overrideIndex];
        }

        private AudioClip GetRandomClip(AudioClip[] clips)
        {
            if (clips == null || clips.Length == 0) return null;
            if (clips.Length == 1) return clips[0];
            return clips[Random.Range(0, clips.Length)];
        }
    }

    /// <summary>
    /// Event broadcast when a sound effect successfully plays.
    /// Used for diagnostics and unit test verification.
    /// </summary>
    public struct SquishyAudioPlayedEvent
    {
        public string ClipName;
        public float Pitch;
        public float Volume;
    }
}
