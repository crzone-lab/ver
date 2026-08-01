using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using FRTE.Core;

namespace FRTE.Decoration.Tests
{
    [TestFixture]
    public sealed class DecorationPlayModeTests
    {
        private GameObject _holder;
        private DecorationLibrary _library;
        private DecorationController _controller;

        [SetUp]
        public void SetUp()
        {
            _holder = new GameObject("DecorationPlayTest");
            
            _library = ScriptableObject.CreateInstance<DecorationLibrary>();
            _library.InitializeLibrary();
            
            _controller = new DecorationController(_library);

            // Register Mock face provider to container
            var container = FRTESdkManager.Instance.Container;
            if (!container.TryResolve<IFaceLandmarkProvider>(out _))
            {
                container.Register<IFaceLandmarkProvider>(new FRTE.AI.MockFaceLandmarkProvider());
            }
        }

        [TearDown]
        public void TearDown()
        {
            if (_holder != null) Object.DestroyImmediate(_holder);
            if (_library != null) Object.DestroyImmediate(_library);
        }

        [UnityTest]
        public IEnumerator DecorationController_AddAndManipulate_WorksCorrectly()
        {
            // 1. Add ear decoration
            string id = _controller.AddDecoration("ear.strawberry");
            Assert.IsNotEmpty(id);
            Assert.AreEqual(1, _controller.CurrentDecorations.Count);
            Assert.AreEqual(id, _controller.SelectedInstanceId);

            // 2. Test Move
            var inst = _controller.CurrentDecorations[0];
            Vector2 oldPos = inst.NormalizedPosition;
            _controller.MoveDecoration(id, new Vector2(0.2f, 0.1f));
            Assert.AreNotEqual(oldPos, inst.NormalizedPosition);

            // 3. Test Flip
            Assert.IsFalse(inst.FlipX);
            _controller.FlipDecoration(id);
            Assert.IsTrue(inst.FlipX);

            // 4. Test Duplicate
            _controller.DuplicateDecoration(id);
            Assert.AreEqual(2, _controller.CurrentDecorations.Count);

            // 5. Test Delete
            _controller.DeleteDecoration(id);
            Assert.AreEqual(1, _controller.CurrentDecorations.Count);

            // 6. Test ClearAll
            _controller.ClearAll();
            Assert.AreEqual(0, _controller.CurrentDecorations.Count);

            yield return null;
        }
    }
}
