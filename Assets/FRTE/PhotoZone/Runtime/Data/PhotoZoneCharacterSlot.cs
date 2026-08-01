using System;
using UnityEngine;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Configures default size and offset boundaries for placing the signature FruitRabbit character illustration.
    /// </summary>
    [Serializable]
    public struct PhotoZoneCharacterSlot
    {
        public string SlotId;
        public string FruitRabbitId; // e.g. "strawberry_rabbit"
        public Vector2 Position;
        public Vector2 Scale;
        public float Rotation;
    }
}
