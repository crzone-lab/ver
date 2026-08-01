using System;
using System.Collections.Generic;
using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Implements the spring-damper physical simulation for a deformable 2D soft-body grid.
    /// Manages node integration, boundary clamping, virtual pressure, and recovery wobbles.
    /// </summary>
    public sealed class SquishySimulation : ISquishySimulation
    {
        private int _columns;
        private int _rows;
        private SquishyVertexState[] _vertices;
        private readonly List<SquishyTouchData> _activeTouches = new List<SquishyTouchData>();

        /// <summary>
        /// Gets the width of the simulation grid.
        /// </summary>
        public int Columns => _columns;

        /// <summary>
        /// Gets the height of the simulation grid.
        /// </summary>
        public int Rows => _rows;

        /// <summary>
        /// Gets the array containing the current physical state of all grid nodes.
        /// </summary>
        public SquishyVertexState[] Vertices => _vertices;

        /// <summary>
        /// Gets or sets the active simulation settings.
        /// </summary>
        public SquishySimulationSettings Settings { get; set; } = new SquishySimulationSettings();

        /// <summary>
        /// Initializes the physics simulation grid.
        /// </summary>
        /// <param name="columns">Number of columns.</param>
        /// <param name="rows">Number of rows.</param>
        public void InitializeGrid(int columns, int rows)
        {
            _columns = columns;
            _rows = rows;
            int count = columns * rows;
            _vertices = new SquishyVertexState[count];

            ResetSimulation();
        }

        public void SetTouchInputs(List<SquishyTouchData> touches)
        {
            _activeTouches.Clear();
            if (touches != null)
            {
                _activeTouches.AddRange(touches);
            }
        }

        public void ResetSimulation()
        {
            if (_vertices == null || _vertices.Length == 0) return;

            int count = _vertices.Length;
            for (int y = 0; y < _rows; y++)
            {
                for (int x = 0; x < _columns; x++)
                {
                    int index = y * _columns + x;
                    float u = (float)x / (_columns - 1);
                    float v = (float)y / (_rows - 1);

                    // Original UV coordinates mapped to local [-0.5, 0.5] space for Z deformation rendering
                    Vector3 position = new Vector3(u - 0.5f, v - 0.5f, 0f);

                    // Compute Edge Weight: 0.0 at center, reaching 1.0 at edges and up to 1.414 at corners
                    float dx = Mathf.Abs(u - 0.5f) * 2f;
                    float dy = Mathf.Abs(v - 0.5f) * 2f;
                    float edgeWeight = Mathf.Max(dx, dy);

                    _vertices[index] = new SquishyVertexState
                    {
                        InitialPosition = position,
                        OriginalPosition = position,
                        CurrentPosition = position,
                        Velocity = Vector3.zero,
                        AccumulatedForce = Vector3.zero,
                        EdgeWeight = edgeWeight
                    };
                }
            }
            _activeTouches.Clear();
        }

        public void Step(float deltaTime)
        {
            if (_vertices == null || _vertices.Length == 0) return;

            // 1. Defend against anomalous frame spikes (max 30FPS equivalent time step)
            deltaTime = Mathf.Clamp(deltaTime, 0.001f, 0.033f);

            int totalNodes = _vertices.Length;
            float invMass = 1.0f / Mathf.Max(0.01f, Settings.Mass);

            // Cached local values for optimization
            float springK = Settings.SpringStrength;
            float neighborK = Settings.NeighborSpringStrength;
            float viscC = Settings.Damping;
            float stretchLimit = Settings.MaxDisplacement;
            float edgeResistance = Settings.EdgeResistance;
            float wobbleFreq = Settings.WobbleFrequency;
            float wobbleAmp = Settings.WobbleAmount;
            float radius = Settings.TouchRadius;

            // 8x Substepping
            int substeps = 8;
            float subDeltaTime = deltaTime / substeps;

            // Neighbor spring definitions (immediate distance 1, diagonal shear, bending distance 2)
            int[] nx = { -1, 1, 0, 0, -1, 1, -1, 1, -2, 2, 0, 0 };
            int[] ny = { 0, 0, -1, 1, -1, 1, 1, -1, 0, 0, -2, 2 };
            float[] springMultiplier = { 1f, 1f, 1f, 1f, 0.8f, 0.8f, 0.8f, 0.8f, 0.5f, 0.5f, 0.5f, 0.5f };

            float restDistanceX = 1.0f / (_columns - 1);
            float restDistanceY = 1.0f / (_rows - 1);
            float restDiag = Mathf.Sqrt(restDistanceX * restDistanceX + restDistanceY * restDistanceY);

            // Track active touches
            int activeTouchCount = _activeTouches.Count;

            for (int step = 0; step < substeps; step++)
            {
                // Force buffer
                Vector3[] forces = new Vector3[totalNodes];

                // 2. Compute internal structural and restoration forces
                for (int y = 0; y < _rows; y++)
                {
                    for (int x = 0; x < _columns; x++)
                    {
                        int index = y * _columns + x;
                        var node = _vertices[index];

                        Vector3 force = Vector3.zero;

                        // --- FORCE 1: Restoration to Rest Position (Hooke's Law with Edge resistance) ---
                        Vector3 displacement = node.OriginalPosition - node.CurrentPosition;
                        float stiffness = springK * (1.0f + node.EdgeWeight * edgeResistance);
                        force += displacement * stiffness;

                        // --- FORCE 2: Neighbor spring forces (Structural membrane) ---
                        for (int n = 0; n < 12; n++)
                        {
                            int neighborX = x + nx[n];
                            int neighborY = y + ny[n];

                            if (neighborX >= 0 && neighborX < _columns && neighborY >= 0 && neighborY < _rows)
                            {
                                int neighborIndex = neighborY * _columns + neighborX;
                                var neighbor = _vertices[neighborIndex];

                                Vector3 dir = node.CurrentPosition - neighbor.CurrentPosition;
                                float currentDist = dir.magnitude;

                                if (currentDist > 0.0001f)
                                {
                                    float restDist = restDistanceX;
                                    if (n < 4) // Structural
                                    {
                                        restDist = (nx[n] != 0) ? restDistanceX : restDistanceY;
                                    }
                                    else if (n < 8) // Shear
                                    {
                                        restDist = restDiag;
                                    }
                                    else // Bending
                                    {
                                        restDist = (nx[n] != 0) ? (restDistanceX * 2f) : (restDistanceY * 2f);
                                    }

                                    float deltaDist = currentDist - restDist;
                                    force -= (dir / currentDist) * (deltaDist * neighborK * springMultiplier[n]);
                                }
                            }
                        }

                        // --- FORCE 3: Viscous Damping ---
                        force -= node.Velocity * viscC;

                        // --- FORCE 4: Wobble perturbation (for jelly secondary wiggle) ---
                        if (wobbleAmp > 0.001f && node.Velocity.sqrMagnitude > 0.0001f)
                        {
                            float wobbleTime = Time.time * wobbleFreq;
                            Vector3 wobbleForce = new Vector3(
                                Mathf.Sin(node.OriginalPosition.x * 5f + wobbleTime),
                                Mathf.Cos(node.OriginalPosition.y * 5f + wobbleTime),
                                Mathf.Sin(wobbleTime)
                            ) * (wobbleAmp * node.Velocity.magnitude * 0.15f);
                            force += wobbleForce;
                        }

                        forces[index] = force;
                    }
                }

                // 3. Compute external touch forces
                bool[] isTouched = new bool[totalNodes];
                for (int t = 0; t < activeTouchCount; t++)
                {
                    var touch = _activeTouches[t];
                    if (touch.Phase == SquishyTouchPhase.Ended || touch.Phase == SquishyTouchPhase.Canceled)
                    {
                        continue;
                    }

                    Vector2 touchPos = touch.ScreenPosition;

                    // Calculate virtual pressure
                    float duration = touch.Duration;
                    float speed = touch.Speed;
                    float virtualPressure = Mathf.Clamp01(0.3f + duration * 0.5f + speed * 1.2f);

                    for (int i = 0; i < totalNodes; i++)
                    {
                        var node = _vertices[i];
                        Vector2 nodePos2D = new Vector2(node.CurrentPosition.x, node.CurrentPosition.y);

                        float dist = Vector2.Distance(nodePos2D, touchPos);
                        if (dist < radius)
                        {
                            isTouched[i] = true;

                            // Smooth quadratic falloff
                            float influence = 1.0f - (dist / radius);
                            influence = influence * influence;

                            Vector3 touchForce = Vector3.zero;

                            // 1) Indentation (Negative Z depth)
                            touchForce.z += -Settings.TouchStrength * virtualPressure * influence * 1.5f;

                            // 2) Bulging (XY expansion away from pointer)
                            if (dist > 0.001f)
                            {
                                Vector2 radialDir = (nodePos2D - touchPos).normalized;
                                touchForce.x += radialDir.x * Settings.TouchStrength * virtualPressure * influence * 0.4f;
                                touchForce.y += radialDir.y * Settings.TouchStrength * virtualPressure * influence * 0.4f;
                            }

                            // 3) Drag forces
                            if (touch.Phase == SquishyTouchPhase.Moved)
                            {
                                touchForce.x += touch.Delta.x * Settings.DragStrength * influence * 3.5f;
                                touchForce.y += touch.Delta.y * Settings.DragStrength * influence * 3.5f;
                            }

                            // Apply cumulative limits per node to prevent explosions
                            forces[i] += Vector3.ClampMagnitude(touchForce, Settings.MultiTouchForceLimit);
                        }
                    }
                }

                // 4. Integrate equations of motion (Semi-Implicit Euler)
                for (int i = 0; i < totalNodes; i++)
                {
                    var node = _vertices[i];
                    node.AccumulatedForce = forces[i];

                    Vector3 acceleration = node.AccumulatedForce * invMass;
                    node.Velocity += acceleration * subDeltaTime;

                    // Clamp velocity to prevent physical divergence/explosion
                    node.Velocity = Vector3.ClampMagnitude(node.Velocity, 25f);

                    // Update position
                    Vector3 newPos = node.CurrentPosition + node.Velocity * subDeltaTime;

                    // Displacement clamp relative to original resting positions
                    Vector3 offset = newPos - node.OriginalPosition;
                    if (offset.magnitude > stretchLimit)
                    {
                        offset = offset.normalized * stretchLimit;
                        newPos = node.OriginalPosition + offset;
                        node.Velocity = Vector3.zero; // Dampen velocity to rest at limit bounds
                    }

                    // Edge nodes recovery multiplier to snap back with delay
                    if (node.EdgeWeight > 0.5f && activeTouchCount == 0)
                    {
                        node.Velocity += (node.OriginalPosition - newPos) * (Settings.RecoveryMultiplier * 0.5f);
                    }

                    node.CurrentPosition = newPos;

                    // --- Viscoelastic Creep relaxation of rest coordinate ---
                    if (isTouched[i])
                    {
                        node.OriginalPosition = Vector3.Lerp(node.OriginalPosition, node.CurrentPosition, Settings.CreepRate * subDeltaTime);
                    }
                    else
                    {
                        node.OriginalPosition = Vector3.Lerp(node.OriginalPosition, node.InitialPosition, Settings.CreepRecoveryRate * subDeltaTime);
                    }

                    // Sanity check: shield against NaN or Infinity leaking
                    if (float.IsNaN(node.CurrentPosition.x) || float.IsInfinity(node.CurrentPosition.x))
                    {
                        node.CurrentPosition = node.OriginalPosition;
                        node.Velocity = Vector3.zero;
                    }

                    _vertices[i] = node;
                }
            }
        }
    }
}
