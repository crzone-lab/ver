using UnityEngine;
using FRTE.Core;

namespace FRTE.Materials
{
    /// <summary>
    /// Static bootstrapper that automatically registers all Materials module services
    /// to the SDK container before scenes load. Decouples assembly dependencies.
    /// </summary>
    public static class SquishyMaterialBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Create and Register Material Preset Provider (Library)
            var library = ScriptableObject.CreateInstance<SquishyMaterialLibrary>();
            library.InitializeLibrary();
            container.Register<IMaterialPresetProvider>(library);

            // 2. Create and Register Settings Repository
            var repo = new SquishySettingsRepository();
            container.Register<ISquishySettingsRepository>(repo);

            // 3. Create and Register Voice-Pooled Audio Service
            var audioGo = new GameObject("FRTE_AudioServiceContainer");
            Object.DontDestroyOnLoad(audioGo);
            var audioService = audioGo.AddComponent<SquishyAudioService>();
            container.Register<ISquishyAudioService>(audioService);

            // 4. Create and Register Preset Controller
            var controller = new MaterialPresetController(library, repo, audioService);
            container.Register<IMaterialPresetController>(controller);

            Debug.Log("[FRTE Materials] Materials DI services successfully bootstrapped.");
        }
    }
}
