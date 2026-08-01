using UnityEngine;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// ScriptableObject defining metadata and layer textures for a single PhotoZone.
    /// </summary>
    [CreateAssetMenu(fileName = "PhotoZonePreset", menuName = "FRTE/Photo Zone/Preset")]
    public sealed class PhotoZonePreset : ScriptableObject
    {
        [SerializeField] private string id;
        [SerializeField] private string displayNameKey;
        [SerializeField] private string descriptionKey;

        [SerializeField] private Sprite background;
        [SerializeField] private Sprite midground;
        [SerializeField] private Sprite foreground;
        [SerializeField] private Sprite lightingOverlay;
        [SerializeField] private Sprite frame;
        [SerializeField] private Sprite thumbnail;

        [SerializeField] private PhotoZoneCharacterSlot[] characterSlots;
        [SerializeField] private PhotoZoneDecorationSlot[] decorationSlots;

        [SerializeField] private bool unlockedByDefault = true;
        [SerializeField] private int sortOrder = 0;

        public string Id => id;
        public string DisplayNameKey => displayNameKey;
        public string DescriptionKey => descriptionKey;

        public Sprite Background => background;
        public Sprite Midground => midground;
        public Sprite Foreground => foreground;
        public Sprite LightingOverlay => lightingOverlay;
        public Sprite Frame => frame;
        public Sprite Thumbnail => thumbnail;

        public PhotoZoneCharacterSlot[] CharacterSlots => characterSlots;
        public PhotoZoneDecorationSlot[] DecorationSlots => decorationSlots;

        public bool UnlockedByDefault => unlockedByDefault;
        public int SortOrder => sortOrder;

        public void SetTestValues(string presetId, string nameKey, int order = 0)
        {
            id = presetId;
            displayNameKey = nameKey;
            sortOrder = order;
            unlockedByDefault = true;
            characterSlots = new PhotoZoneCharacterSlot[0];
            decorationSlots = new PhotoZoneDecorationSlot[0];
        }
    }
}
