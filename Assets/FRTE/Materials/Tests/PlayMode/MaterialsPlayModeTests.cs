using System.Collections;
using System.Collections.Generic;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;
using FRTE.Core;
using FRTE.Physics;

namespace FRTE.Materials.Tests
{
    [TestFixture]
    public sealed class MaterialsPlayModeTests
    {
        private GameObject _holderGo;
        private SquishySurface _surface;
        private DeformableJellyRenderer _jellyRenderer;
        private Texture2D _dummyTexture;
        private Camera _dummyCamera;

        [UnitySetUp]
        public IEnumerator UnitySetUp()
        {
            _holderGo = new GameObject("FRTE_PlayMode_Holder");
            _dummyCamera = _holderGo.AddComponent<Camera>();
            _dummyCamera.orthographic = true;

            _dummyTexture = new Texture2D(32, 32);
            _dummyTexture.Apply();

            // Set up Surface
            var surfaceGo = new GameObject("Surface");
            surfaceGo.transform.SetParent(_holderGo.transform);
            _surface = surfaceGo.AddComponent<SquishySurface>();
            _jellyRenderer = surfaceGo.AddComponent<DeformableJellyRenderer>();

            var containerGo = new GameObject("UIContainer");
            containerGo.transform.SetParent(_holderGo.transform);
            var rect = containerGo.AddComponent<RectTransform>();
            rect.sizeDelta = new Vector2(200f, 200f);

            var input = new SquishySurfaceInput
            {
                SourceTexture = _dummyTexture,
                Width = 2f,
                Height = 2f,
                Quality = SquishyMeshQuality.Low,
                TargetCamera = _dummyCamera,
                ContainerRect = rect
            };

            _surface.Initialize(input);

            // Re-bootstrap components if not done
            var container = FRTESdkManager.Instance.Container;
            if (!container.TryResolve<IMaterialPresetController>(out _))
            {
                var library = ScriptableObject.CreateInstance<SquishyMaterialLibrary>();
                library.InitializeLibrary();
                container.Register<IMaterialPresetProvider>(library);

                var repo = new SquishySettingsRepository();
                container.Register<ISquishySettingsRepository>(repo);

                var audioGo = new GameObject("Audio");
                var audioSvc = audioGo.AddComponent<SquishyAudioService>();
                container.Register<ISquishyAudioService>(audioSvc);

                var controller = new MaterialPresetController(library, repo, audioSvc);
                container.Register<IMaterialPresetController>(controller);
            }

            yield return null;
        }

        [UnityTearDown]
        public IEnumerator UnityTearDown()
        {
            if (_holderGo != null)
            {
                Object.Destroy(_holderGo);
            }
            if (_dummyTexture != null)
            {
                Object.Destroy(_dummyTexture);
            }
            yield return null;
        }

        [UnityTest]
        public IEnumerator PresetController_ApplyPreset_ChangesPhysicalParameters()
        {
            var controller = FRTESdkManager.Instance.Container.Resolve<IMaterialPresetController>() as MaterialPresetController;
            controller.BindRenderers(_surface, _jellyRenderer);

            // Apply Rubber (stiff)
            controller.ApplyPreset("basic.rubber");
            yield return new WaitForSeconds(0.4f); // Wait for transition coroutine

            Assert.AreEqual(90f, _surface.Simulation.Settings.SpringStrength);
            Assert.AreEqual(12f, _surface.Simulation.Settings.Damping);

            // Apply Slime (sticky, low spring)
            controller.ApplyPreset("basic.slime");
            yield return new WaitForSeconds(0.4f);

            Assert.AreEqual(15f, _surface.Simulation.Settings.SpringStrength);
            Assert.AreEqual(15f, _surface.Simulation.Settings.Damping);
        }

        [UnityTest]
        public IEnumerator FastSequentialSwapping_RemainsStable()
        {
            var controller = FRTESdkManager.Instance.Container.Resolve<IMaterialPresetController>() as MaterialPresetController;
            controller.BindRenderers(_surface, _jellyRenderer);

            // Rapidly swap presets in subsequent frames
            controller.ApplyPreset("basic.rubber");
            yield return null;
            controller.ApplyPreset("basic.slime");
            yield return null;
            controller.ApplyPreset("basic.mochi");
            yield return null;
            controller.ApplyPreset("basic.jelly");
            yield return new WaitForSeconds(0.4f); // Wait for final transition

            // Confirms it completes safely without throwing NaN/Infinity calculations
            Assert.IsFalse(float.IsNaN(_surface.Simulation.Settings.SpringStrength));
            Assert.AreEqual(50f, _surface.Simulation.Settings.SpringStrength);
        }

        [UnityTest]
        public IEnumerator AudioService_PoolLimitsConcurrentVoices()
        {
            var audioSvc = FRTESdkManager.Instance.Container.Resolve<ISquishyAudioService>() as SquishyAudioService;
            
            var clips = new AudioClip[1];
            clips[0] = AudioClip.Create("TestClip", 44100, 1, 44100, false);
            
            var audParams = new SquishyAudioParameters
            {
                TouchClips = clips,
                Volume = 1f,
                PitchRange = new Vector2(0.9f, 1.1f),
                MinInterval = 0f, // zero cooldown for trigger flooding
                MaxConcurrentVoices = 2
            };
            audioSvc.SetAudioParameters(audParams);

            // Flood play triggers
            var context = new SquishyInteractionContext { Speed = 10f, Intensity = 1f };
            audioSvc.PlayTouch(context);
            audioSvc.PlayTouch(context);
            audioSvc.PlayTouch(context);
            audioSvc.PlayTouch(context);

            // Assert playing voices does not exceed limit
            Assert.LessOrEqual(audioSvc.ActiveVoiceCount, 2);
        }
    }
}
