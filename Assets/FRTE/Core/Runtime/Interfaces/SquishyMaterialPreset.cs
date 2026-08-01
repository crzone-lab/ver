using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// ScriptableObject defining a custom physical and visual material preset.
    /// Uses serialized private fields and read-only public properties.
    /// </summary>
    [CreateAssetMenu(fileName = "SquishyMaterialPreset", menuName = "FRTE/Squishy/Material Preset")]
    public sealed class SquishyMaterialPreset : ScriptableObject
    {
        [SerializeField] private string id;
        [SerializeField] private string displayName;
        [SerializeField] private string description;
        [SerializeField] private MaterialCategory category;
        [SerializeField] private Sprite icon;

        [SerializeField] private SquishyPhysicsParameters physics;
        [SerializeField] private SquishyVisualParameters visual;
        [SerializeField] private SquishyAudioParameters audio;
        [SerializeField] private SquishyHapticParameters haptic;

        [SerializeField] private bool isUnlockedByDefault = true;
        [SerializeField] private int sortOrder = 0;

        public string Id => id;
        public string DisplayName => displayName;
        public string Description => description;
        public MaterialCategory Category => category;
        public Sprite Icon => icon;

        public SquishyPhysicsParameters Physics => physics;
        public SquishyVisualParameters Visual => visual;
        public SquishyAudioParameters Audio => audio;
        public SquishyHapticParameters Haptic => haptic;

        public bool IsUnlockedByDefault => isUnlockedByDefault;
        public int SortOrder => sortOrder;

        public void SetTestValues(
            string presetId, 
            string name, 
            MaterialCategory cat,
            SquishyPhysicsParameters physParams,
            SquishyVisualParameters visParams,
            SquishyAudioParameters audParams,
            SquishyHapticParameters hapParams)
        {
            id = presetId;
            displayName = name;
            category = cat;
            physics = physParams;
            visual = visParams;
            audio = audParams;
            haptic = hapParams;
        }
    }
}
