using UnityEngine;
using System.Text;

#if UNITY_2017_1_OR_NEWER
using UnityEngine.Profiling;
#endif

namespace FRTE.Physics
{
    /// <summary>
    /// Lightweight developer debug panel for real-time physics monitoring and tuning.
    /// Uses IMGUI (OnGUI) to remain self-contained. Excluded in release builds.
    /// </summary>
    public sealed class SquishyDebugPanel : MonoBehaviour
    {
        [Header("Physics Bindings")]
        [SerializeField] private SquishySurface targetSurface;

        [Header("UI Styling")]
        [SerializeField] private bool showPanel = true;

        private float _fps;
        private float _fpsTimer;
        private int _fpsFrames;

        private StringBuilder _sb = new StringBuilder(256);

        private void Start()
        {
            if (targetSurface == null)
            {
                targetSurface = FindObjectOfType<SquishySurface>();
            }
        }

        private void Update()
        {
            // Compute FPS
            _fpsTimer += Time.unscaledDeltaTime;
            _fpsFrames++;
            if (_fpsTimer >= 0.5f)
            {
                _fps = _fpsFrames / _fpsTimer;
                _fpsFrames = 0;
                _fpsTimer = 0f;
            }
        }

#if UNITY_EDITOR || DEVELOPMENT_BUILD
        private void OnGUI()
        {
            if (!showPanel || targetSurface == null || !targetSurface.IsInitialized) return;

            var sim = targetSurface.Simulation;
            var settings = sim.Settings;

            // Draw Background panel (width: 320, height: 620)
            GUI.Box(new Rect(10, 10, 320, 620), "FRTE Squishy Debug Panel");

            int yOffset = 35;
            int rowHeight = 20;

            // --- RESOLVE CONTAINER SERVICES ---
            IMaterialPresetController matController = null;
            IMaterialPresetProvider matProvider = null;
            IAppModeController appModeCtrl = null;
            IDecorationController decCtrl = null;
            IPhotoZoneController zoneCtrl = null;
            ICollectionController bookCtrl = null;
            ISurpriseEventController surpriseCtrl = null;

            var container = FRTESdkManager.Instance.Container;
            if (container != null)
            {
                container.TryResolve<IMaterialPresetController>(out matController);
                container.TryResolve<IMaterialPresetProvider>(out matProvider);
                container.TryResolve<IAppModeController>(out appModeCtrl);
                container.TryResolve<IDecorationController>(out decCtrl);
                container.TryResolve<IPhotoZoneController>(out zoneCtrl);
                container.TryResolve<ICollectionController>(out bookCtrl);
                container.TryResolve<ISurpriseEventController>(out surpriseCtrl);
            }

            // --- READ ONLY MONITOR FIELDS ---
            DrawText(15, yOffset, $"FPS: {_fps:F1}");
            yOffset += rowHeight;

            // 1. App Mode
            string modeName = appModeCtrl != null ? appModeCtrl.CurrentMode.ToString() : "N/A";
            DrawText(15, yOffset, $"App Mode: <color=cyan>{modeName}</color>");
            yOffset += rowHeight;

            // 2. Material Preset Status
            if (matController != null && matController.CurrentPreset != null)
            {
                var preset = matController.CurrentPreset;
                DrawText(15, yOffset, $"Preset: <color=yellow>{preset.DisplayName}</color> ({preset.Id})");
                yOffset += rowHeight;
            }
            else
            {
                DrawText(15, yOffset, "Preset: <color=red>None</color>");
                yOffset += rowHeight;
            }

            // 3. PhotoZone Status
            string zoneId = (zoneCtrl != null && zoneCtrl.CurrentPreset != null) ? zoneCtrl.CurrentPreset.Id : "None";
            DrawText(15, yOffset, $"PhotoZone ID: <color=green>{zoneId}</color>");
            yOffset += rowHeight;

            // 4. Decoration Placements
            int decCount = decCtrl != null ? decCtrl.CurrentDecorations.Count : 0;
            string selDec = (decCtrl != null && !string.IsNullOrEmpty(decCtrl.SelectedInstanceId)) ? decCtrl.SelectedInstanceId.Substring(0, 5) + "..." : "None";
            DrawText(15, yOffset, $"Decorations: {decCount} | Selected: {selDec}");
            yOffset += rowHeight;

            // 5. Surprise & Collection Stats
            int discoveredCount = 0;
            if (bookCtrl != null && bookCtrl.GetEntries() != null)
            {
                for (int i = 0; i < bookCtrl.GetEntries().Count; i++)
                {
                    if (bookCtrl.GetEntries()[i].IsDiscovered) discoveredCount++;
                }
            }
            DrawText(15, yOffset, $"Collection Discovered: {discoveredCount} events");
            yOffset += rowHeight;

            DrawText(15, yOffset, $"Active Touch Count: {GetTouchCount()}");
            yOffset += rowHeight;

            int vertCount = sim.Vertices != null ? sim.Vertices.Length : 0;
            int triCount = vertCount > 0 ? (sim.Columns - 1) * (sim.Rows - 1) * 2 : 0;
            DrawText(15, yOffset, $"Vertices: {vertCount} | Triangles: {triCount}");
            yOffset += rowHeight;

            // Calculate simulation stats
            float maxDisplacement = 0f;
            float maxVelocity = 0f;
            if (sim.Vertices != null && sim.Vertices.Length > 0)
            {
                for (int i = 0; i < sim.Vertices.Length; i++)
                {
                    var v = sim.Vertices[i];
                    float disp = Vector3.Distance(v.CurrentPosition, v.OriginalPosition);
                    if (disp > maxDisplacement) maxDisplacement = disp;

                    float vel = v.Velocity.magnitude;
                    if (vel > maxVelocity) maxVelocity = vel;
                }
            }

            DrawText(15, yOffset, $"Max Disp: {maxDisplacement:F3} | Max Vel: {maxVelocity:F2} m/s");
            yOffset += rowHeight;

            // Audio Voice counts
            long gcMemory = System.GC.GetTotalMemory(false) / (1024 * 1024);
            int activeVoices = 0;
            if (container != null && container.TryResolve<ISquishyAudioService>(out var audioSvc))
            {
                try
                {
                    var prop = audioSvc.GetType().GetProperty("ActiveVoiceCount");
                    if (prop != null) activeVoices = (int)prop.GetValue(audioSvc);
                }
                catch {}
            }
            DrawText(15, yOffset, $"Heap: {gcMemory} MB | Audio Voices: {activeVoices}");
            yOffset += rowHeight;

            yOffset += 5; // spacing

            // --- REAL-TIME SLIDERS FOR TUNING ---
            settings.TouchRadius = DrawSlider(15, ref yOffset, "Touch Radius", settings.TouchRadius, 0.05f, 0.5f);
            settings.TouchStrength = DrawSlider(15, ref yOffset, "Touch Strength", settings.TouchStrength, 1f, 50f);
            settings.SpringStrength = DrawSlider(15, ref yOffset, "Spring Strength", settings.SpringStrength, 10f, 150f);
            settings.NeighborSpringStrength = DrawSlider(15, ref yOffset, "Neighbor Spring", settings.NeighborSpringStrength, 5f, 100f);
            settings.Damping = DrawSlider(15, ref yOffset, "Damping", settings.Damping, 0.5f, 25f);
            settings.WobbleAmount = DrawSlider(15, ref yOffset, "Wobble Amount", settings.WobbleAmount, 0f, 3f);
            settings.MaxDisplacement = DrawSlider(15, ref yOffset, "Max Displacement", settings.MaxDisplacement, 0.02f, 0.3f);

            // --- DEVELOPMENT CHEAT BUTTONS ---
            if (GUI.Button(new Rect(15, yOffset, 140, 24), "Next Preset"))
            {
                if (matController != null && matProvider != null) CyclePresets(matController, matProvider);
            }
            if (GUI.Button(new Rect(165, yOffset, 140, 24), "Clear Decs"))
            {
                if (decCtrl != null) decCtrl.ClearAll();
            }
            yOffset += 26;

            if (GUI.Button(new Rect(15, yOffset, 140, 24), "Reset Book"))
            {
                if (bookCtrl != null) bookCtrl.ClearAll();
            }
            if (GUI.Button(new Rect(165, yOffset, 140, 24), "Force Event"))
            {
                // Force a mock discovery trigger
                if (bookCtrl != null)
                {
                    bookCtrl.RegisterDiscovery("event.fruit_pop", "strawberry");
                }
            }
            yOffset += 26;

            if (GUI.Button(new Rect(15, yOffset, 290, 24), "Reset Physics Mesh"))
            {
                targetSurface.ResetSurface();
            }
        }

