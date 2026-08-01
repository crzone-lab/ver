using NUnit.Framework;
using UnityEngine;
using FRTE.Physics;

namespace FRTE.Physics.Tests.EditMode
{
    [TestFixture]
    public class PhysicsEditModeTests
    {
        [Test]
        public void Simulation_InitializeGrid_AllocatesCorrectNodeSizes()
        {
            var sim = new SquishySimulation();
            sim.InitializeGrid(10, 20);

            Assert.AreEqual(10, sim.Columns);
            Assert.AreEqual(20, sim.Rows);
            Assert.AreEqual(200, sim.Vertices.Length);
        }

        [Test]
        public void Simulation_InitializeGrid_MapsRestUVsCorrectly()
        {
            var sim = new SquishySimulation();
            sim.InitializeGrid(3, 3);

            // Bottom-Left node should map to [-0.5, -0.5] local coordinates
            Assert.AreEqual(new Vector3(-0.5f, -0.5f, 0f), sim.Vertices[0].OriginalPosition);

            // Center node should map to [0, 0] local coordinates
            Assert.AreEqual(new Vector3(0f, 0f, 0f), sim.Vertices[4].OriginalPosition);

            // Top-Right node should map to [0.5, 0.5] local coordinates
            Assert.AreEqual(new Vector3(0.5f, 0.5f, 0f), sim.Vertices[8].OriginalPosition);
        }

        [Test]
        public void Simulation_EdgeWeightCalculation_IsCorrect()
        {
            var sim = new SquishySimulation();
            sim.InitializeGrid(3, 3);

            // Center node EdgeWeight should be 0
            Assert.AreEqual(0f, sim.Vertices[4].EdgeWeight, 0.0001f);

            // Edge node (e.g. index 1: center-bottom) EdgeWeight should be 1
            Assert.AreEqual(1f, sim.Vertices[1].EdgeWeight, 0.0001f);

            // Corner node (e.g. index 0: bottom-left) EdgeWeight should be 1
            Assert.AreEqual(1f, sim.Vertices[0].EdgeWeight, 0.0001f);
        }

        [Test]
        public void Simulation_Step_LimitsMaximumDisplacement()
        {
            var sim = new SquishySimulation();
            sim.InitializeGrid(5, 5);
            sim.Settings.MaxDisplacement = 0.1f;
            sim.Settings.SpringStrength = 0f; // Disable restoration to let it stretch indefinitely

            // Trigger touch Began at center (normalized local position [0, 0])
            var touches = new System.Collections.Generic.List<SquishyTouchData>
            {
                new SquishyTouchData
                {
                    TouchId = 0,
                    ScreenPosition = Vector2.zero,
                    PreviousScreenPosition = Vector2.zero,
                    Delta = Vector2.zero,
                    Duration = 0.5f,
                    Speed = 0f,
                    Phase = SquishyTouchPhase.Began
                }
            };
            sim.SetTouchInputs(touches);

            // Step with an extremely high deltaTime to force massive force integration
            sim.Step(1.0f);

            // Verify that no vertex displacement exceeds MaxDisplacement
            for (int i = 0; i < sim.Vertices.Length; i++)
            {
                float disp = Vector3.Distance(sim.Vertices[i].CurrentPosition, sim.Vertices[i].OriginalPosition);
                Assert.LessOrEqual(disp, 0.1001f);
            }
        }

        [Test]
        public void Simulation_Step_PreventsNaNOrInfinity()
        {
            var sim = new SquishySimulation();
            sim.InitializeGrid(5, 5);

            // Set massive force inputs and step
            var touches = new System.Collections.Generic.List<SquishyTouchData>
            {
                new SquishyTouchData
                {
                    TouchId = 0,
                    ScreenPosition = Vector2.zero,
                    Phase = SquishyTouchPhase.Began,
                    Duration = 100f
                }
            };
            sim.SetTouchInputs(touches);
            sim.Step(100f); // Massive deltaTime

            for (int i = 0; i < sim.Vertices.Length; i++)
            {
                var pos = sim.Vertices[i].CurrentPosition;
                Assert.IsFalse(float.IsNaN(pos.x));
                Assert.IsFalse(float.IsNaN(pos.y));
                Assert.IsFalse(float.IsNaN(pos.z));
                Assert.IsFalse(float.IsInfinity(pos.x));
                Assert.IsFalse(float.IsInfinity(pos.y));
                Assert.IsFalse(float.IsInfinity(pos.z));
            }
        }
    }
}
