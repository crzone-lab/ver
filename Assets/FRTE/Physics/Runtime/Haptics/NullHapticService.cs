using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Fallback haptic adapter that ignores vibration commands.
    /// Used inside the Unity Editor or on devices lacking haptic hardware.
    /// </summary>
    public sealed class NullHapticService : IHapticService
    {
        public void PlayLight()
        {
            // Fallback: log in debug mode or do nothing
#if UNITY_EDITOR
            Debug.Log("[Haptics] Light feedback triggered.");
#endif
        }

        public void PlayMedium()
        {
#if UNITY_EDITOR
            Debug.Log("[Haptics] Medium feedback triggered.");
#endif
        }

        public void PlayStrong()
        {
#if UNITY_EDITOR
            Debug.Log("[Haptics] Strong feedback triggered.");
#endif
        }
    }
}
