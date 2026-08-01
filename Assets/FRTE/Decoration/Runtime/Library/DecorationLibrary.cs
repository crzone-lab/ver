using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// ScriptableObject database containing all registered decoration presets.
    /// Dynamically constructs 30 placeholder presets if empty to ensure zero-setup testing.
    /// </summary>
    [CreateAssetMenu(fileName = "DecorationLibrary", menuName = "FRTE/Decoration/Library")]
    public sealed class DecorationLibrary : ScriptableObject, IDecorationPresetProvider
    {
        [SerializeField] private List<DecorationPreset> presets = new List<DecorationPreset>();

        private readonly Dictionary<string, DecorationPreset> _cache = new Dictionary<string, DecorationPreset>();
        private readonly Dictionary<DecorationCategory, List<DecorationPreset>> _categoryCache = new Dictionary<DecorationCategory, List<DecorationPreset>>();
        private bool _isInitialized;

        private void OnEnable()
        {
            InitializeLibrary();
        }

        public void InitializeLibrary()
        {
            _cache.Clear();
            _categoryCache.Clear();

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

                    if (!_categoryCache.TryGetValue(preset.Category, out var list))
                    {
                        list = new List<DecorationPreset>();
                        _categoryCache.Add(preset.Category, list);
                    }
                    list.Add(preset);
                }
            }

            _isInitialized = true;
        }

        public IReadOnlyList<DecorationPreset> GetAll()
        {
            if (!_isInitialized) InitializeLibrary();
            return presets;
        }

        public IReadOnlyList<DecorationPreset> GetByCategory(DecorationCategory category)
        {
            if (!_isInitialized) InitializeLibrary();
            if (_categoryCache.TryGetValue(category, out var list))
            {
                return list;
            }
            return System.Array.Empty<DecorationPreset>();
        }

        public bool TryGetById(string id, out DecorationPreset preset)
        {
            if (!_isInitialized) InitializeLibrary();
            if (string.IsNullOrEmpty(id))
            {
                preset = null;
                return false;
            }
            return _cache.TryGetValue(id, out preset);
        }

        private List<DecorationPreset> CreateFallbackPresets()
        {
            var list = new List<DecorationPreset>();

            // --- Category 1: FruitRabbitEars (6) ---
            list.Add(CreatePreset("ear.strawberry", "Strawberry Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));
            list.Add(CreatePreset("ear.lemon", "Lemon Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));
            list.Add(CreatePreset("ear.peach", "Peach Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));
            list.Add(CreatePreset("ear.watermelon", "Watermelon Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));
            list.Add(CreatePreset("ear.kiwi", "Kiwi Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));
            list.Add(CreatePreset("ear.grape", "Grape Ears", DecorationCategory.FruitRabbitEars, DecorationAnchorType.HeadTop));

            // --- Category 2: FruitHat (6) ---
            list.Add(CreatePreset("hat.strawberry", "Strawberry Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("hat.lemon", "Lemon Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("hat.peach", "Peach Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("hat.watermelon", "Watermelon Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("hat.kiwi", "Kiwi Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("hat.grape", "Grape Hat", DecorationCategory.FruitHat, DecorationAnchorType.Forehead));

            // --- Category 3: Glasses (3) ---
            list.Add(CreatePreset("glass.round", "Round Glasses", DecorationCategory.Glasses, DecorationAnchorType.EyesCenter));
            list.Add(CreatePreset("glass.heart", "Heart Glasses", DecorationCategory.Glasses, DecorationAnchorType.EyesCenter));
            list.Add(CreatePreset("glass.star", "Star Glasses", DecorationCategory.Glasses, DecorationAnchorType.EyesCenter));

            // --- Category 4: FaceSticker (5) ---
            list.Add(CreatePreset("sticker.heart_blush", "Heart Blush", DecorationCategory.FaceSticker, DecorationAnchorType.LeftCheek));
            list.Add(CreatePreset("sticker.star_blush", "Star Blush", DecorationCategory.FaceSticker, DecorationAnchorType.RightCheek));
            list.Add(CreatePreset("sticker.fruit_slice", "Fruit Slice Sticker", DecorationCategory.FaceSticker, DecorationAnchorType.LeftCheek));
            list.Add(CreatePreset("sticker.sparkle", "Sparkle Sticker", DecorationCategory.FaceSticker, DecorationAnchorType.Forehead));
            list.Add(CreatePreset("sticker.cherry", "Cherry Sticker", DecorationCategory.FaceSticker, DecorationAnchorType.RightCheek));

            // --- Category 5: HandProp (3) ---
            list.Add(CreatePreset("prop.strawberry_juice", "Strawberry Juice", DecorationCategory.HandProp, DecorationAnchorType.Chin));
            list.Add(CreatePreset("prop.lemon_juice", "Lemon Juice", DecorationCategory.HandProp, DecorationAnchorType.Chin));
            list.Add(CreatePreset("prop.basket", "Fruit Basket", DecorationCategory.HandProp, DecorationAnchorType.Chin));

            // --- Category 6: Frame (3) ---
            list.Add(CreatePreset("frame.strawberry", "Strawberry Frame", DecorationCategory.Frame, DecorationAnchorType.Free));
            list.Add(CreatePreset("frame.lemon", "Lemon Frame", DecorationCategory.Frame, DecorationAnchorType.Free));
            list.Add(CreatePreset("frame.mix", "Fruit Mix Frame", DecorationCategory.Frame, DecorationAnchorType.Free));

            // --- Category 7: SpeechBubble (4) ---
            list.Add(CreatePreset("bubble.mochi", "말랑말랑!", DecorationCategory.SpeechBubble, DecorationAnchorType.Free));
            list.Add(CreatePreset("bubble.jelly", "탱글탱글!", DecorationCategory.SpeechBubble, DecorationAnchorType.Free));
            list.Add(CreatePreset("bubble.cute", "오늘도 귀여워!", DecorationCategory.SpeechBubble, DecorationAnchorType.Free));
            list.Add(CreatePreset("bubble.title", "FruitRabbit!", DecorationCategory.SpeechBubble, DecorationAnchorType.Free));

            return list;
        }

        private DecorationPreset CreatePreset(string id, string name, DecorationCategory category, DecorationAnchorType anchor)
        {
            var preset = ScriptableObject.CreateInstance<DecorationPreset>();
            preset.SetTestValues(id, name, category, anchor);
            return preset;
        }

        // Setter for testing
        public void SetTestPresets(List<DecorationPreset> testPresets)
        {
            presets = testPresets;
            InitializeLibrary();
        }
    }
}
