using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

namespace FRTE.Materials.Editor
{
    /// <summary>
    /// Validates ScriptableObject material assets for duplicate or blank IDs.
    /// Executes automatically during asset post-processing.
    /// </summary>
    public sealed class MaterialPresetValidator : AssetPostprocessor
    {
        private static void OnPostprocessAllAssets(
            string[] importedAssets, 
            string[] deletedAssets, 
            string[] movedAssets, 
            string[] movedFromAssetPaths)
        {
            // Run validation check when any MaterialPreset is saved or imported
            bool shouldValidate = false;
            for (int i = 0; i < importedAssets.Length; i++)
            {
                if (importedAssets[i].EndsWith(".asset"))
                {
                    shouldValidate = true;
                    break;
                }
            }

            if (shouldValidate)
            {
                ValidatePresetsInProject();
            }
        }

        [MenuItem("FRTE/Squishy/Validate Material Presets")]
        public static void ValidatePresetsInProject()
        {
            string[] guids = AssetDatabase.FindAssets("t:SquishyMaterialPreset");
            var idRegistry = new Dictionary<string, string>(); // maps ID to asset path
            int errorCount = 0;

            for (int i = 0; i < guids.Length; i++)
            {
                string path = AssetDatabase.GUIDToAssetPath(guids[i]);
                var preset = AssetDatabase.LoadAssetAtPath<SquishyMaterialPreset>(path);

                if (preset == null) continue;

                // 1. Verify empty ID
                if (string.IsNullOrEmpty(preset.Id))
                {
                    Debug.LogError($"[PresetValidator] Blank ID detected in asset: '{path}'", preset);
                    errorCount++;
                    continue;
                }

                // 2. Verify duplicate ID
                if (idRegistry.TryGetValue(preset.Id, out var existingPath))
                {
                    Debug.LogError($"[PresetValidator] Duplicate preset ID '{preset.Id}' detected!\n" +
                                   $"Asset A: '{existingPath}'\n" +
                                   $"Asset B: '{path}'", preset);
                    errorCount++;
                }
                else
                {
                    idRegistry.Add(preset.Id, path);
                }
            }

            if (errorCount == 0)
            {
                Debug.Log($"[PresetValidator] Successfully validated {guids.Length} material presets. 0 errors found.");
            }
            else
            {
                Debug.LogError($"[PresetValidator] Validation completed with {errorCount} errors. Please resolve duplicate/blank IDs.");
            }
        }
    }
}
