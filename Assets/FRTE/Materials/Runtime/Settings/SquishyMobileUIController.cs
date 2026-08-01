using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;
using FRTE.Physics;

namespace FRTE.Materials
{
    /// <summary>
    /// Master UI Controller for the portrait mobile canvas overlay.
    /// Manages character popups, feel preset popups, capturing photos, recording video clips,
    /// and autopilot diagnostics triggers, matching the HTML5 web-simulator interface.
    /// </summary>
    public sealed class SquishyMobileUIController : MonoBehaviour
    {
        [Header("Top Bar Buttons")]
        [SerializeField] private Button settingsBtn;
        [SerializeField] private Button characterMenuBtn;
        [SerializeField] private Button feelMenuBtn;
        [SerializeField] private Button photoCaptureBtn;
        [SerializeField] private Button videoRecordBtn;
        [SerializeField] private Button autopilotBtn;

        [Header("Popup Overlays")]
        [SerializeField] private GameObject settingsPanel;
        [SerializeField] private GameObject characterPopPanel;
        [SerializeField] private GameObject feelPopPanel;
        [SerializeField] private GameObject resultPreviewModal;

        [Header("Character Selection Cards")]
        [SerializeField] private Button cardStrawberry;
        [SerializeField] private Button cardLemon;
        [SerializeField] private Button cardPeach;
        [SerializeField] private Button cardCamera;
        [SerializeField] private Button cardIllust;

        [Header("Feel Selection Cards")]
        [SerializeField] private Button cardFeelJelly;
        [SerializeField] private Button cardFeelMochi;
        [SerializeField] private Button cardFeelSlime;

        [Header("Overlays & Indicators")]
        [SerializeField] private Image cameraFlashOverlay;
        [SerializeField] private Text countdownText;
        [SerializeField] private GameObject recordingIndicator;
        [SerializeField] private Text recordingTimerText;
        [SerializeField] private Text resultModalStatusText;

        [Header("Target Deformable Mesh")]
        [SerializeField] private SquishySurface targetSurface;

        private IMaterialPresetController _presetController;
        private IMaterialPresetProvider _presetProvider;
        private bool _isAutopilotActive;
        private Coroutine _recordingCoroutine;

        private void Start()
        {
            // Resolve dependencies from FRTE container
            var container = FRTESdkManager.Instance.Container;
            if (container != null)
            {
                container.TryResolve<IMaterialPresetController>(out _presetController);
                container.TryResolve<IMaterialPresetProvider>(out _presetProvider);
            }

            // Bind top menu listeners
            if (settingsBtn != null) settingsBtn.onClick.AddListener(ToggleSettings);
            if (characterMenuBtn != null) characterMenuBtn.onClick.AddListener(() => TogglePopup(characterPopPanel));
            if (feelMenuBtn != null) feelMenuBtn.onClick.AddListener(() => TogglePopup(feelPopPanel));
            if (photoCaptureBtn != null) photoCaptureBtn.onClick.AddListener(CapturePhotoInstant);
            if (videoRecordBtn != null) videoRecordBtn.onClick.AddListener(StartVideoRecordingInstant);
            if (autopilotBtn != null) autopilotBtn.onClick.AddListener(ToggleAutopilot);

            // Bind character cards
            if (cardStrawberry != null) cardStrawberry.onClick.AddListener(() => SelectCharacter("strawberry_rabbit"));
            if (cardLemon != null) cardLemon.onClick.AddListener(() => SelectCharacter("lemon_rabbit"));
            if (cardPeach != null) cardPeach.onClick.AddListener(() => SelectCharacter("peach_rabbit"));
            if (cardCamera != null) cardCamera.onClick.AddListener(() => SelectCharacter("camera_face"));
            if (cardIllust != null) cardIllust.onClick.AddListener(() => SelectCharacter("illust_body"));

            // Bind feel cards
            if (cardFeelJelly != null) cardFeelJelly.onClick.AddListener(() => SelectFeelPreset("jelly"));
            if (cardFeelMochi != null) cardFeelMochi.onClick.AddListener(() => SelectFeelPreset("mochi"));
            if (cardFeelSlime != null) cardFeelSlime.onClick.AddListener(() => SelectFeelPreset("slime"));

            // Close panels initially
            CloseAllPopups();
        }

