using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Physics.Tests
{
    [TestFixture]
    public class PhysicsSimulationTests
    {
        private FRTEContainer _container;
        private SquishyPhysicsSolver _solver;

        [SetUp]
        public void SetUp()
        {
            _container = new FRTEContainer();
            _solver = new SquishyPhysicsSolver();
            _solver.Initialize(_container);
            _solver.Enable();
        }

        [TearDown]
        public void TearDown()
        {
            _solver.Disable();
            _container.Clear();
        }

        [Test]
        public void GridInitialization_MapsUvsCorrectly()
        {
            _solver.InitializeGrid(4, 4);

            var restPositions = _solver.GetRestPositions();
            Assert.AreEqual(16, restPositions.Length);

            // Verify corner bounds
            Assert.AreEqual(new Vector3(0f, 0f, 0f), restPositions[0]);
            Assert.AreEqual(new Vector3(1f, 1f, 0f), restPositions[15]);
        }

        [Test]
        public void TouchForces_DeformGridNodes()
        {
            _solver.InitializeGrid(10, 10);

            // Center of the grid (index 45: row 4, col 5 is roughly center)
            Vector2 touchUV = new Vector2(0.5f, 0.5f);
            
            // Check original state
            Vector3 originalCenter = _solver.GetDeformedPositions()[45];

            // Apply touchBegans
            _solver.UpdateTouch(0, touchUV, TouchPhase.Began, pressure: 1.0f, duration: 0f, dragSpeed: 0f);
            _solver.StepSimulation(0.016f);

            Vector3 deformedCenter = _solver.GetDeformedPositions()[45];

            // Indentation forces should push center node down in Z direction (negative Z)
            Assert.Less(deformedCenter.z, originalCenter.z);
        }

        [Test]
        public void Reset_RestoresOriginalPositions()
        {
            _solver.InitializeGrid(5, 5);
            Vector2 touchUV = new Vector2(0.5f, 0.5f);

            _solver.UpdateTouch(0, touchUV, TouchPhase.Began, pressure: 1.0f, duration: 0f, dragSpeed: 0f);
            _solver.StepSimulation(0.02f);

            _solver.ResetSimulation();

            var deformed = _solver.GetDeformedPositions();
            var rest = _solver.GetRestPositions();

            for (int i = 0; i < deformed.Length; i++)
            {
                Assert.AreEqual(rest[i], deformed[i]);
            }
        }
    }
}
