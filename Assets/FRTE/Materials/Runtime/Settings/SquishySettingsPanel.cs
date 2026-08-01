using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;
using FRTE.Physics;

namespace FRTE.Materials
{
    /// <summary>
    /// UI panel managing sliders and toggles for user settings:
    /// Sound toggles/volumes, haptics, post-effects toggles/scales, and mesh quality.
    /// </summary>
    public sealed class SquishySettingsPanel : MonoBehaviour
    {
        [Header("UI Bindings")]
        [SerializeField] private Toggle audioToggle;
        [SerializeField] private Slider audioVolumeSlider;
        [SerializeField] private Toggle hapticToggle;
        [SerializeField] private Toggle visualToggle;
        [SerializeField] private Slider visualStrengthSlider;
        [SerializeField] private Button resetButton;

        private ISquishySettingsRepository _settingsRepo;
        private MaterialPresetController _controller;
        private SquishyUserSettings _settings;

        private void Start()
        {
            var container = FRTESdkManager.Instance.Container;
            if (container.TryResolve<ISquishySettingsRepository>(out var repo))
            {
                _settingsRepo = repo;
            }
            if (container.TryResolve<IMaterialPresetController>(out var ctrl))
            {
                _controller = ctrl as MaterialPresetController;
            }

            LoadSettings();

            // Bind listeners
            if (audioToggle != null) audioToggle.onValueChanged.AddListener(OnAudioToggled);
            if (audioVolumeSlider != null) audioVolumeSlider.onValueChanged.AddListener(OnAudioVolumeChanged);
            if (hapticToggle != null) hapticToggle.onValueChanged.AddListener(OnHapticToggled);
            if (visualToggle != null) visualToggle.onValueChanged.AddListener(OnVisualToggled);
            if (visualStrengthSlider != null) visualStrengthSlider.onValueChanged.AddListener(OnVisualStrengthChanged);
            if (resetButton != null) resetButton.onClick.AddListener(OnResetPressed);
        }

        private void LoadSettings()
        {
            if (_settingsRepo == null) return;

            _settings = _settingsRepo.Load();

            if (audioToggle != null) audioToggle.isOn = _settings.AudioEnabled;
            if (audioVolumeSlider != null) audioVolumeSlider.value = _settings.AudioVolume;
            if (hapticToggle != null) hapticToggle.isOn = _settings.HapticEnabled;
            if (visualToggle != null) visualToggle.isOn = _settings.VisualEffectsEnabled;
            if (visualStrengthSlider != null) visualStrengthSlider.value = _settings.VisualEffectsStrength;
        }

        private void OnAudioToggled(bool value)
        {
            _settings.AudioEnabled = value;
            SaveSettings();
        }

        private void OnAudioVolumeChanged(float value)
        {
            _settings.AudioVolume = value;
            SaveSettings();
        }

        private void OnHapticToggled(bool value)
        {
            _settings.HapticEnabled = value;
            SaveSettings();
        }

        private void OnVisualToggled(bool value)
        {
            _settings.VisualEffectsEnabled = value;
            SaveSettings();

            // Refresh visuals on current preset immediately
            if (_controller != null && _controller.CurrentPreset != null)
            {
                _controller.ApplyPreset(_controller.CurrentPreset, animateTransition: false);
            }
        }

        private void OnVisualStrengthChanged(float value)
        {
            _settings.VisualEffectsStrength = value;
            SaveSettings();

            // Refresh visuals on current preset immediately
            if (_controller != null && _controller.CurrentPreset != null)
            {
                _controller.ApplyPreset(_controller.CurrentPreset, animateTransition: false);
            }
        }

        private void OnResetPressed()
        {
            if (_settingsRepo != null)
            {
                _settingsRepo.Reset();
                LoadSettings();

                // Re-apply defaults
                if (_controller != null)
                {
                    _controller.ApplyDefaultPreset();
                }
            }
        }

        private void SaveSettings()
        {
            if (_settingsRepo != null)
            {
                _settingsRepo.Save(_settings);
            }
        }
    }
}
