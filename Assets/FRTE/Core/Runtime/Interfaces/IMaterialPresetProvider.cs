using System.Collections.Generic;

namespace FRTE.Core
{
    /// <summary>
    /// Provider interface for querying available materials and resolving preset IDs.
    /// </summary>
    public interface IMaterialPresetProvider
    {
        IReadOnlyList<SquishyMaterialPreset> GetAll();
        bool TryGetById(string id, out SquishyMaterialPreset preset);
        SquishyMaterialPreset GetDefault();
    }
}
