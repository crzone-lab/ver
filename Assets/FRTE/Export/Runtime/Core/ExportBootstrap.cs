using UnityEngine;
using FRTE.Core;

namespace FRTE.Export
{
    /// <summary>
    /// Bootstraps all Export/Save/Record module services into the DI registry container.
    /// Runs automatically before scenes load to prevent tight coupling.
    /// </summary>
    public static class ExportBootstrap
    {
        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
        private static void Bootstrap()
        {
            var container = FRTESdkManager.Instance.Container;

            // 1. Storage Service
            var storage = new ExportStorageService();
            container.Register<IExportStorageService>(storage);

            // 2. Project Session Repository
            var projectRepo = new SquishyProjectRepository();
            container.Register<ISquishyProjectRepository>(projectRepo);

            // 3. Capture Source Fallback
            container.Register<ICaptureSource>(new DefaultCaptureSource());

            // 4. Image Exporter
            container.Register<IImageExporter>(new ImageExporter(storage));

            // 5. Video Exporter
            container.Register<IVideoExporter>(new VideoExporter(storage));

            // 6. GIF Exporter
            container.Register<IGifExporter>(new GifExporter(storage));

            // 7. Share Service
            container.Register<IShareService>(new ShareService());

            Debug.Log("[FRTE Export] Export/Save/Record DI services successfully bootstrapped.");
        }
    }
}
