using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;
using FRTE.Effects;

namespace FRTE.Samples
{
    /// <summary>
    /// Sample UI demonstrating the 4-step integration flow of the FRTE SDK:
    /// Photo (Load) -> Touch (Deform) -> Material (Swap) -> Save (Export).
    /// </summary>
    public sealed class FRTESampleUI : MonoBehaviour
    {
        [Header("Scene References")]
        [Tooltip("The deformable mesh renderer component in the scene.")]
        [SerializeField] private DeformableMeshRenderer deformableMesh;

        [Tooltip("The camera shaker component in the scene.")]
        [SerializeField] private CameraShaker cameraShaker;

        [Tooltip("The ripple controller component attached to the mesh.")]
        [SerializeField] private RippleController rippleController;

        [Header("Demo UI Elements")]
        [SerializeField] private Button loadButton;
        [SerializeField] private Button materialButton;
        [SerializeField] private Button saveButton;
        [SerializeField] private Text materialText;

        private Texture2D _sampleTexture;
        private int _currentMaterialIndex = 0;

        private void Start()
        {
            // 1. Initialize SDK
            FRTESdkManager.Instance.InitializeSDK();

            // 2. Set up Deformable Mesh with Physics Engine resolved from Container
            if (deformableMesh != null && FRTESdkManager.Instance.Container.TryResolve<ISquishyPhysicsEngine>(out var physics))
            {
                deformableMesh.Setup(physics);
            }

            // 3. Create a dummy sample texture (Rainbow grid)
            _sampleTexture = new Texture2D(128, 128, TextureFormat.RGBA32, false);
            for (int y = 0; y < 128; y++)
            {
                for (int x = 0; x < 128; x++)
                {
                    float r = (float)x / 127f;
                    float g = (float)y / 127f;
                    _sampleTexture.SetPixel(x, y, new Color(r, g, 0.6f, 1.0f));
                }
            }
            _sampleTexture.Apply();

            // 4. Bind UI actions
            if (loadButton != null) loadButton.onClick.AddListener(OnLoadPressed);
            if (materialButton != null) materialButton.onClick.AddListener(OnMaterialPressed);
            if (saveButton != null) saveButton.onClick.AddListener(OnSavePressed);

            UpdateMaterialLabel();
        }

        private void OnLoadPressed()
        {
            // Step 1: Photo Loading via SDK Photo Engine
            if (FRTESdkManager.Instance.Container.TryResolve<IPhotoEngine>(out var photoEngine))
            {
                photoEngine.LoadPhoto(_sampleTexture);
                Debug.Log("[FRTE Sample] Sample photo loaded into PhotoEngine.");
            }
        }

        private void OnMaterialPressed()
        {
            // Step 3: Material Configuration Hot-Swapping
            if (FRTESdkManager.Instance.Container.TryResolve<ISquishyPhysicsEngine>(out var physics))
            {
                _currentMaterialIndex = (_currentMaterialIndex + 1) % 4;
                switch (_currentMaterialIndex)
                {
                    case 0:
                        physics.MaterialConfig = FRTEMaterialConfig.CreateJelly();
                        break;
                    case 1:
                        physics.MaterialConfig = FRTEMaterialConfig.CreateSlime();
                        break;
                    case 2:
                        physics.MaterialConfig = FRTEMaterialConfig.CreatePudding();
                        break;
                    case 3:
                        physics.MaterialConfig = FRTEMaterialConfig.CreateMochi();
                        break;
                }
                UpdateMaterialLabel();
            }
        }

        private void UpdateMaterialLabel()
        {
            if (materialText == null) return;
            switch (_currentMaterialIndex)
            {
                case 0: materialText.text = "Material: Jelly"; break;
                case 1: materialText.text = "Material: Slime"; break;
                case 2: materialText.text = "Material: Pudding"; break;
                case 3: materialText.text = "Material: Mochi"; break;
            }
        }

        private async void OnSavePressed()
        {
            // Step 4: Asynchronous Export (PNG)
            if (FRTESdkManager.Instance.Container.TryResolve<IPhotoEngine>(out var photo) &&
                FRTESdkManager.Instance.Container.TryResolve<IExportEngine>(out var export))
            {
                string path = System.IO.Path.Combine(Application.persistentDataPath, "FruitRabbit_Export.png");
                
                // Disable UI interactions during export
                SetUIInteractable(false);
                
                try
                {
                    // Asynchronously exports the deformed GPU WorkingTexture
                    await export.ExportPNGAsync(photo.WorkingTexture, path);
                    Debug.Log($"[FRTE Sample] Image successfully saved to: {path}");
                }
                catch (System.Exception ex)
                {
                    Debug.LogError($"[FRTE Sample] Export failed: {ex.Message}");
                }
                finally
                {
                    SetUIInteractable(true);
                }
            }
        }

        private void SetUIInteractable(bool interactable)
        {
            if (loadButton != null) loadButton.interactable = interactable;
            if (materialButton != null) materialButton.interactable = interactable;
            if (saveButton != null) saveButton.interactable = interactable;
        }

        private void Update()
        {
            // Step 2: Touch / Mouse Interaction mapping
            if (Input.GetMouseButtonDown(0) || Input.GetMouseButton(0) || Input.GetMouseButtonUp(0))
            {
                // Raycast against the deformable mesh to find touch UV coordinates
                Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
                if (Physics.Raycast(ray, out RaycastHit hit))
                {
                    if (hit.collider.gameObject == deformableMesh.gameObject)
                    {
                        Vector2 touchUV = hit.textureCoord;

                        TouchPhase phase = TouchPhase.Stationary;
                        if (Input.GetMouseButtonDown(0))
                        {
                            phase = TouchPhase.Began;
                            // Trigger ripple refraction on touch down
                            if (rippleController != null)
                            {
                                rippleController.TriggerRipple(touchUV, 0.06f);
                            }
                            // Trigger camera shake on touch down peak
                            if (cameraShaker != null)
                            {
                                cameraShaker.TriggerShake(0.8f, Vector3.one);
                            }
                        }
                        else if (Input.GetMouseButtonUp(0))
                        {
                            phase = TouchPhase.Ended;
                        }
                        else
                        {
                            phase = TouchPhase.Moved;
                        }

                        // Feed touch event into the SDK coordinator
                        FRTESdkManager.Instance.SetTouchInput(0, touchUV, phase, pressure: 1.0f);
                    }
                }
            }
        }

        private void OnDestroy()
        {
            if (_sampleTexture != null)
            {
                DestroyImmediate(_sampleTexture);
            }
        }
    }
}
