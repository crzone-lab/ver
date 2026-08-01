using System.Collections.Generic;
using FRTE.Core;

namespace FRTE.Decoration
{
    /// <summary>
    /// Contract for querying registered decoration accessory assets.
    /// </summary>
    public interface IDecorationPresetProvider
    {
        IReadOnlyList<DecorationPreset> GetAll();
        IReadOnlyList<DecorationPreset> GetByCategory(DecorationCategory category);
        bool TryGetById(string id, out DecorationPreset preset);
    }
}
