using System;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Holds structural landmark points of a detected face.
    /// Normalized coordinates in [0.0 - 1.0] range relative to the photo rect.
    /// </summary>
    [Serializable]
    public struct FaceLandmarkData
    {
        public Vector2 FaceCenter;
        public Vector2 LeftEye;
        public Vector2 RightEye;
        public Vector2 LeftCheek;
        public Vector2 RightCheek;
        public Vector2 Chin;
        public Vector2 Forehead;
        public Vector2 HeadTop;
        public float FaceRotation;
        public float FaceWidth;
        public float FaceHeight;
    }
}
