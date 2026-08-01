using System;
using System.Collections.Generic;

namespace FRTE.Collection
{
    /// <summary>
    /// Packaged container for serializing the collection book data locally.
    /// </summary>
    [Serializable]
    public sealed class CollectionSaveData
    {
        public List<CollectionEntryData> Entries = new List<CollectionEntryData>();
    }
}
