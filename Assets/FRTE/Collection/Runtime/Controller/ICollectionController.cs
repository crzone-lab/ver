using System.Collections.Generic;

namespace FRTE.Collection
{
    /// <summary>
    /// Contract for the active Collection Book coordinator.
    /// </summary>
    public interface ICollectionController
    {
        bool IsDiscovered(string eventId);
        void RegisterDiscovery(string eventId, string relatedFruitId);
        IReadOnlyList<CollectionEntryData> GetEntries();
        void ClearAll();
    }
}
