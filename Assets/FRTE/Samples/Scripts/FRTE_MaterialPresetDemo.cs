using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;
using FRTE.Physics;

namespace FRTE.Materials.Samples
{
    /// <summary>
    /// Procedural demo coordinator for the Materials & Presets system.
    /// Sets up cameras, surfaces, category tabs, scrolling lists, and configuration settings
    /// without requiring any scene file dependencies.
    /// </summary>
    public sealed class FRTE_MaterialPresetDemo : MonoBehaviour
    {
        private SquishySurface _squishySurface;
        private DeformableJellyRenderer _jellyRenderer;
        private Texture2D _testTexture;
        private Camera _mainCamera;

        // UI references
        private GameObject _canvasGo;
        private Text _presetNameText;
        private Text _presetDescText;
        private Transform _scrollContent;

        private IMaterialPresetController _controller;
        private IMaterialPresetProvider _provider;

        private MaterialCategory _activeCategory = MaterialCategory.Basic;
        private readonly List<GameObject> _slotsList = new List<GameObject>();

        private void Start()
        {
            // 1. Setup Camera
            SetupCamera();

            // 2. Setup Test Texture
            CreateTestTexture();

            // 3. Setup Surface and Jelly Renderer
            CreateDeformableObject();

            // 4. Resolve bootstrapped controllers
            var container = FRTESdkManager.Instance.Container;
            if (container.TryResolve<IMaterialPresetController>(out _controller))
            {
                var presetCtrl = _controller as MaterialPresetController;
                if (presetCtrl != null)
                {
                    presetCtrl.BindRenderers(_squishySurface, _jellyRenderer);
                }
            }
            container.TryResolve<IMaterialPresetProvider>(out _provider);

            // 5. Build procedural UI layouts
            CreateProceduralUI();

            // 6. Hook material selection panel update
            FRTESdkManager.Instance.EventBus.Subscribe<MaterialPresetChangedEvent>(OnMaterialChanged);

            // Render first preset list
            RenderList();
            UpdateLabels();
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
            _mainCamera.backgroundColor = new Color(0.15f, 0.15f, 0.18f, 1f);
        }

        private void CreateTestTexture()
        {
            _testTexture = new Texture2D(128, 128, TextureFormat.RGBA32, false);
            for (int y = 0; y < 128; y++)
            {
                for (int x = 0; x < 128; x++)
                {
                    float r = (float)x / 127f;
                    float g = (float)y / 127f;
                    _testTexture.SetPixel(x, y, new Color(r, g, 0.6f, 1f));
                }
            }
            _testTexture.Apply();
        }

        private void CreateDeformableObject()
        {
            var surfaceGo = new GameObject("DeformableSurface");
            _squishySurface = surfaceGo.AddComponent<SquishySurface>();
            _jellyRenderer = surfaceGo.AddComponent<DeformableJellyRenderer>();

            // Setup Material
            var renderer = surfaceGo.GetComponent<MeshRenderer>();
            renderer.sharedMaterial = new Material(Shader.Find("Sprites/Default"));

            // Add Debug panel for monitor tuning
            surfaceGo.AddComponent<SquishyDebugPanel>();

            var containerGo = new GameObject("Container");
            var containerRect = containerGo.AddComponent<RectTransform>();
            containerRect.sizeDelta = new Vector2(350f, 350f);

            var collider = surfaceGo.AddComponent<BoxCollider>();
            collider.size = new Vector3(4.5f, 4.5f, 0.1f);

            var input = new SquishySurfaceInput
            {
                SourceTexture = _testTexture,
                Width = 4.5f,
                Height = 4.5f,
                Quality = SquishyMeshQuality.Medium,
                TargetCamera = _mainCamera,
                ContainerRect = containerRect
            };
            _squishySurface.Initialize(input);
        }

