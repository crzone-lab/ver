using System;

namespace FRTE.Collection
{
    /// <summary>
    /// Holds serializable diagnostic details for a single discovered surprise event.
    /// </summary>
    [Serializable]
    public sealed class CollectionEntryData
    {
        public string EventId = "";
        public bool IsDiscovered;
        public int DiscoveryCount;
        public string FirstDiscoveredUtc = "";
        public string LastDiscoveredUtc = "";
        public string RelatedFruitId = "";
    }
}
