using UnityEngine;
using FRTE.Core;

namespace FRTE.Surprise
{
    /// <summary>
    /// Bootstraps all Surprise module services to the DI container.
    /// Runs automatically before scenes load to prevent coupling.
    /// </summary>
    public static class SurpriseBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Create and Register Surprise Effect Pool
            var poolGo = new GameObject("FRTE_SurpriseEffectPool");
            Object.DontDestroyOnLoad(poolGo);
            var pool = poolGo.AddComponent<SurpriseEffectPool>();
            container.Register<ISurpriseEffectPool>(pool);

            // 2. Create and Register Surprise Event Controller
            var controller = new SurpriseEventController();
            container.Register<ISurpriseEventController>(controller);

            Debug.Log("[FRTE SurpriseEvent] Surprise Event DI services successfully bootstrapped.");
        }
    }
}
