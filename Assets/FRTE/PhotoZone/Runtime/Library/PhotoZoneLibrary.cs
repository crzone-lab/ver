using System.Collections.Generic;
using UnityEngine;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// ScriptableObject database containing all registered PhotoZone presets.
    /// Dynamically constructs the 5 fallback presets (Strawberry, Lemon, Peach, Watermelon, Grape) if empty.
    /// </summary>
    [CreateAssetMenu(fileName = "PhotoZoneLibrary", menuName = "FRTE/Photo Zone/Library")]
    public sealed class PhotoZoneLibrary : ScriptableObject, IPhotoZoneProvider
    {
        [SerializeField] private List<PhotoZonePreset> presets = new List<PhotoZonePreset>();

        private readonly Dictionary<string, PhotoZonePreset> _cache = new Dictionary<string, PhotoZonePreset>();
        private readonly List<PhotoZonePreset> _sortedList = new List<PhotoZonePreset>();
        private bool _isInitialized;

        private void OnEnable()
        {
            InitializeLibrary();
        }

        public void InitializeLibrary()
        {
            _cache.Clear();
            _sortedList.Clear();

            if (presets == null || presets.Count == 0)
            {
                presets = CreateFallbackPresets();
            }

            for (int i = 0; i < presets.Count; i++)
            {
                var preset = presets[i];
                if (preset == null || string.IsNullOrEmpty(preset.Id)) continue;

                if (!_cache.ContainsKey(preset.Id))
                {
                    _cache.Add(preset.Id, preset);
                    _sortedList.Add(preset);
                }
            }

            _sortedList.Sort((a, b) => a.SortOrder.CompareTo(b.SortOrder));
            _isInitialized = true;
        }

        public IReadOnlyList<PhotoZonePreset> GetAll()
        {
            if (!_isInitialized) InitializeLibrary();
            return _sortedList;
        }

        public bool TryGetById(string id, out PhotoZonePreset preset)
        {
            if (!_isInitialized) InitializeLibrary();
            if (string.IsNullOrEmpty(id))
            {
                preset = null;
                return false;
            }
            return _cache.TryGetValue(id, out preset);
        }

        public PhotoZonePreset GetDefault()
        {
            if (!_isInitialized) InitializeLibrary();

            // Try to return Strawberry Farm as default
            if (TryGetById("photozone.strawberry_farm", out var preset))
            {
                return preset;
            }

            if (_sortedList.Count > 0)
            {
                return _sortedList[0];
            }

            return null;
        }

        private List<PhotoZonePreset> CreateFallbackPresets()
        {
            var list = new List<PhotoZonePreset>();

            list.Add(CreatePreset("photozone.strawberry_farm", "Strawberry Farm", 0));
            list.Add(CreatePreset("photozone.lemon_garden", "Lemon Garden", 1));
            list.Add(CreatePreset("photozone.peach_village", "Peach Village", 2));
            list.Add(CreatePreset("photozone.watermelon_beach", "Watermelon Beach", 3));
            list.Add(CreatePreset("photozone.grape_tunnel", "Grape Tunnel", 4));

            return list;
        }

        private PhotoZonePreset CreatePreset(string id, string name, int order)
        {
            var preset = ScriptableObject.CreateInstance<PhotoZonePreset>();
            preset.SetTestValues(id, name, order);
            return preset;
        }

        // Setter for testing
        public void SetTestPresets(List<PhotoZonePreset> testPresets)
        {
            presets = testPresets;
            InitializeLibrary();
        }
    }
}
