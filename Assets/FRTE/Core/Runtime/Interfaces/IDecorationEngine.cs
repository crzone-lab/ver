using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for the Layered Decoration Engine. Manages adding, positioning,
    /// and rendering accessory items (ears, glasses, stickers) bound to AI landmarks.
    /// </summary>
    public interface IDecorationEngine
    {
        void AddDecoration(string key, GameObject prefab, LandmarkType anchor, int sortingOrder, Vector3 offset);
        void RemoveDecoration(string key);
        void ClearDecorations();
        void UpdateDecorationPositions(LandmarkData[] landmarks, float meshWidth, float meshHeight);
    }
}
