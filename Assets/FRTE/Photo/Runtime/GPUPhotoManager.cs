using UnityEngine;
using FRTE.Core;

namespace FRTE.Photo
{
    /// <summary>
    /// GPU implementation of the Photo Engine. Modifies image coordinates
    /// on the GPU using affine matrices to maintain original resolution and avoid GC.
    /// </summary>
    public sealed class GPUPhotoManager : IPhotoEngine, IPlugin
    {
        private Texture2D _originalTexture;
        private RenderTexture _workingTexture;
        private Material _transformMaterial;

        // Cumulative transformation matrix mapping current coordinate system to the original texture UV
        private Matrix3x3 _cumulativeTransform = Matrix3x3.Identity;

        public string PluginId => "FRTE.PhotoEngine";
        public bool IsEnabled { get; private set; }

        public RenderTexture WorkingTexture => _workingTexture;
        public int OriginalWidth => _originalTexture != null ? _originalTexture.width : 0;
        public int OriginalHeight => _originalTexture != null ? _originalTexture.height : 0;

        public void Initialize(FRTEContainer container)
        {
            var shader = Shader.Find("Hidden/FRTE/PhotoTransform");
            if (shader == null)
            {
                Debug.LogError("[PhotoEngine] Failed to find PhotoTransform shader.");
                return;
            }
            _transformMaterial = new Material(shader);
            container.Register<IPhotoEngine>(this);
        }

        public void Enable()
        {
            IsEnabled = true;
        }

        public void Disable()
        {
            IsEnabled = false;
            ReleaseTextures();
            if (_transformMaterial != null)
            {
                Object.DestroyImmediate(_transformMaterial);
                _transformMaterial = null;
            }
        }

        public void LoadPhoto(Texture2D texture)
        {
            if (texture == null) return;

            _originalTexture = texture;
            _cumulativeTransform = Matrix3x3.Identity;

            // Re-allocate working texture at original size
            ReleaseTextures();
            _workingTexture = new RenderTexture(texture.width, texture.height, 0, RenderTextureFormat.ARGB32)
            {
                filterMode = FilterMode.Bilinear,
                wrapMode = TextureWrapMode.Clamp
            };
            _workingTexture.Create();

            // Direct copy
            Graphics.Blit(texture, _workingTexture);
        }

        public void Crop(Rect normalizedRect)
        {
            if (_originalTexture == null || _workingTexture == null) return;

            // 1. Calculate Crop matrix mapping new coordinates [0, 1] to old coordinates
            float cropX = normalizedRect.x;
            float cropY = normalizedRect.y;
            float cropW = normalizedRect.width;
            float cropH = normalizedRect.height;

            Matrix3x3 cropMatrix = new Matrix3x3(
                cropW, 0, cropX,
                0, cropH, cropY,
                0, 0, 1
            );

            // Accumulate
            _cumulativeTransform = _cumulativeTransform * cropMatrix;

            // 2. Perform GPU Blit to update WorkingTexture
            ApplyTransform();
        }

        public void Rotate(float angleDegrees)
        {
            if (_originalTexture == null || _workingTexture == null) return;

            // 1. Calculate Rotation matrix (rotation around center 0.5, 0.5)
            float rad = angleDegrees * Mathf.Deg2Rad;
            float c = Mathf.Cos(rad);
            float s = Mathf.Sin(rad);

            Matrix3x3 rotMatrix = new Matrix3x3(
                c, -s, 0.5f - 0.5f * c + 0.5f * s,
                s, c, 0.5f - 0.5f * s - 0.5f * c,
                0, 0, 1
            );

            // Accumulate
            _cumulativeTransform = _cumulativeTransform * rotMatrix;

            // 2. Perform GPU Blit to update WorkingTexture
            ApplyTransform();
        }

