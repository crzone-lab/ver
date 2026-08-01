using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;

namespace FRTE.Physics.Samples
{
    /// <summary>
    /// Procedural demo coordinator for the Squishy Physics Engine.
    /// Sets up the canvas, buttons, camera, and links the Photo Engine with the Physics Engine.
    /// Enables testing "Photo Edit Mode" and "Squishy Play Mode" without any manual scene setup.
    /// </summary>
    public sealed class FRTE_SquishyPhysicsDemo : MonoBehaviour
    {
        private enum AppMode
        {
            PhotoEdit,
            SquishyPlay
        }

        private AppMode _currentMode = AppMode.PhotoEdit;
        private SquishySurface _squishySurface;
        private Texture2D _testTexture;
        private Camera _mainCamera;

        // UI References
        private GameObject _canvasGo;
        private Text _modeText;
        private Text _qualityText;

        // Photo transformation state (Edit Mode)
        private Vector3 _photoPosition = Vector3.zero;
        private float _photoScale = 1.0f;
        private float _photoRotation = 0f;

        private void Start()
        {
            // 1. Setup Camera and Lighting
            SetupCamera();

            // 2. Load/Create Test image (Rainbow texture)
            CreateTestTexture();

            // 3. Create Canvas UI procedurally
            CreateDemoUI();

            // 4. Create the Deformable Object
            CreateDeformableObject();

            // 5. Apply initial mode states
            SetMode(AppMode.PhotoEdit);
        }

        private void SetupCamera()
        {
            _mainCamera = Camera.main;
            if (_mainCamera == null)
            {
                var camGo = new GameObject("Main Camera");
                _mainCamera = camGo.AddComponent<Camera>();
                _mainCamera.tag = "MainCamera";
                camGo.transform.position = new Vector3(0f, 0f, -10f);
            }
            _mainCamera.orthographic = true;
            _mainCamera.orthographicSize = 5f;

            // Add lighting
            var lightGo = new GameObject("Directional Light");
            var light = lightGo.AddComponent<Light>();
            light.type = LightType.Directional;
            lightGo.transform.rotation = Quaternion.Euler(50f, -30f, 0f);
        }

        private void CreateTestTexture()
        {
            _testTexture = new Texture2D(256, 256, TextureFormat.RGBA32, false);
            for (int y = 0; y < 256; y++)
            {
                for (int x = 0; x < 256; x++)
                {
                    float r = (float)x / 255f;
                    float g = (float)y / 255f;
                    _testTexture.SetPixel(x, y, new Color(r, g, 0.5f, 1.0f));
                }
            }
            _testTexture.Apply();
        }

        private void CreateDeformableObject()
        {
            var surfaceGo = new GameObject("SquishySurface_Instance");
            _squishySurface = surfaceGo.AddComponent<SquishySurface>();

            // Setup Material
            var renderer = surfaceGo.GetComponent<MeshRenderer>();
            renderer.sharedMaterial = new Material(Shader.Find("Sprites/Default"));

            // Attach Debug Panel to the surface
            var debugPanel = surfaceGo.AddComponent<SquishyDebugPanel>();

            // Create Container RectTransform mapping
            var containerGo = new GameObject("Surface_UI_Container");
            var containerRect = containerGo.AddComponent<RectTransform>();
            containerRect.sizeDelta = new Vector2(300f, 300f);

            // Set up collision for Raycast mapping
            var collider = surfaceGo.AddComponent<BoxCollider>();
            collider.size = new Vector3(4f, 4f, 0.1f);

            // Initialize Surface (Medium quality)
            var input = new SquishySurfaceInput
            {
                SourceTexture = _testTexture,
                Width = 4f,
                Height = 4f,
                Quality = SquishyMeshQuality.Medium,
                TargetCamera = _mainCamera,
                ContainerRect = containerRect
            };
            _squishySurface.Initialize(input);
        }

        private void CreateDemoUI()
        {
            _canvasGo = new GameObject("Demo_Canvas");
            var canvas = _canvasGo.AddComponent<Canvas>();
            canvas.renderMode = RenderMode.ScreenSpaceOverlay;
            _canvasGo.AddComponent<CanvasScaler>();
            _canvasGo.AddComponent<GraphicRaycaster>();

            // Main Background Panel
            var panelGo = new GameObject("ControlPanel");
            panelGo.transform.SetParent(_canvasGo.transform, false);
            var panelImg = panelGo.AddComponent<Image>();
            panelImg.color = new Color(0.1f, 0.1f, 0.1f, 0.85f);
            var panelRect = panelGo.GetComponent<RectTransform>();
            panelRect.anchorMin = new Vector2(0.5f, 0f);
            panelRect.anchorMax = new Vector2(0.5f, 0f);
            panelRect.anchoredPosition = new Vector2(0f, 60f);
            panelRect.sizeDelta = new Vector2(600f, 90f);

            // Mode Label
            var modeLabelGo = new GameObject("ModeLabel");
            modeLabelGo.transform.SetParent(panelGo.transform, false);
            _modeText = modeLabelGo.AddComponent<Text>();
            _modeText.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            _modeText.fontSize = 18;
            _modeText.alignment = TextAnchor.MiddleCenter;
            _modeText.color = Color.white;
            var labelRect = modeLabelGo.GetComponent<RectTransform>();
            labelRect.anchoredPosition = new Vector2(0f, 30f);
            labelRect.sizeDelta = new Vector2(400f, 30f);

            // --- BUTTONS ---
            CreateButton(panelGo.transform, new Vector2(-220f, -15f), "Toggle Mode", ToggleAppMode);
            CreateButton(panelGo.transform, new Vector2(-90f, -15f), "Reset Surface", ResetSurface);
            CreateButton(panelGo.transform, new Vector2(40f, -15f), "Cycle Quality", CycleMeshQuality);
            CreateButton(panelGo.transform, new Vector2(170f, -15f), "Transform +/-", CyclePhotoTransforms);
        }

