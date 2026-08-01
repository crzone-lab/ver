using System;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Holds the result of a subject background masking extraction.
    /// </summary>
    [Serializable]
    public struct SubjectMaskResult
    {
        /// <summary>
        /// Extracted subject texture (background is alpha zero).
        /// </summary>
        public Texture2D MaskedTexture;

        /// <summary>
        /// Pixel boundary rectangle of the extracted subject.
        /// </summary>
        public Rect BoundaryRect;

        /// <summary>
        /// True if detected as an illustration/drawing (triggers full character crop).
        /// False if detected as a real human (triggers face-only crop).
        /// </summary>
        public bool IsIllustration;
    }
}
