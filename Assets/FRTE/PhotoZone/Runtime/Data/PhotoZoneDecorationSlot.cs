using System;
using UnityEngine;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Holds preset accessory decoration configurations attached to a specific PhotoZone.
    /// </summary>
    [Serializable]
    public struct PhotoZoneDecorationSlot
    {
        public string DecorationPresetId;
        public Vector2 LocalPosition;
        public Vector2 LocalScale;
        public float LocalRotation;
    }
}
