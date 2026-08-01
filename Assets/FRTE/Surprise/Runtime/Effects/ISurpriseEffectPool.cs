namespace FRTE.Surprise
{
    /// <summary>
    /// Contract for the Object Pool recycling surprise effect GameObjects.
    /// Prevents garbage allocation during high-frequency play interaction.
    /// </summary>
    public interface ISurpriseEffectPool
    {
        ISurpriseEffect Rent(string effectId);
        void Return(ISurpriseEffect effect);
        void Clear();
    }
}
