using UnityEngine;
using FRTE.Core;

namespace FRTE.Collection
{
    /// <summary>
    /// Bootstraps all Collection Book module services to the DI container.
    /// Runs automatically before scenes load to prevent coupling.
    /// </summary>
    public static class CollectionBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Repository
            var repo = new CollectionRepository();
            container.Register<ICollectionRepository>(repo);

            // 2. Controller
            var controller = new CollectionController(repo);
            container.Register<ICollectionController>(controller);

            Debug.Log("[FRTE Collection] Collection Book DI services successfully bootstrapped.");
        }
    }
}