        private void CyclePresets(IMaterialPresetController ctrl, IMaterialPresetProvider prov)
        {
            var list = prov.GetAll();
            if (list == null || list.Count == 0) return;

            int idx = -1;
            string currentId = ctrl.CurrentPreset != null ? ctrl.CurrentPreset.Id : string.Empty;

            for (int i = 0; i < list.Count; i++)
            {
                if (list[i].Id == currentId)
                {
                    idx = i;
                    break;
                }
            }

            int nextIdx = (idx + 1) % list.Count;
            ctrl.ApplyPreset(list[nextIdx].Id);
        }

        private int GetTouchCount()
        {
            var provider = targetSurface.GetComponent<ISquishyInputProvider>();
            return provider != null ? provider.ActiveTouchCount : 0;
        }

        private void DrawText(int x, int y, string label)
        {
            GUI.Label(new Rect(x, y, 300, 20), label);
        }

        private float DrawSlider(int x, ref int y, string label, float value, float min, float max)
        {
            _sb.Clear();
            _sb.Append(label).Append(": ").Append(value.ToString("F2"));
            GUI.Label(new Rect(x, y, 150, 20), _sb.ToString());
            float result = GUI.HorizontalSlider(new Rect(x + 150, y + 4, 140, 16), value, min, max);
            y += 24;
            return result;
        }
#endif
    }
}
