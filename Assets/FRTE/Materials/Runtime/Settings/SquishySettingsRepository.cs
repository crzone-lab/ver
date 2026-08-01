using UnityEngine;

namespace FRTE.Materials
{
    /// <summary>
    /// Implements local settings storage using Unity's PlayerPrefs and JsonUtility.
    /// Defends against corrupted configurations, out-of-bound variables, or missing fields.
    /// </summary>
    public sealed class SquishySettingsRepository : ISquishySettingsRepository
    {
        private const string PrefsKey = "FRTE_SquishyUserSettings";

        public SquishyUserSettings Load()
        {
            if (!PlayerPrefs.HasKey(PrefsKey))
            {
                return new SquishyUserSettings(); // Default values
            }

            string json = PlayerPrefs.GetString(PrefsKey);
            if (string.IsNullOrEmpty(json))
            {
                return new SquishyUserSettings();
            }

            try
            {
                var settings = JsonUtility.FromJson<SquishyUserSettings>(json);
                if (settings == null)
                {
                    return new SquishyUserSettings();
                }

                // --- VALIDATE AND CLAMP VARIABLES ---
                if (settings.AudioVolume < 0f || settings.AudioVolume > 2f || float.IsNaN(settings.AudioVolume))
                {
                    settings.AudioVolume = 1f; // Sane default
                }
                if (settings.VisualEffectsStrength < 0f || settings.VisualEffectsStrength > 5f || float.IsNaN(settings.VisualEffectsStrength))
                {
                    settings.VisualEffectsStrength = 1f;
                }
                if (string.IsNullOrEmpty(settings.SelectedPresetId))
                {
                    settings.SelectedPresetId = "basic.jelly";
                }
                if (settings.MeshQuality != "Low" && settings.MeshQuality != "Medium" && settings.MeshQuality != "High")
                {
                    settings.MeshQuality = "Medium";
                }

                return settings;
            }
            catch (System.Exception ex)
            {
                Debug.LogWarning($"[SettingsRepository] Loading corrupted JSON failed (restoring default): {ex.Message}");
                return new SquishyUserSettings();
            }
        }

        public void Save(SquishyUserSettings settings)
        {
            if (settings == null) return;

            try
            {
                string json = JsonUtility.ToJson(settings);
                PlayerPrefs.SetString(PrefsKey, json);
                PlayerPrefs.Save();

                // Notify Event Bus for tracking
                var eventBus = FRTE.Core.FRTESdkManager.Instance.EventBus;
                if (eventBus != null)
                {
                    eventBus.Publish(new SquishySettingsChangedEvent { Settings = settings });
                }
            }
            catch (System.Exception ex)
            {
                Debug.LogError($"[SettingsRepository] Save configurations failed: {ex.Message}");
            }
        }

        public void Reset()
        {
            PlayerPrefs.DeleteKey(PrefsKey);
            PlayerPrefs.Save();
        }
    }

    /// <summary>
    /// Event broadcast when user settings are altered.
    /// </summary>
    public struct SquishySettingsChangedEvent
    {
        public SquishyUserSettings Settings;
    }
}
