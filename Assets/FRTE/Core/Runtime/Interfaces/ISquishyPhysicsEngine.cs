using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for the Squishy Physics Engine. Controls simulation grid,
    /// material properties, and processes multi-touch interaction forces.
    /// </summary>
    public interface ISquishyPhysicsEngine
    {
        FRTEMaterialConfig MaterialConfig { get; set; }
        int GridWidth { get; }
        int GridHeight { get; }
        Vector3[] GetDeformedPositions();
        Vector3[] GetRestPositions();
        void InitializeGrid(int gridWidth, int gridHeight);
        void UpdateTouch(int touchId, Vector2 normalizedUV, TouchPhase phase, float pressure, float duration, float dragSpeed);
        void StepSimulation(float deltaTime);
        void ResetSimulation();
    }
}
