using System.Collections.Generic;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Contract for querying PhotoZone presets.
    /// </summary>
    public interface IPhotoZoneProvider
    {
        IReadOnlyList<PhotoZonePreset> GetAll();
        bool TryGetById(string id, out PhotoZonePreset preset);
        PhotoZonePreset GetDefault();
    }
}
