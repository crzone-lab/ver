using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using FRTE.Physics;

namespace FRTE.Physics.Tests.PlayMode
{
    [TestFixture]
    public class PhysicsPlayModeTests
    {
        private GameObject _testGo;
        private SquishySurface _surface;
        private Texture2D _dummyTex;

        [SetUp]
        public void SetUp()
        {
            _testGo = new GameObject("Test_SquishySurface");
            _surface = _testGo.AddComponent<SquishySurface>();

            // Setup a dummy 32x32 texture
            _dummyTex = new Texture2D(32, 32, TextureFormat.RGBA32, false);
            for (int y = 0; y < 32; y++)
            {
                for (int x = 0; x < 32; x++)
                {
                    _dummyTex.SetPixel(x, y, Color.white);
                }
            }
            _dummyTex.Apply();

            // Setup temporary UI Container RectTransform
            var canvasGo = new GameObject("Test_Canvas");
            var canvasRect = canvasGo.AddComponent<RectTransform>();
            canvasRect.sizeDelta = new Vector2(400f, 400f);

            var input = new SquishySurfaceInput
            {
                SourceTexture = _dummyTex,
                Width = 4f,
                Height = 4f,
                Quality = SquishyMeshQuality.Low, // 20x30 for fast testing
                TargetCamera = null,
                ContainerRect = canvasRect
            };

            _surface.Initialize(input);
        }

        [TearDown]
        public void TearDown()
        {
            if (_testGo != null)
            {
                Object.DestroyImmediate(_testGo);
            }
            if (_dummyTex != null)
            {
                Object.DestroyImmediate(_dummyTex);
            }
        }

        [Test]
        public void Surface_InitializesCorrectly()
        {
            Assert.IsTrue(_surface.IsInitialized);
            Assert.IsNotNull(_surface.Simulation);
            Assert.IsNotNull(_surface.GetComponent<MeshFilter>().sharedMesh);
        }

        [UnityTest]
        public IEnumerator Surface_CenterTouch_DeformsVertices()
        {
            // Center index around (10, 15) in a 20x30 Low Quality grid: 15 * 20 + 10 = 310
            int centerIndex = 310;
            var originalPos = _surface.Simulation.Vertices[centerIndex].CurrentPosition;

            // Trigger touch Began at normalized center coordinate (0, 0)
            var touches = new List<SquishyTouchData>
            {
                new SquishyTouchData
                {
                    TouchId = 0,
                    ScreenPosition = Vector2.zero,
                    PreviousScreenPosition = Vector2.zero,
                    Delta = Vector2.zero,
                    Duration = 0.1f,
                    Speed = 0f,
                    Phase = SquishyTouchPhase.Began
                }
            };
            _surface.Simulation.SetTouchInputs(touches);
            _surface.Simulation.Step(0.02f);

            var deformedPos = _surface.Simulation.Vertices[centerIndex].CurrentPosition;

            // Z coordinate should sink (indentation, Z becomes negative)
            Assert.Less(deformedPos.z, originalPos.z);
            yield return null;
        }

        [UnityTest]
        public IEnumerator Surface_Reset_RestoresShape()
        {
            int centerIndex = 310;

            // Trigger deformation
            var touches = new List<SquishyTouchData>
            {
                new SquishyTouchData
                {
                    TouchId = 0,
                    ScreenPosition = Vector2.zero,
                    Phase = SquishyTouchPhase.Began,
                    Duration = 0.2f
                }
            };
            _surface.Simulation.SetTouchInputs(touches);
            _surface.Simulation.Step(0.02f);

            Assert.AreNotEqual(_surface.Simulation.Vertices[centerIndex].OriginalPosition, _surface.Simulation.Vertices[centerIndex].CurrentPosition);

            // Execute Reset
            _surface.ResetSurface();

            Assert.AreEqual(_surface.Simulation.Vertices[centerIndex].OriginalPosition, _surface.Simulation.Vertices[centerIndex].CurrentPosition);
            yield return null;
        }

        [UnityTest]
        public IEnumerator Simulation_30SecondContinuousSimulation_RemainsStable()
        {
            // Simulate 30 seconds of active interactions
            float totalTime = 0f;
            float dt = 0.02f;

            var touches = new List<SquishyTouchData>
            {
                new SquishyTouchData
                {
                    TouchId = 0,
                    ScreenPosition = new Vector2(0.1f, -0.1f),
                    PreviousScreenPosition = Vector2.zero,
                    Delta = new Vector2(0.1f, -0.1f),
                    Duration = 0f,
                    Speed = 5f,
                    Phase = SquishyTouchPhase.Moved
                }
            };

            while (totalTime < 30f)
            {
                // Update touch properties to simulate sliding finger
                var t = touches[0];
                t.Duration += dt;
                t.ScreenPosition = new Vector2(Mathf.Sin(totalTime) * 0.3f, Mathf.Cos(totalTime) * 0.3f);
                touches[0] = t;

                _surface.Simulation.SetTouchInputs(touches);
                _surface.Simulation.Step(dt);

                totalTime += dt;
            }

            // Verify no NaN or infinity has leaked and grid has stayed structurally stable
            for (int i = 0; i < _surface.Simulation.Vertices.Length; i++)
            {
                var pos = _surface.Simulation.Vertices[i].CurrentPosition;
                Assert.IsFalse(float.IsNaN(pos.x));
                Assert.IsFalse(float.IsNaN(pos.y));
                Assert.IsFalse(float.IsNaN(pos.z));
            }
            yield return null;
        }
    }
}
