using UnityEngine;

namespace FRTE.Collection
{
    /// <summary>
    /// Implements local PlayerPrefs JSON serialization for the Collection Book.
    /// Safely handles corrupted strings or empty saves.
    /// </summary>
    public sealed class CollectionRepository : ICollectionRepository
    {
        private const string PrefsKey = "FRTE_SquishyCollectionBook";

        public CollectionSaveData Load()
        {
            if (!PlayerPrefs.HasKey(PrefsKey))
            {
                return new CollectionSaveData();
            }

            string json = PlayerPrefs.GetString(PrefsKey);
            if (string.IsNullOrEmpty(json))
            {
                return new CollectionSaveData();
            }

            try
            {
                var data = JsonUtility.FromJson<CollectionSaveData>(json);
                if (data == null || data.Entries == null)
                {
                    return new CollectionSaveData();
                }

                // Sane validation check
                for (int i = 0; i < data.Entries.Count; i++)
                {
                    var ent = data.Entries[i];
                    if (ent == null) continue;
                    if (ent.DiscoveryCount < 0) ent.DiscoveryCount = 0;
                }

                return data;
            }
            catch (System.Exception ex)
            {
                Debug.LogWarning($"[CollectionRepository] Loading corrupted JSON failed (restoring default): {ex.Message}");
                return new CollectionSaveData();
            }
        }

        public void Save(CollectionSaveData data)
        {
            if (data == null) return;

            try
            {
                string json = JsonUtility.ToJson(data);
                PlayerPrefs.SetString(PrefsKey, json);
                PlayerPrefs.Save();
            }
            catch (System.Exception ex)
            {
                Debug.LogError($"[CollectionRepository] Save book failed: {ex.Message}");
            }
        }

        public void Reset()
        {
            PlayerPrefs.DeleteKey(PrefsKey);
            PlayerPrefs.Save();
        }
    }
}
