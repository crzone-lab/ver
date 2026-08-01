using UnityEngine;

namespace FRTE.Effects
{
    /// <summary>
    /// Animates camera shakes using an elastic spring-damping model.
    /// Guarantees smooth, physically realistic shake behaviors without allocating garbage.
    /// </summary>
    public sealed class CameraShaker : MonoBehaviour
    {
        [Header("Spring Constants")]
        [Tooltip("Stiffness of the shake spring (k). Higher values vibrate faster.")]
        [SerializeField] private float stiffness = 120f;

        [Tooltip("Viscous damping of the shake (c). Higher values stop the shake quicker.")]
        [SerializeField] private float damping = 12f;

        private Vector3 _shakeDisplacement;
        private Vector3 _shakeVelocity;
        private Vector3 _originalPosition;
        private bool _isOriginalPosSaved;

        private void Start()
        {
            SaveOriginalPosition();
        }

        private void SaveOriginalPosition()
        {
            if (!_isOriginalPosSaved)
            {
                _originalPosition = transform.localPosition;
                _isOriginalPosSaved = true;
            }
        }

        /// <summary>
        /// Triggers a screen shake by applying an impulse velocity.
        /// </summary>
        /// <param name="intensity">Magnitude of the shake velocity vector.</param>
        /// <param name="direction">Direction of the initial shake impulse.</param>
        public void TriggerShake(float intensity, Vector3 direction)
        {
            SaveOriginalPosition();
            _shakeVelocity += direction.normalized * intensity;
        }

        private void LateUpdate()
        {
            if (!_isOriginalPosSaved) return;

            // Solve Spring-Damping equations: F = -k*x - c*v
            Vector3 force = -stiffness * _shakeDisplacement - damping * _shakeVelocity;

            // Mass = 1.0
            _shakeVelocity += force * Time.deltaTime;
            _shakeDisplacement += _shakeVelocity * Time.deltaTime;

            // Set local position offset
            transform.localPosition = _originalPosition + _shakeDisplacement;

            // Stop update if displacement has converged to zero to conserve CPU cycle
            if (_shakeDisplacement.sqrMagnitude < 0.00001f && _shakeVelocity.sqrMagnitude < 0.00001f)
            {
                _shakeDisplacement = Vector3.zero;
                _shakeVelocity = Vector3.zero;
                transform.localPosition = _originalPosition;
            }
        }

        private void OnDisable()
        {
            if (_isOriginalPosSaved)
            {
                transform.localPosition = _originalPosition;
            }
        }
    }
}
