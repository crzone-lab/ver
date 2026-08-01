namespace FRTE.Collection
{
    /// <summary>
    /// Contract for loading and saving discovered event collections book.
    /// </summary>
    public interface ICollectionRepository
    {
        CollectionSaveData Load();
        void Save(CollectionSaveData data);
        void Reset();
    }
}
