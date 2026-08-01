using System.Threading;
using System.Threading.Tasks;
using UnityEngine;

namespace FRTE.Core
{
    /// <summary>
    /// Contract for subject extraction masking.
    /// Supports distinguishing between real humans (face-only extraction) and drawings (full-body character extraction).
    /// </summary>
    public interface ISubjectMaskProvider
    {
        /// <summary>
        /// Gets if masking is supported.
        /// </summary>
        bool IsAvailable { get; }

        /// <summary>
        /// Runs async background removal and subject extraction.
        /// </summary>
        Task<SubjectMaskResult> CreateMaskAsync(Texture2D source, CancellationToken cancellationToken);
    }
}
