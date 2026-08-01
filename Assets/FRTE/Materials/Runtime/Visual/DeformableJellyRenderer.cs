using UnityEngine;

namespace FRTE.Materials
{
    /// <summary>
    /// Updates the mesh shader visual attributes using MaterialPropertyBlock.
    /// Avoids creating runtime duplicate material instances to prevent memory leaks.
    /// </summary>
    [RequireComponent(typeof(Renderer))]
    public sealed class DeformableJellyRenderer : MonoBehaviour
    {
        private Renderer _renderer;
        private MaterialPropertyBlock _propBlock;

        private static readonly int HighlightProp = Shader.PropertyToID("_HighlightStrength");
        private static readonly int GlossinessProp = Shader.PropertyToID("_Glossiness");
        private static readonly int RimProp = Shader.PropertyToID("_RimStrength");
        private static readonly int TransparencyProp = Shader.PropertyToID("_TransparencyEffect");
        private static readonly int RefractionProp = Shader.PropertyToID("_RefractionStrength");
        private static readonly int SaturationProp = Shader.PropertyToID("_SaturationMultiplier");
        private static readonly int BrightnessProp = Shader.PropertyToID("_BrightnessMultiplier");
        private static readonly int OverlayOpacityProp = Shader.PropertyToID("_OverlayOpacity");

        private void Awake()
        {
            _renderer = GetComponent<Renderer>();
            _propBlock = new MaterialPropertyBlock();
        }

        /// <summary>
        /// Commits the preset's visual values to the renderer using a MaterialPropertyBlock.
        /// </summary>
        public void ApplyVisuals(SquishyVisualParameters visual, bool effectsEnabled)
        {
            if (_renderer == null || _propBlock == null) return;

            _renderer.GetPropertyBlock(_propBlock);

            if (effectsEnabled)
            {
                _propBlock.SetFloat(HighlightProp, visual.HighlightStrength);
                _propBlock.SetFloat(GlossinessProp, visual.Glossiness);
                _propBlock.SetFloat(RimProp, visual.RimStrength);
                _propBlock.SetFloat(TransparencyProp, visual.TransparencyEffect);
                _propBlock.SetFloat(RefractionProp, visual.RefractionStrength);
                _propBlock.SetFloat(SaturationProp, visual.SaturationMultiplier);
                _propBlock.SetFloat(BrightnessProp, visual.BrightnessMultiplier);
                _propBlock.SetFloat(OverlayOpacityProp, visual.OverlayOpacity);
            }
            else
            {
                // Reset to standard fallback values (no visual distort overlays)
                _propBlock.SetFloat(HighlightProp, 0f);
                _propBlock.SetFloat(GlossinessProp, 0.5f);
                _propBlock.SetFloat(RimProp, 0f);
                _propBlock.SetFloat(TransparencyProp, 0f);
                _propBlock.SetFloat(RefractionProp, 0f);
                _propBlock.SetFloat(SaturationProp, 1f);
                _propBlock.SetFloat(BrightnessProp, 1f);
                _propBlock.SetFloat(OverlayOpacityProp, 0f);
            }

            _renderer.SetPropertyBlock(_propBlock);
        }
    }
}
