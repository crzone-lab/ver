using System.Threading;
using System.Threading.Tasks;
using UnityEngine;
using FRTE.Core;

namespace FRTE.AI
{
    /// <summary>
    /// Mock implementation of ISubjectMaskProvider for local serverless execution.
    /// Implements specific rules:
    /// - Real human photos: crops/masks face only.
    /// - Drawings/illustrations: crops/masks entire character body.
    /// </summary>
    public sealed class MockSubjectMaskProvider : ISubjectMaskProvider
    {
        public bool IsAvailable => true;

        public async Task<SubjectMaskResult> CreateMaskAsync(Texture2D source, CancellationToken cancellationToken)
        {
            // Simulate local processing delay (e.g. 200ms)
            await Task.Delay(200, cancellationToken);

            if (source == null)
            {
                return new SubjectMaskResult
                {
                    MaskedTexture = null,
                    BoundaryRect = Rect.zero,
                    IsIllustration = false
                };
            }

            // Detect if illustration/drawing based on name
            bool isIllust = source.name.Contains("illust") || 
                             source.name.Contains("drawing") || 
                             source.name.Contains("character") || 
                             source.name.Contains("cartoon");

            Rect boundary;
            Texture2D maskedTex;

            if (isIllust)
            {
                // ILLUSTRATION: Extract full body (mocked as full texture area)
                boundary = new Rect(0, 0, source.width, source.height);
                maskedTex = CloneTexturePart(source, boundary);
            }
            else
            {
                // HUMAN: Extract face area only (mocked as center 50% area)
                float fw = source.width * 0.5f;
                float fh = source.height * 0.5f;
                boundary = new Rect(source.width * 0.25f, source.height * 0.25f, fw, fh);
                maskedTex = CloneTexturePart(source, boundary);
            }

            maskedTex.name = source.name + "_masked";

            return new SubjectMaskResult
            {
                MaskedTexture = maskedTex,
                BoundaryRect = boundary,
                IsIllustration = isIllust
            };
        }

        private Texture2D CloneTexturePart(Texture2D source, Rect rect)
        {
            int x = Mathf.RoundToInt(rect.x);
            int y = Mathf.RoundToInt(rect.y);
            int w = Mathf.RoundToInt(rect.width);
            int h = Mathf.RoundToInt(rect.height);

            // Sane clamps
            x = Mathf.Clamp(x, 0, source.width - 1);
            y = Mathf.Clamp(y, 0, source.height - 1);
            w = Mathf.Clamp(w, 1, source.width - x);
            h = Mathf.Clamp(h, 1, source.height - y);

            var dest = new Texture2D(w, h, source.format, false);
            try
            {
                var pixels = source.GetPixels(x, y, w, h);
                dest.SetPixels(pixels);
                dest.Apply();
            }
            catch
            {
                // Fallback copy if formats are mismatch / unreadable
                for (int cy = 0; cy < h; cy++)
                {
                    for (int cx = 0; cx < w; cx++)
                    {
                        dest.SetPixel(cx, cy, Color.magenta);
                    }
                }
                dest.Apply();
            }
            return dest;
        }
    }
}
