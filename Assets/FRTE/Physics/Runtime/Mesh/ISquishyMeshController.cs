using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Contract for generating and dynamically updating the 2D grid rendering mesh.
    /// Manages Vertex streams without allocating dynamic heap memory.
    /// </summary>
    public interface ISquishyMeshController
    {
        /// <summary>
        /// Gets the active dynamic Unity mesh instance.
        /// </summary>
        Mesh RuntimeMesh { get; }

        /// <summary>
        /// Allocates a new grid mesh buffer matching layout and density quality.
        /// </summary>
        /// <param name="settings">Config parameters specifying width, height, columns, rows.</param>
        void BuildMesh(SquishyMeshSettings settings);

        /// <summary>
        /// Commits deformed vertex positions back to the GPU mesh buffers in-place.
        /// </summary>
        void ApplyVertexPositions();

        /// <summary>
        /// Resets the mesh vertices back to original planar resting states.
        /// </summary>
        void ResetVertices();
    }
}
