using UnityEngine;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// Bootstraps all Decoration module services to the DI container.
    /// Runs automatically before scenes load to prevent tight coupling.
    /// </summary>
    public static class DecorationBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Create and Register Preset Provider (Library)
            var library = ScriptableObject.CreateInstance<DecorationLibrary>();
            library.InitializeLibrary();
            container.Register<IDecorationPresetProvider>(library);

            // 2. Create and Register Decoration Controller
            var controller = new DecorationController(library);
            container.Register<IDecorationController>(controller);

            Debug.Log("[FRTE Decoration] Decoration DI services successfully bootstrapped.");
        }
    }
}