        private void ToggleSettings()
        {
            if (settingsPanel != null)
            {
                bool active = !settingsPanel.activeSelf;
                CloseAllPopups();
                settingsPanel.SetActive(active);
            }
        }

        private void TogglePopup(GameObject popup)
        {
            if (popup != null)
            {
                bool active = !popup.activeSelf;
                CloseAllPopups();
                popup.SetActive(active);
            }
        }

        private void CloseAllPopups()
        {
            if (settingsPanel != null) settingsPanel.SetActive(false);
            if (characterPopPanel != null) characterPopPanel.SetActive(false);
            if (feelPopPanel != null) feelPopPanel.SetActive(false);
        }

        private void SelectCharacter(string characterId)
        {
            Debug.Log($"[MobileUI] Character selected: {characterId}");
            
            // In a real Unity implementation, this updates the texture and shape bounds on the SquishySurface.
            CloseAllPopups();
        }

        private void SelectFeelPreset(string presetId)
        {
            if (_presetController != null)
            {
                _presetController.ApplyPreset(presetId);
                Debug.Log($"[MobileUI] Preset selected: {presetId}");
            }
            CloseAllPopups();
        }

        private void CapturePhotoInstant()
        {
            StartCoroutine(FlashEffectCoroutine());
            if (resultPreviewModal != null)
            {
                resultPreviewModal.SetActive(true);
                if (resultModalStatusText != null)
                {
                    resultModalStatusText.text = "📸 스냅샷 이미지가 갤러리에 저장되었습니다!";
                }
            }
        }

        private System.Collections.IEnumerator FlashEffectCoroutine()
        {
            if (cameraFlashOverlay != null)
            {
                cameraFlashOverlay.gameObject.SetActive(true);
                cameraFlashOverlay.color = Color.white;
                float elapsed = 0f;
                float duration = 0.2f;
                while (elapsed < duration)
                {
                    elapsed += Time.deltaTime;
                    float alpha = Mathf.Lerp(1f, 0f, elapsed / duration);
                    cameraFlashOverlay.color = new Color(1f, 1f, 1f, alpha);
                    yield return null;
                }
                cameraFlashOverlay.gameObject.SetActive(false);
            }
        }

        private void StartVideoRecordingInstant()
        {
            StartCoroutine(RecordingCountdownCoroutine());
        }

        private System.Collections.IEnumerator RecordingCountdownCoroutine()
        {
            if (countdownText != null)
            {
                countdownText.gameObject.SetActive(true);
                for (int i = 3; i > 0; i--)
                {
                    countdownText.text = i.ToString();
                    yield return new WaitForSeconds(0.8f);
                }
                countdownText.gameObject.SetActive(false);
            }

            // Start Rec Loop
            if (_recordingCoroutine != null) StopCoroutine(_recordingCoroutine);
            _recordingCoroutine = StartCoroutine(RecordingTimerCoroutine());
        }

        private System.Collections.IEnumerator RecordingTimerCoroutine()
        {
            if (recordingIndicator != null) recordingIndicator.SetActive(true);
            int duration = 0;
            while (duration < 5)
            {
                if (recordingTimerText != null)
                {
                    recordingTimerText.text = $"00:0{duration}";
                }
                yield return new WaitForSeconds(1.0f);
                duration++;
            }
            if (recordingIndicator != null) recordingIndicator.SetActive(false);

            // Open result modal
            if (resultPreviewModal != null)
            {
                resultPreviewModal.SetActive(true);
                if (resultModalStatusText != null)
                {
                    resultModalStatusText.text = "🎬 비디오 녹화 미리보기가 준비되었습니다!";
                }
            }
        }

        private void ToggleAutopilot()
        {
            _isAutopilotActive = !_isAutopilotActive;
            if (autopilotBtn != null)
            {
                var textComponent = autopilotBtn.GetComponentInChildren<Text>();
                if (textComponent != null)
                {
                    textComponent.text = _isAutopilotActive ? "🤖 Autopilot: ON" : "🤖 Autopilot: OFF";
                }
            }
            Debug.Log($"[MobileUI] Autopilot toggled: {_isAutopilotActive}");
        }
    }
}