        private void CreateButton(Transform parent, Vector2 pos, string labelText, UnityEngine.Events.UnityAction action)
        {
            var btnGo = new GameObject("Btn_" + labelText);
            btnGo.transform.SetParent(parent, false);
            var btn = btnGo.AddComponent<Button>();
            var img = btnGo.AddComponent<Image>();
            img.color = new Color(0.3f, 0.3f, 0.3f, 1f);

            var rect = btnGo.GetComponent<RectTransform>();
            rect.anchoredPosition = pos;
            rect.sizeDelta = new Vector2(110f, 35f);

            var textGo = new GameObject("Text");
            textGo.transform.SetParent(btnGo.transform, false);
            var text = textGo.AddComponent<Text>();
            text.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            text.text = labelText;
            text.fontSize = 13;
            text.alignment = TextAnchor.MiddleCenter;
            text.color = Color.white;
            var txtRect = textGo.GetComponent<RectTransform>();
            txtRect.sizeDelta = rect.sizeDelta;

            btn.onClick.AddListener(action);
        }

        private void ToggleAppMode()
        {
            _currentMode = (_currentMode == AppMode.PhotoEdit) ? AppMode.SquishyPlay : AppMode.PhotoEdit;
            SetMode(_currentMode);
        }

        private void SetMode(AppMode mode)
        {
            _currentMode = mode;
            if (_modeText != null)
            {
                _modeText.text = $"Current Mode: <color=yellow>{_currentMode}</color>";
            }

            if (_squishySurface != null)
            {
                // In Edit Mode, we disable the physics simulation to prevent conflict with photo translation
                _squishySurface.enabled = (_currentMode == AppMode.SquishyPlay);
                if (_currentMode == AppMode.PhotoEdit)
                {
                    _squishySurface.ResetSurface();
                }
            }
        }

        private void ResetSurface()
        {
            if (_squishySurface != null)
            {
                _squishySurface.ResetSurface();
            }
            _photoPosition = Vector3.zero;
            _photoScale = 1.0f;
            _photoRotation = 0f;
            ApplyTransformsToMesh();
        }

        private void CycleMeshQuality()
        {
            if (_squishySurface == null) return;

            var newQuality = SquishyMeshQuality.Medium;
            if (_quality == SquishyMeshQuality.Low) newQuality = SquishyMeshQuality.Medium;
            else if (_quality == SquishyMeshQuality.Medium) newQuality = SquishyMeshQuality.High;
            else newQuality = SquishyMeshQuality.Low;

            _quality = newQuality;

            // Rebuild with new mesh resolution quality
            var input = new SquishySurfaceInput
            {
                SourceTexture = _testTexture,
                Width = 4f,
                Height = 4f,
                Quality = _quality,
                TargetCamera = _mainCamera,
                ContainerRect = _squishySurface.GetComponent<SquishyDebugPanel>().GetComponent<RectTransform>() // uses container
            };
            _squishySurface.RebuildSurface(input);
            SetMode(_currentMode); // restore state
        }

        private SquishyMeshQuality _quality = SquishyMeshQuality.Medium;

        private void CyclePhotoTransforms()
        {
            if (_currentMode != AppMode.PhotoEdit)
            {
                Debug.LogWarning("[Demo] Photo transformations can only be run in Photo Edit Mode.");
                return;
            }

            // Cycle through scale/rotation transformations
            _photoScale = (_photoScale >= 1.5f) ? 0.75f : _photoScale + 0.25f;
            _photoRotation = (_photoRotation >= 270f) ? 0f : _photoRotation + 90f;
            _photoPosition = new Vector3(Mathf.Sin(Time.time) * 0.5f, 0f, 0f);

            ApplyTransformsToMesh();
        }

        private void ApplyTransformsToMesh()
        {
            if (_squishySurface != null)
            {
                _squishySurface.transform.localPosition = _photoPosition;
                _squishySurface.transform.localScale = Vector3.one * _photoScale;
                _squishySurface.transform.localRotation = Quaternion.Euler(0f, 0f, _photoRotation);
            }
        }

        private void OnDestroy()
        {
            if (_testTexture != null)
            {
                DestroyImmediate(_testTexture);
            }
            if (_canvasGo != null)
            {
                DestroyImmediate(_canvasGo);
            }
        }
    }
}
