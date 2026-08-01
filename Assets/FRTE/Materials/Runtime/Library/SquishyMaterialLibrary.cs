using System.Collections.Generic;
using UnityEngine;

namespace FRTE.Materials
{
    /// <summary>
    /// ScriptableObject database containing all registered material presets.
    /// Exposes search, categorization, and validation.
    /// </summary>
    [CreateAssetMenu(fileName = "SquishyMaterialLibrary", menuName = "FRTE/Squishy/Material Library")]
    public sealed class SquishyMaterialLibrary : ScriptableObject, IMaterialPresetProvider
    {
        [SerializeField] private List<SquishyMaterialPreset> presets = new List<SquishyMaterialPreset>();

        private readonly Dictionary<string, SquishyMaterialPreset> _presetCache = new Dictionary<string, SquishyMaterialPreset>();
        private readonly List<SquishyMaterialPreset> _sortedPresets = new List<SquishyMaterialPreset>();
        private bool _isInitialized;

        private void OnEnable()
        {
            InitializeLibrary();
        }

        /// <summary>
        /// Validates and populates the lookup cache.
        /// </summary>
        public void InitializeLibrary()
        {
            _presetCache.Clear();
            _sortedPresets.Clear();

            if (presets == null || presets.Count == 0)
            {
                presets = SquishyMaterialPresetsFactory.CreateAllPresets();
            }

            for (int i = 0; i < presets.Count; i++)
            {
                var preset = presets[i];
                if (preset == null)
                {
                    Debug.LogWarning($"[MaterialLibrary] Null slot detected in preset index {i}.");
                    continue;
                }

                if (string.IsNullOrEmpty(preset.Id))
                {
                    Debug.LogWarning($"[MaterialLibrary] Preset in slot {i} has an empty ID.");
                    continue;
                }

                if (_presetCache.ContainsKey(preset.Id))
                {
                    Debug.LogError($"[MaterialLibrary] Duplicate preset ID detected: '{preset.Id}'. skipping...");
                    continue;
                }

                _presetCache.Add(preset.Id, preset);
                _sortedPresets.Add(preset);
            }

            // Sort presets by SortOrder
            _sortedPresets.Sort((a, b) => a.SortOrder.CompareTo(b.SortOrder));
            _isInitialized = true;
        }

        public IReadOnlyList<SquishyMaterialPreset> GetAll()
        {
            if (!_isInitialized) InitializeLibrary();
            return _sortedPresets;
        }

        public bool TryGetById(string id, out SquishyMaterialPreset preset)
        {
            if (!_isInitialized) InitializeLibrary();
            if (string.IsNullOrEmpty(id))
            {
                preset = null;
                return false;
            }
            return _presetCache.TryGetValue(id, out preset);
        }

        public SquishyMaterialPreset GetDefault()
        {
            if (!_isInitialized) InitializeLibrary();

            // Try to find Jelly as default
            if (TryGetById("basic.jelly", out var jelly))
            {
                return jelly;
            }

            // Fallback: return first sorted preset
            if (_sortedPresets.Count > 0)
            {
                return _sortedPresets[0];
            }

            return null;
        }

        // Custom setter for unit testing
        public void SetTestPresets(List<SquishyMaterialPreset> testPresets)
        {
            presets = testPresets;
            InitializeLibrary();
        }
    }
}