        public void Scale(Vector2 scale)
        {
            if (_originalTexture == null || _workingTexture == null) return;

            // Ensure scale values are non-zero to avoid division by zero
            float sx = Mathf.Abs(scale.x) < 0.001f ? 0.001f : scale.x;
            float sy = Mathf.Abs(scale.y) < 0.001f ? 0.001f : scale.y;

            // 1. Calculate Scale matrix (scaling around center 0.5, 0.5)
            Matrix3x3 scaleMatrix = new Matrix3x3(
                1f / sx, 0, 0.5f - 0.5f / sx,
                0, 1f / sy, 0.5f - 0.5f / sy,
                0, 0, 1
            );

            // Accumulate
            _cumulativeTransform = _cumulativeTransform * scaleMatrix;

            // 2. Perform GPU Blit to update WorkingTexture
            ApplyTransform();
        }

        public void Reset()
        {
            if (_originalTexture == null) return;
            _cumulativeTransform = Matrix3x3.Identity;
            ApplyTransform();
        }

        private void ApplyTransform()
        {
            if (_originalTexture == null || _workingTexture == null || _transformMaterial == null) return;

            // Temporary RenderTexture to write to
            RenderTexture temp = RenderTexture.GetTemporary(_workingTexture.width, _workingTexture.height, 0, _workingTexture.format);
            temp.filterMode = FilterMode.Bilinear;
            temp.wrapMode = TextureWrapMode.Clamp;

            // Pass matrices to shader
            _transformMaterial.SetVector("_TransformRow0", new Vector4(_cumulativeTransform.m00, _cumulativeTransform.m01, _cumulativeTransform.m02, 0));
            _transformMaterial.SetVector("_TransformRow1", new Vector4(_cumulativeTransform.m10, _cumulativeTransform.m11, _cumulativeTransform.m12, 0));

            // Execute Blit: original -> temp via shader
            Graphics.Blit(_originalTexture, temp, _transformMaterial);

            // Blit back to working texture
            Graphics.Blit(temp, _workingTexture);

            RenderTexture.ReleaseTemporary(temp);
        }

        private void ReleaseTextures()
        {
            if (_workingTexture != null)
            {
                _workingTexture.Release();
                Object.DestroyImmediate(_workingTexture);
                _workingTexture = null;
            }
        }

        /// <summary>
        /// Inline 3x3 Matrix helper to represent 2D affine transformations.
        /// </summary>
        private struct Matrix3x3
        {
            public float m00, m01, m02;
            public float m10, m11, m12;
            public float m20, m21, m22;

            public Matrix3x3(float m00, float m01, float m02, float m10, float m11, float m12, float m20, float m21, float m22)
            {
                this.m00 = m00; this.m01 = m01; this.m02 = m02;
                this.m10 = m10; this.m11 = m11; this.m12 = m12;
                this.m20 = m20; this.m21 = m21; this.m22 = m22;
            }

            public static Matrix3x3 Identity => new Matrix3x3(
                1, 0, 0,
                0, 1, 0,
                0, 0, 1
            );

            public static Matrix3x3 operator *(Matrix3x3 a, Matrix3x3 b)
            {
                return new Matrix3x3(
                    a.m00 * b.m00 + a.m01 * b.m10 + a.m02 * b.m20,
                    a.m00 * b.m01 + a.m01 * b.m11 + a.m02 * b.m21,
                    a.m00 * b.m02 + a.m01 * b.m12 + a.m02 * b.m22,

                    a.m10 * b.m00 + a.m11 * b.m10 + a.m12 * b.m20,
                    a.m10 * b.m01 + a.m11 * b.m11 + a.m12 * b.m21,
                    a.m10 * b.m02 + a.m11 * b.m12 + a.m12 * b.m22,

                    a.m20 * b.m00 + a.m21 * b.m10 + a.m22 * b.m20,
                    a.m20 * b.m01 + a.m21 * b.m11 + a.m22 * b.m21,
                    a.m20 * b.m02 + a.m21 * b.m12 + a.m22 * b.m22
                );
            }
        }
    }
}
