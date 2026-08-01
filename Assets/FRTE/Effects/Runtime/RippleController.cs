using UnityEngine;

namespace FRTE.Effects
{
    /// <summary>
    /// Animates pixel-refractive ripple parameters on a material using DeformableJelly shader.
    /// Manages wave propagation and amplitude decay over time.
    /// </summary>
    public sealed class RippleController : MonoBehaviour
    {
        [Header("Ripple Performance")]
        [Tooltip("How fast the ripple fades away.")]
        [SerializeField] private float fadeSpeed = 3.5f;

        [Tooltip("Frequency of the waves.")]
        [SerializeField] private float waveFrequency = 18f;

        [Tooltip("Speed of wave expansion.")]
        [SerializeField] private float waveSpeed = 8f;

        private Material _jellyMaterial;
        private float _currentAmplitude;
        private Vector2 _rippleCenter;

        private static readonly int RippleCenterProp = Shader.PropertyToID("_RippleCenter");
        private static readonly int RippleParamsProp = Shader.PropertyToID("_RippleParams");

        private void Start()
        {
            var renderer = GetComponent<Renderer>();
            if (renderer != null)
            {
                _jellyMaterial = renderer.material;
            }
        }

        /// <summary>
        /// Triggers a ripple originating at the specified UV coordinate.
        /// </summary>
        /// <param name="normalizedUV">Center coordinates of the ripple [0.0 - 1.0].</param>
        /// <param name="intensity">Initial amplitude of the waves.</param>
        public void TriggerRipple(Vector2 normalizedUV, float intensity)
        {
            _rippleCenter = normalizedUV;
            _currentAmplitude = intensity;

            if (_jellyMaterial != null)
            {
                _jellyMaterial.SetVector(RippleCenterProp, new Vector4(normalizedUV.x, normalizedUV.y, 0f, 0f));
            }
        }

        private void Update()
        {
            if (_jellyMaterial == null || _currentAmplitude < 0.0001f) return;

            // Decay the ripple amplitude exponentially
            _currentAmplitude = Mathf.Lerp(_currentAmplitude, 0f, Time.deltaTime * fadeSpeed);

            // Pass updated parameters: x = Amplitude, y = Frequency, z = Speed, w = Decay Rate
            Vector4 rippleParams = new Vector4(_currentAmplitude, waveFrequency, waveSpeed, fadeSpeed);
            _jellyMaterial.SetVector(RippleParamsProp, rippleParams);
        }

        private void OnDestroy()
        {
            if (_jellyMaterial != null)
            {
                DestroyImmediate(_jellyMaterial);
            }
        }
    }
}
