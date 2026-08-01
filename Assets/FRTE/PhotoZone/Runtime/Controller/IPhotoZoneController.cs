using FRTE.Core;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Contract for controlling active PhotoZone layer configurations.
    /// Supports visibility toggles and preset swapping.
    /// </summary>
    public interface IPhotoZoneController
    {
        PhotoZonePreset CurrentPreset { get; }

        bool ApplyPhotoZone(string presetId);
        void ClearPhotoZone();
        void SetLayerVisibility(PhotoZoneLayer layer, bool visible);
    }
}
