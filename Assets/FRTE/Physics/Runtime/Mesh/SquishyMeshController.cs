using UnityEngine;

namespace FRTE.Physics
{
    /// <summary>
    /// Component managing the creation and update of the deformable 2D quad mesh.
    /// Reuse buffers in-place to ensure zero runtime garbage collection.
    /// </summary>
    public sealed class SquishyMeshController : MonoBehaviour, ISquishyMeshController
    {
        private Mesh _runtimeMesh;
        private Vector3[] _vertices;
        private Vector2[] _uvs;
        private int[] _triangles;

        private float _meshWidth;
        private float _meshHeight;
        private int _columns;
        private int _rows;

        // Reference to the active simulation solver to query deformed states
        private SquishySimulation _simulation;

        /// <summary>
        /// Gets the active dynamic Unity mesh instance.
        /// </summary>
        public Mesh RuntimeMesh => _runtimeMesh;

        private void Awake()
        {
            _runtimeMesh = new Mesh
            {
                name = "FRTE_SquishyMesh"
            };
            _runtimeMesh.MarkDynamic();
        }

        /// <summary>
        /// Connects the mesh controller to the active physical simulation grid.
        /// </summary>
        public void LinkSimulation(SquishySimulation simulation)
        {
            _simulation = simulation;
        }

        public void BuildMesh(SquishyMeshSettings settings)
        {
            _meshWidth = settings.Width;
            _meshHeight = settings.Height;
            _columns = settings.Columns;
            _rows = settings.Rows;

            int count = _columns * _rows;

            // Reuse arrays if sizes haven't changed, preventing heap allocations
            if (_vertices == null || _vertices.Length != count)
            {
                _vertices = new Vector3[count];
                _uvs = new Vector2[count];
            }

            int numTriangles = (_columns - 1) * (_rows - 1) * 6;
            if (_triangles == null || _triangles.Length != numTriangles)
            {
                _triangles = new int[numTriangles];
            }

            // 1. Build planar vertex coordinates and UV mapping
            for (int y = 0; y < _rows; y++)
            {
                for (int x = 0; x < _columns; x++)
                {
                    int index = y * _columns + x;
                    float u = (float)x / (_columns - 1);
                    float v = (float)y / (_rows - 1);

                    // Center-aligned coordinates in local mesh space
                    _vertices[index] = new Vector3((u - 0.5f) * _meshWidth, (v - 0.5f) * _meshHeight, 0f);
                    _uvs[index] = new Vector2(u, v);
                }
            }

            // 2. Build index buffer (Triangle list topology)
            int triIndex = 0;
            for (int y = 0; y < _rows - 1; y++)
            {
                for (int x = 0; x < _columns - 1; x++)
                {
                    int botLeft = y * _columns + x;
                    int botRight = botLeft + 1;
                    int topLeft = (y + 1) * _columns + x;
                    int topRight = topLeft + 1;

                    _triangles[triIndex++] = botLeft;
                    _triangles[triIndex++] = topLeft;
                    _triangles[triIndex++] = botRight;

                    _triangles[triIndex++] = botRight;
                    _triangles[triIndex++] = topLeft;
                    _triangles[triIndex++] = topRight;
                }
            }

            _runtimeMesh.Clear();
            _runtimeMesh.vertices = _vertices;
            _runtimeMesh.uv = _uvs;
            _runtimeMesh.triangles = _triangles;
            _runtimeMesh.RecalculateNormals();
            _runtimeMesh.RecalculateBounds();
        }

        public void ApplyVertexPositions()
        {
            if (_simulation == null || _vertices == null) return;

            var simVertices = _simulation.Vertices;
            if (simVertices == null || simVertices.Length != _vertices.Length) return;

            int count = _vertices.Length;
            for (int i = 0; i < count; i++)
            {
                Vector3 simPos = simVertices[i].CurrentPosition;

                // Map simulation UV coordinates [-0.5, 0.5] back to local mesh scale units
                _vertices[i].x = simPos.x * _meshWidth;
                _vertices[i].y = simPos.y * _meshHeight;
                _vertices[i].z = simPos.z * 1.5f; // scale factor for visual depth
            }

            _runtimeMesh.vertices = _vertices;
            _runtimeMesh.RecalculateNormals();
            _runtimeMesh.RecalculateBounds();
        }

        public void ResetVertices()
        {
            if (_vertices == null) return;

            int count = _vertices.Length;
            for (int y = 0; y < _rows; y++)
            {
                for (int x = 0; x < _columns; x++)
                {
                    int index = y * _columns + x;
                    float u = (float)x / (_columns - 1);
                    float v = (float)y / (_rows - 1);

                    _vertices[index] = new Vector3((u - 0.5f) * _meshWidth, (v - 0.5f) * _meshHeight, 0f);
                }
            }

            _runtimeMesh.vertices = _vertices;
            _runtimeMesh.RecalculateNormals();
            _runtimeMesh.RecalculateBounds();
        }

        private void OnDestroy()
        {
            if (_runtimeMesh != null)
            {
                DestroyImmediate(_runtimeMesh);
                _runtimeMesh = null;
            }
        }
    }
}
