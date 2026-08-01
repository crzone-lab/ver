using UnityEngine;

namespace FRTE.Surprise
{
    /// <summary>
    /// ScriptableObject defining trigger criteria, visual effect payloads,
    /// and collection book properties for a single Surprise Event.
    /// </summary>
    [CreateAssetMenu(fileName = "SurpriseEventPreset", menuName = "FRTE/Surprise/Event Preset")]
    public sealed class SurpriseEventPreset : ScriptableObject
    {
        [SerializeField] private string id;
        [SerializeField] private string displayNameKey;
        [SerializeField] private string descriptionKey;

        [SerializeField] private SurpriseTriggerDefinition[] triggers;
        [SerializeField] private SurpriseEffectDefinition[] effects;

        [SerializeField] private float cooldownSeconds = 5f;
        [SerializeField] private float globalWeight = 1.0f;
        [SerializeField] private bool discoverable = true;
        [SerializeField] private bool unlockedByDefault = false;
        [SerializeField] private string relatedFruitId;
        [SerializeField] private Sprite collectionThumbnail;

        public string Id => id;
        public string DisplayNameKey => displayNameKey;
        public string DescriptionKey => descriptionKey;

        public SurpriseTriggerDefinition[] Triggers => triggers;
        public SurpriseEffectDefinition[] Effects => effects;

        public float CooldownSeconds => cooldownSeconds;
        public float GlobalWeight => globalWeight;
        public bool Discoverable => discoverable;
        public bool UnlockedByDefault => unlockedByDefault;
        public string RelatedFruitId => relatedFruitId;
        public Sprite CollectionThumbnail => collectionThumbnail;

        public void SetTestValues(
            string presetId,
            string nameKey,
            SurpriseTriggerDefinition[] triggerDefs,
            SurpriseEffectDefinition[] effectDefs,
            float cooldown = 5f,
            string fruitId = "")
        {
            id = presetId;
            displayNameKey = nameKey;
            triggers = triggerDefs;
            effects = effectDefs;
            cooldownSeconds = cooldown;
            relatedFruitId = fruitId;
            discoverable = true;
        }
    }
}
