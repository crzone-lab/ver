using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// ScriptableObject defining metadata for a single decoration accessory.
    /// Exposes read-only properties via serialized fields.
    /// </summary>
    [CreateAssetMenu(fileName = "DecorationPreset", menuName = "FRTE/Decoration/Preset")]
    public sealed class DecorationPreset : ScriptableObject
    {
        [SerializeField] private string id;
        [SerializeField] private string displayNameKey;
        [SerializeField] private string descriptionKey;
        [SerializeField] private DecorationCategory category;
        [SerializeField] private Sprite sprite;
        [SerializeField] private Sprite thumbnail;
        [SerializeField] private DecorationAnchorType anchorType = DecorationAnchorType.Free;
        [SerializeField] private Vector2 defaultNormalizedPosition = Vector2.zero;
        [SerializeField] private Vector2 defaultScale = Vector2.one;
        [SerializeField] private float defaultRotation = 0f;
        [SerializeField] private int defaultSortingOrder = 10;
        [SerializeField] private bool allowFlip = true;
        [SerializeField] private bool allowDuplicate = true;
        [SerializeField] private bool unlockedByDefault = true;

        public string Id => id;
        public string DisplayNameKey => displayNameKey;
        public string DescriptionKey => descriptionKey;
        public DecorationCategory Category => category;
        public Sprite Sprite => sprite;
        public Sprite Thumbnail => thumbnail;
        public DecorationAnchorType AnchorType => anchorType;
        public Vector2 DefaultNormalizedPosition => defaultNormalizedPosition;
        public Vector2 DefaultScale => defaultScale;
        public float DefaultRotation => defaultRotation;
        public int DefaultSortingOrder => defaultSortingOrder;
        public bool AllowFlip => allowFlip;
        public bool AllowDuplicate => allowDuplicate;
        public bool UnlockedByDefault => unlockedByDefault;

        public void SetTestValues(
            string presetId,
            string nameKey,
            DecorationCategory cat,
            DecorationAnchorType anchor,
            Sprite testSprite = null)
        {
            id = presetId;
            displayNameKey = nameKey;
            category = cat;
            anchorType = anchor;
            sprite = testSprite;
            defaultScale = Vector2.one;
            unlockedByDefault = true;
            allowDuplicate = true;
        }
    }
}
