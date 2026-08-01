using System;

namespace FRTE.Core
{
    /// <summary>
    /// Holds physical runtime configuration for an instantiated decoration placement.
    /// Preserved separately from the read-only preset assets.
    /// </summary>
    [Serializable]
    public sealed class DecorationInstanceData
    {
        public string InstanceId;
        public string PresetId;
        public Vector2 NormalizedPosition;
        public Vector2 Scale = UnityEngine.Vector2.one;
        public float Rotation;
        public bool FlipX;
        public int SortingOrder;
        public bool IsVisible = true;
    }
}
