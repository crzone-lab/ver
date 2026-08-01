using System.Threading.Tasks;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for the high-performance media export engine.
    /// Performs asynchronous GPU readbacks and background thread encoding (PNG, GIF, MP4)
    /// to prevent mobile gameplay frame rate hitches.
    /// </summary>
    public interface IExportEngine
    {
        Task ExportPNGAsync(RenderTexture texture, string filePath);
        Task ExportGIFAsync(RenderTexture[] frames, int fps, string filePath);
    }
}