        private void CreateProceduralUI()
        {
            _canvasGo = new GameObject("PresetDemo_Canvas");
            var canvas = _canvasGo.AddComponent<Canvas>();
            canvas.renderMode = RenderMode.ScreenSpaceOverlay;
            _canvasGo.AddComponent<CanvasScaler>();
            _canvasGo.AddComponent<GraphicRaycaster>();

            // 1. Bottom Selection Panel background
            var panelGo = new GameObject("Panel_Bottom");
            panelGo.transform.SetParent(_canvasGo.transform, false);
            var panelImg = panelGo.AddComponent<Image>();
            panelImg.color = new Color(0.08f, 0.08f, 0.1f, 0.95f);
            var panelRect = panelGo.GetComponent<RectTransform>();
            panelRect.anchorMin = new Vector2(0f, 0f);
            panelRect.anchorMax = new Vector2(1f, 0f);
            panelRect.anchoredPosition = new Vector2(0f, 130f);
            panelRect.sizeDelta = new Vector2(0f, 220f);

            // Category Tab Buttons: Basic & Fruit
            CreateButton(panelGo.transform, new Vector2(-120f, 90f), new Vector2(100f, 30f), "Basic Tab", () => SetActiveCategory(MaterialCategory.Basic));
            CreateButton(panelGo.transform, new Vector2(0f, 90f), new Vector2(100f, 30f), "Fruit Tab", () => SetActiveCategory(MaterialCategory.Fruit));
            CreateButton(panelGo.transform, new Vector2(120f, 90f), new Vector2(100f, 30f), "Reset", ResetDemoSurface);

            // Descriptions Texts
            var nameGo = new GameObject("Txt_Name");
            nameGo.transform.SetParent(panelGo.transform, false);
            _presetNameText = nameGo.AddComponent<Text>();
            _presetNameText.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            _presetNameText.fontSize = 20;
            _presetNameText.fontStyle = FontStyle.Bold;
            _presetNameText.color = Color.yellow;
            _presetNameText.alignment = TextAnchor.MiddleCenter;
            var nameRect = nameGo.GetComponent<RectTransform>();
            nameRect.anchoredPosition = new Vector2(0f, 50f);
            nameRect.sizeDelta = new Vector2(500f, 30f);

            var descGo = new GameObject("Txt_Desc");
            descGo.transform.SetParent(panelGo.transform, false);
            _presetDescText = descGo.AddComponent<Text>();
            _presetDescText.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            _presetDescText.fontSize = 15;
            _presetDescText.color = Color.white;
            _presetDescText.alignment = TextAnchor.MiddleCenter;
            var descRect = descGo.GetComponent<RectTransform>();
            descRect.anchoredPosition = new Vector2(0f, 20f);
            descRect.sizeDelta = new Vector2(500f, 30f);

            // Horizontal ScrollView viewport
            var scrollGo = new GameObject("ScrollArea");
            scrollGo.transform.SetParent(panelGo.transform, false);
            var scrollRect = scrollGo.AddComponent<ScrollRect>();
            scrollRect.vertical = false;
            scrollRect.horizontal = true;
            var scrollRectTrans = scrollGo.GetComponent<RectTransform>();
            scrollRectTrans.anchoredPosition = new Vector2(0f, -40f);
            scrollRectTrans.sizeDelta = new Vector2(550f, 80f);

            var viewGo = new GameObject("Viewport");
            viewGo.transform.SetParent(scrollGo.transform, false);
            var viewRect = viewGo.AddComponent<RectTransform>();
            viewRect.anchorMin = Vector2.zero;
            viewRect.anchorMax = Vector2.one;
            viewRect.offsetMin = Vector2.zero;
            viewRect.offsetMax = Vector2.zero;
            viewGo.AddComponent<Image>().color = new Color(0.15f, 0.15f, 0.15f, 0.5f);
            viewGo.AddComponent<Mask>();

            var contentGo = new GameObject("Content");
            contentGo.transform.SetParent(viewGo.transform, false);
            _scrollContent = contentGo.AddComponent<RectTransform>();
            _scrollContent.anchorMin = new Vector2(0f, 0f);
            _scrollContent.anchorMax = new Vector2(0f, 1f);
            _scrollContent.anchoredPosition = Vector2.zero;
            _scrollContent.sizeDelta = new Vector2(800f, 0f);

            var glg = contentGo.AddComponent<GridLayoutGroup>();
            glg.cellSize = new Vector2(90f, 65f);
            glg.spacing = new Vector2(10f, 0f);
            glg.startAxis = GridLayoutGroup.Axis.Horizontal;
            glg.constraint = GridLayoutGroup.Constraint.FixedRowCount;
            glg.constraintCount = 1;

            scrollRect.content = _scrollContent;
            scrollRect.viewport = viewRect;
        }

