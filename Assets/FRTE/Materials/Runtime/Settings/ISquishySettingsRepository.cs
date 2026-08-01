namespace FRTE.Materials
{
    /// <summary>
    /// Contract for saving, loading, and restoring local customization settings.
    /// </summary>
    public interface ISquishySettingsRepository
    {
        SquishyUserSettings Load();
        void Save(SquishyUserSettings settings);
        void Reset();
    }
}
