using System;
using System.Collections.Generic;

namespace FRTE.Core
{
    /// <summary>
    /// Holds serializable workspace session details for loading or resuming projects.
    /// </summary>
    [Serializable]
    public sealed class SquishyProjectSessionData
    {
        public string CurrentMaterialId = "basic.jelly";
        public string CurrentPhotoZoneId = "";
        public List<DecorationInstanceData> Decorations = new List<DecorationInstanceData>();
        public FaceLandmarkData? ManualFaceLandmarks;
        public SquishyAppMode LastMode = SquishyAppMode.PhotoEdit;
    }
}
