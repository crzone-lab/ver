using System.IO;
using UnityEngine;

namespace FRTE.Export
{
    /// <summary>
    /// Implements IExportStorageService, managing directory creation and local disk space safety checks.
    /// </summary>
    public sealed class ExportStorageService : IExportStorageService
    {
        public string TemporaryDirectory { get; }
        public string ExportDirectory { get; }

        public ExportStorageService()
        {
            TemporaryDirectory = Path.Combine(Application.temporaryCachePath, "FRTE_Cache");
            ExportDirectory = Path.Combine(Application.persistentDataPath, "FRTE_Export");

            EnsureDirectoriesExist();
        }

        public bool HasEnoughSpace(long estimatedBytes)
        {
            // Safeguard fallback: check local partition space in Editor/Standalone
#if UNITY_EDITOR || UNITY_STANDALONE
            try
            {
                var drive = new DriveInfo(Path.GetPathRoot(ExportDirectory));
                return drive.AvailableFreeSpace > estimatedBytes + 10 * 1024 * 1024; // 10MB safety margin
            }
            catch
            {
                return true; // Fallback if DriveInfo is unsupported (WebGL or mobile)
            }
#else
            return true; // Handled natively by Scoped Storage on modern mobile
#endif
        }

        public void CleanTemporaryFiles()
        {
            if (Directory.Exists(TemporaryDirectory))
            {
                try
                {
                    var files = Directory.GetFiles(TemporaryDirectory);
                    for (int i = 0; i < files.Length; i++)
                    {
                        File.Delete(files[i]);
                    }
                }
                catch (System.Exception ex)
                {
                    Debug.LogWarning($"[ExportStorageService] Failed to clear temp files: {ex.Message}");
                }
            }
        }

        private void EnsureDirectoriesExist()
        {
            if (!Directory.Exists(TemporaryDirectory))
            {
                Directory.CreateDirectory(TemporaryDirectory);
            }
            if (!Directory.Exists(ExportDirectory))
            {
                Directory.CreateDirectory(ExportDirectory);
            }
        }
    }
}