        private void CreateButton(Transform parent, Vector2 pos, Vector2 size, string textLabel, UnityEngine.Events.UnityAction action)
        {
            var btnGo = new GameObject("Btn_" + textLabel);
            btnGo.transform.SetParent(parent, false);
            var btn = btnGo.AddComponent<Button>();
            var img = btnGo.AddComponent<Image>();
            img.color = new Color(0.25f, 0.25f, 0.28f, 1f);

            var rect = btnGo.GetComponent<RectTransform>();
            rect.anchoredPosition = pos;
            rect.sizeDelta = size;

            var txtGo = new GameObject("Text");
            txtGo.transform.SetParent(btnGo.transform, false);
            var text = txtGo.AddComponent<Text>();
            text.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            text.text = textLabel;
            text.fontSize = 14;
            text.alignment = TextAnchor.MiddleCenter;
            text.color = Color.white;

            var tRect = txtGo.GetComponent<RectTransform>();
            tRect.anchorMin = Vector2.zero;
            tRect.anchorMax = Vector2.one;
            tRect.offsetMin = Vector2.zero;
            tRect.offsetMax = Vector2.zero;

            btn.onClick.AddListener(action);
        }

        private void SetActiveCategory(MaterialCategory category)
        {
            _activeCategory = category;
            RenderList();
        }

        private void RenderList()
        {
            // Clear cells
            for (int i = 0; i < _slotsList.Count; i++)
            {
                Destroy(_slotsList[i]);
            }
            _slotsList.Clear();

            if (_provider == null || _scrollContent == null) return;

            var list = _provider.GetAll();
            for (int i = 0; i < list.Count; i++)
            {
                var preset = list[i];
                if (preset.Category != _activeCategory) continue;

                var slotGo = new GameObject("Slot_" + preset.Id);
                slotGo.transform.SetParent(_scrollContent, false);
                var img = slotGo.AddComponent<Image>();
                
                // Highlight active selection
                bool isSelected = (_controller != null && _controller.CurrentPreset != null && _controller.CurrentPreset.Id == preset.Id);
                img.color = isSelected ? new Color(1f, 0.85f, 0f, 1f) : new Color(0.2f, 0.2f, 0.2f, 1f);

                var txtGo = new GameObject("Text");
                txtGo.transform.SetParent(slotGo.transform, false);
                var text = txtGo.AddComponent<Text>();
                text.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
                text.text = preset.DisplayName;
                text.fontSize = 13;
                text.alignment = TextAnchor.MiddleCenter;
                text.color = Color.white;
                var tRect = txtGo.GetComponent<RectTransform>();
                tRect.anchorMin = Vector2.zero;
                tRect.anchorMax = Vector2.one;
                tRect.offsetMin = Vector2.zero;
                tRect.offsetMax = Vector2.zero;

                var btn = slotGo.AddComponent<Button>();
                string pid = preset.Id;
                btn.onClick.AddListener(() => SelectPreset(pid));

                _slotsList.Add(slotGo);
            }
        }

        private void SelectPreset(string id)
        {
            if (_controller != null)
            {
                _controller.ApplyPreset(id);
            }
        }

        private void ResetDemoSurface()
        {
            if (_squishySurface != null)
            {
                _squishySurface.ResetSurface();
            }
        }

        private void OnMaterialChanged(MaterialPresetChangedEvent evt)
        {
            UpdateLabels();
            RenderList();
        }

        private void UpdateLabels()
        {
            if (_controller == null || _controller.CurrentPreset == null) return;

            _presetNameText.text = _controller.CurrentPreset.DisplayName;
            _presetDescText.text = _controller.CurrentPreset.Description;
        }

        private void OnDestroy()
        {
            var sdk = FRTESdkManager.Instance;
            if (sdk != null && sdk.EventBus != null)
            {
                sdk.EventBus.Unsubscribe<MaterialPresetChangedEvent>(OnMaterialChanged);
            }
            if (_testTexture != null) DestroyImmediate(_testTexture);
            if (_canvasGo != null) DestroyImmediate(_canvasGo);
        }
    }
}
