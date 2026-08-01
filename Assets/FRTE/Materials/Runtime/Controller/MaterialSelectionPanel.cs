using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using FRTE.Core;

namespace FRTE.Materials
{
    /// <summary>
    /// UI Component managing category tabs, scrolling lists, selection highlights,
    /// and descriptions for the 12 material presets.
    /// </summary>
    public sealed class MaterialSelectionPanel : MonoBehaviour
    {
        [Header("Controller Bindings")]
        [SerializeField] private MaterialSelectionPanelUIReferences ui;

        private IMaterialPresetController _controller;
        private IMaterialPresetProvider _provider;

        private MaterialCategory _activeCategory = MaterialCategory.Basic;
        private readonly List<GameObject> _instantiatedSlots = new List<GameObject>();

        [System.Serializable]
        public struct MaterialSelectionPanelUIReferences
        {
            public Button basicTab;
            public Button fruitTab;
            public ScrollRect scrollRect;
            public RectTransform scrollContent;
            public GameObject slotPrefab; // optional fallback if null
            public Text selectedNameText;
            public Text selectedDescText;
        }

        private void Start()
        {
            // 1. Resolve core services
            var container = FRTESdkManager.Instance.Container;
            if (container.TryResolve<IMaterialPresetController>(out var ctrl))
            {
                _controller = ctrl;
            }
            if (container.TryResolve<IMaterialPresetProvider>(out var prov))
            {
                _provider = prov;
            }

            // 2. Bind tab listeners
            if (ui.basicTab != null) ui.basicTab.onClick.AddListener(() => SetCategory(MaterialCategory.Basic));
            if (ui.fruitTab != null) ui.fruitTab.onClick.AddListener(() => SetCategory(MaterialCategory.Fruit));

            // 3. Render initial list
            RenderPresetList();
            UpdateDescriptionLabels();

            // Listen to material preset changes
            FRTESdkManager.Instance.EventBus.Subscribe<MaterialPresetChangedEvent>(OnPresetChanged);
        }

        private void OnDestroy()
        {
            var sdk = FRTESdkManager.Instance;
            if (sdk != null && sdk.EventBus != null)
            {
                sdk.EventBus.Unsubscribe<MaterialPresetChangedEvent>(OnPresetChanged);
            }
        }

        private void SetCategory(MaterialCategory category)
        {
            _activeCategory = category;
            RenderPresetList();
        }

        private void RenderPresetList()
        {
            // Clear old slots
            for (int i = 0; i < _instantiatedSlots.Count; i++)
            {
                Destroy(_instantiatedSlots[i]);
            }
            _instantiatedSlots.Clear();

            if (_provider == null || ui.scrollContent == null) return;

            var allPresets = _provider.GetAll();
            for (int i = 0; i < allPresets.Count; i++)
            {
                var preset = allPresets[i];
                if (preset.Category != _activeCategory) continue;

                // Instantiate preset slot
                GameObject slotGo;
                if (ui.slotPrefab != null)
                {
                    slotGo = Instantiate(ui.slotPrefab, ui.scrollContent);
                }
                else
                {
                    // Procedural slot fallback
                    slotGo = CreateProceduralSlot(preset);
                }

                _instantiatedSlots.Add(slotGo);

                // Configure button action
                var btn = slotGo.GetComponent<Button>();
                if (btn == null) btn = slotGo.AddComponent<Button>();

                string pid = preset.Id;
                btn.onClick.AddListener(() => SelectPreset(pid));

                // Bind selection state visualization
                UpdateSlotSelectionVisual(slotGo, preset);
            }
        }

        private void SelectPreset(string presetId)
        {
            if (_controller != null)
            {
                _controller.ApplyPreset(presetId);
            }
        }

        private void OnPresetChanged(MaterialPresetChangedEvent evt)
        {
            UpdateDescriptionLabels();

            // Refresh slot highlights
            if (_provider != null)
            {
                var allPresets = _provider.GetAll();
                int slotIdx = 0;
                for (int i = 0; i < allPresets.Count; i++)
                {
                    var preset = allPresets[i];
                    if (preset.Category != _activeCategory) continue;

                    if (slotIdx < _instantiatedSlots.Count)
                    {
                        UpdateSlotSelectionVisual(_instantiatedSlots[slotIdx], preset);
                        slotIdx++;
                    }
                }
            }
        }

        private void UpdateDescriptionLabels()
        {
            if (_controller == null || _controller.CurrentPreset == null) return;

            var current = _controller.CurrentPreset;
            if (ui.selectedNameText != null)
            {
                ui.selectedNameText.text = current.DisplayName;
            }
            if (ui.selectedDescText != null)
            {
                ui.selectedDescText.text = current.Description;
            }
        }

        private void UpdateSlotSelectionVisual(GameObject slotGo, SquishyMaterialPreset preset)
        {
            if (_controller == null) return;

            bool isSelected = (_controller.CurrentPreset != null && _controller.CurrentPreset.Id == preset.Id);

            // Highlight border or background
            var img = slotGo.GetComponent<Image>();
            if (img != null)
            {
                img.color = isSelected ? new Color(1f, 0.85f, 0f, 1f) : new Color(0.2f, 0.2f, 0.2f, 1f);
            }
        }

        private GameObject CreateProceduralSlot(SquishyMaterialPreset preset)
        {
            var slotGo = new GameObject("Slot_" + preset.Id);
            slotGo.transform.SetParent(ui.scrollContent, false);

            var img = slotGo.AddComponent<Image>();
            img.color = new Color(0.2f, 0.2f, 0.2f, 1f);

            var layout = slotGo.AddComponent<LayoutElement>();
            layout.minWidth = 100f;
            layout.minHeight = 80f;

            // Name label inside cell
            var labelGo = new GameObject("Label");
            labelGo.transform.SetParent(slotGo.transform, false);
            var text = labelGo.AddComponent<Text>();
            text.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
            text.text = preset.DisplayName;
            text.fontSize = 14;
            text.alignment = TextAnchor.MiddleCenter;
            text.color = Color.white;

            var rect = labelGo.GetComponent<RectTransform>();
            rect.anchorMin = Vector2.zero;
            rect.anchorMax = Vector2.one;
            rect.offsetMin = Vector2.zero;
            rect.offsetMax = Vector2.zero;

            return slotGo;
        }
    }
}
