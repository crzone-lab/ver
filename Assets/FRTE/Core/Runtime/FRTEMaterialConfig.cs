using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// ScriptableObject defining physical and visual characteristics of a deformable material.
    /// Presets like Jelly, Mochi, Slime, Pudding, and Rubber can be created as project assets.
    /// </summary>
    [CreateAssetMenu(fileName = "NewMaterialConfig", menuName = "FRTE/Material Config", order = 120)]
    public sealed class FRTEMaterialConfig : ScriptableObject
    {
        [Header("Elastic Properties")]
        [Tooltip("Stiffness of the springs (k). Higher values return to shape faster with more force.")]
        [Range(1f, 200f)]
        public float elasticity = 40f;

        [Tooltip("Resistance to stretch. Limits how far the mesh can deform under touch pressure.")]
        [Range(0.1f, 5f)]
        public float stretchLimit = 1.5f;

        [Header("Viscous Properties")]
        [Tooltip("Damping resistance (c). Higher values slow down oscillations quickly (less wobbling).")]
        [Range(0.1f, 50f)]
        public float viscosity = 5f;

        [Tooltip("The speed at which the material recovers after touch release.")]
        [Range(0.1f, 10f)]
        public float recoverySpeed = 2f;

        [Header("Secondary Motion & Bounce")]
        [Tooltip("Overshoot amplitude scaling. Controls secondary wobbling size.")]
        [Range(0f, 2f)]
        public float bounce = 0.8f;

        [Tooltip("Deceleration rate of the wobble oscillation.")]
        [Range(0.01f, 1f)]
        public float damping = 0.15f;

        [Header("Surface Noise (Slime Effect)")]
        [Tooltip("Frequency of irregular surface wobbling noise.")]
        [Range(0f, 20f)]
        public float noiseFrequency = 0f;

        [Tooltip("Amplitude of irregular surface wobbling noise.")]
        [Range(0f, 0.5f)]
        public float noiseAmplitude = 0f;

        public static FRTEMaterialConfig CreateJelly()
        {
            var config = CreateInstance<FRTEMaterialConfig>();
            config.elasticity = 50f;
            config.stretchLimit = 1.2f;
            config.viscosity = 3.5f;
            config.recoverySpeed = 3f;
            config.bounce = 0.9f;
            config.damping = 0.1f;
            return config;
        }

        public static FRTEMaterialConfig CreateSlime()
        {
            var config = CreateInstance<FRTEMaterialConfig>();
            config.elasticity = 15f;
            config.stretchLimit = 2.5f;
            config.viscosity = 15f;
            config.recoverySpeed = 0.8f;
            config.bounce = 0.1f;
            config.damping = 0.6f;
            config.noiseFrequency = 8f;
            config.noiseAmplitude = 0.08f;
            return config;
        }

        public static FRTEMaterialConfig CreatePudding()
        {
            var config = CreateInstance<FRTEMaterialConfig>();
            config.elasticity = 30f;
            config.stretchLimit = 1.8f;
            config.viscosity = 2f;
            config.recoverySpeed = 4f;
            config.bounce = 1.4f;
            config.damping = 0.05f;
            return config;
        }

        public static FRTEMaterialConfig CreateMochi()
        {
            var config = CreateInstance<FRTEMaterialConfig>();
            config.elasticity = 80f;
            config.stretchLimit = 0.6f;
            config.viscosity = 25f;
            config.recoverySpeed = 1.5f;
            config.bounce = 0.2f;
            config.damping = 0.4f;
            return config;
        }
    }
}
