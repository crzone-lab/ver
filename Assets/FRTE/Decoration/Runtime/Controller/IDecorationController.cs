using System.Collections.Generic;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// Contract for the runtime decoration placement manager.
    /// Supports transforms, sorting orders, flips, duplicates, and deletions.
    /// </summary>
    public interface IDecorationController
    {
        string SelectedInstanceId { get; set; }
        IReadOnlyList<DecorationInstanceData> CurrentDecorations { get; }

        string AddDecoration(string presetId);
        void MoveDecoration(string instanceId, Vector2 delta);
        void RotateDecoration(string instanceId, float deltaAngle);
        void ScaleDecoration(string instanceId, Vector2 deltaScale);
        void FlipDecoration(string instanceId);
        void DeleteDecoration(string instanceId);
        void DuplicateDecoration(string instanceId);

        void SendToFront(string instanceId);
        void SendToBack(string instanceId);
        void SendForward(string instanceId);
        void SendBackward(string instanceId);

        void ClearAll();
    }
}
