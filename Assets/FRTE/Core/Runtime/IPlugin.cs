namespace FRTE.Core
{
    /// <summary>
    /// Base interface for all FruitRabbit Touch Engine modular plugins.
    /// Supports dynamic ON/OFF runtime lifecycle switching.
    /// </summary>
    public interface IPlugin
    {
        /// <summary>
        /// Gets the unique identifier of the plugin.
        /// </summary>
        string PluginId { get; }

        /// <summary>
        /// Gets a value indicating whether the plugin is currently enabled.
        /// </summary>
        bool IsEnabled { get; }

        /// <summary>
        /// Initializes the plugin with the SDK's dependency container.
        /// </summary>
        /// <param name="container">The core dependency injection container.</param>
        void Initialize(FRTEContainer container);

        /// <summary>
        /// Enables the plugin module.
        /// </summary>
        void Enable();

        /// <summary>
        /// Disables the plugin module, cleaning up any active resources.
        /// </summary>
        void Disable();
    }
}
