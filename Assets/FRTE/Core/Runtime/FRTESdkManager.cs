using System;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Master coordinator for the FruitRabbit Touch Engine (FRTE) SDK.
    /// Bootstraps all plugins, exposes clean APIs, and integrates touch flows
    /// to make integration as simple as: Load Photo -> Touch -> Material -> Save.
    /// </summary>
    public sealed class FRTESdkManager : MonoBehaviour
    {
        private static FRTESdkManager _instance;

        /// <summary>
        /// Gets the singleton coordinator instance.
        /// </summary>
        public static FRTESdkManager Instance
        {
            get
            {
                if (_instance == null)
                {
                    var go = new GameObject("FRTE_SDK_Manager");
                    _instance = go.AddComponent<FRTESdkManager>();
                    DontDestroyOnLoad(go);
                }
                return _instance;
            }
        }

        private readonly FRTEContainer _container = new FRTEContainer();
        private readonly FRTEEventBus _eventBus = new FRTEEventBus();

        private bool _isInitialized;

        // Active plugin instances
        private IPlugin _photoPlugin;
        private IPlugin _aiPlugin;
        private IPlugin _physicsPlugin;
        private IPlugin _decorationPlugin;
        private IPlugin _exportPlugin;

        // Public Engine References
        public FRTEContainer Container => _container;
        public FRTEEventBus EventBus => _eventBus;

        private void Awake()
        {
            if (_instance != null && _instance != this)
            {
                Destroy(gameObject);
                return;
            }
            _instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeSDK();
        }

        /// <summary>
        /// Bootstraps the SDK, registers core sub-systems, and activates plugins.
        /// </summary>
        public void InitializeSDK()
        {
            if (_isInitialized) return;

            _container.Register<IAppModeController>(new AppModeController());

            // 1. Dynamic Assembly-decoupled plugin instantiation (using assembly references or direct instantiation for simplicity)
            // To ensure compatibility across Unity versions without reflection bottlenecks, we instantiate concrete types directly here.
            
            // Photo Engine (FRTE.Photo)
            _photoPlugin = InstantiatePlugin("FRTE.Photo.GPUPhotoManager");
            if (_photoPlugin == null)
            {
                // Fallback direct reference if reflection not preferred in strict IL2CPP builds
                _photoPlugin = new FRTE.Photo.GPUPhotoManager();
            }

            // AI Engine (FRTE.AI)
            _aiPlugin = InstantiatePlugin("FRTE.AI.MockAIDetectionProvider");
            if (_aiPlugin == null)
            {
                _aiPlugin = new FRTE.AI.MockAIDetectionProvider();
            }

            // Physics Engine (FRTE.Physics)
            _physicsPlugin = InstantiatePlugin("FRTE.Physics.SquishyPhysicsSolver");
            if (_physicsPlugin == null)
            {
                _physicsPlugin = new FRTE.Physics.SquishyPhysicsSolver();
            }

            // Decoration Engine (FRTE.Decoration)
            _decorationPlugin = InstantiatePlugin("FRTE.Decoration.DecorationManager");
            if (_decorationPlugin == null)
            {
                _decorationPlugin = new FRTE.Decoration.DecorationManager();
            }

            // Export Engine (FRTE.Export)
            _exportPlugin = InstantiatePlugin("FRTE.Export.AsyncExporter");
            if (_exportPlugin == null)
            {
                _exportPlugin = new FRTE.Export.AsyncExporter();
            }

            // 2. Initialize plugins with the DI Container
            _photoPlugin?.Initialize(_container);
            _aiPlugin?.Initialize(_container);
            _physicsPlugin?.Initialize(_container);
            _decorationPlugin?.Initialize(_container);
            _exportPlugin?.Initialize(_container);

            // 3. Enable all plugins by default
            _photoPlugin?.Enable();
            _aiPlugin?.Enable();
            _physicsPlugin?.Enable();
            _decorationPlugin?.Enable();
            _exportPlugin?.Enable();

            _isInitialized = true;
            Debug.Log("[FRTE] Core SDK Successfully Bootstrapped.");
        }

        private IPlugin InstantiatePlugin(string typeName)
        {
            try
            {
                var type = Type.GetType(typeName);
                if (type != null)
                {
                    return Activator.CreateInstance(type) as IPlugin;
                }
            }
            catch (Exception ex)
            {
                Debug.LogWarning($"[FRTE] Dynamic instantiation of '{typeName}' skipped (falling back to direct reference): {ex.Message}");
            }
            return null;
        }

        private void Update()
        {
            if (!_isInitialized) return;

            // Step the physics simulation loop
            if (_container.TryResolve<FRTE.Physics.ISquishyPhysicsEngine>(out var physics))
            {
                physics.StepSimulation(Time.deltaTime);
            }
        }

        /// <summary>
        /// Feeds screen-space touch coordinates into the physics solver.
        /// </summary>
        public void SetTouchInput(int id, Vector2 normalizedUV, TouchPhase phase, float pressure = 1.0f, float duration = 0.1f, float dragSpeed = 0f)
        {
            if (!_isInitialized) return;

            if (_container.TryResolve<FRTE.Physics.ISquishyPhysicsEngine>(out var physics))
            {
                physics.UpdateTouch(id, normalizedUV, phase, pressure, duration, dragSpeed);
            }
        }

        private void OnDestroy()
        {
            // Disable and release all plugin resources
            _photoPlugin?.Disable();
            _aiPlugin?.Disable();
            _physicsPlugin?.Disable();
            _decorationPlugin?.Disable();
            _exportPlugin?.Disable();

            _container.Clear();
            _eventBus.Clear();
            _isInitialized = false;
        }
    }
}
