using UnityEngine;
using FRTE.Core;

namespace FRTE.PhotoZone
{
    /// <summary>
    /// Bootstraps all PhotoZone module services to the DI container.
    /// Runs automatically before scenes load to prevent coupling.
    /// </summary>
    public static class PhotoZoneBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Provider
            var library = ScriptableObject.CreateInstance<PhotoZoneLibrary>();
            library.InitializeLibrary();
            container.Register<IPhotoZoneProvider>(library);

            // 2. Controller
            var controller = new PhotoZoneController(library);
            container.Register<IPhotoZoneController>(controller);

            Debug.Log("[FRTE PhotoZone] PhotoZone DI services successfully bootstrapped.");
        }
    }
}
