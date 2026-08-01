using System;
using UnityEngine;

namespace FRTE.Surprise
{
    /// <summary>
    /// Configures trigger thresholds and rules for surprise events.
    /// </summary>
    [Serializable]
    public struct SurpriseTriggerDefinition
    {
        public SurpriseTriggerType TriggerType;
        public float FloatValue; // threshold tap count, consecutive window duration, press delay
        public string TargetId; // material ID, photo zone ID
        public Rect TargetArea; // normalized area rectangle [x, y, w, h]
    }
}
