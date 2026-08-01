using NUnit.Framework;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Collection.Tests
{
    [TestFixture]
    public sealed class CollectionEditModeTests
    {
        private CollectionRepository _repository;

        [SetUp]
        public void SetUp()
        {
            _repository = new CollectionRepository();
            _repository.Reset();
        }

        [TearDown]
        public void TearDown()
        {
            _repository.Reset();
        }

        [Test]
        public void Controller_FirstDiscovery_RegistersCorrectValues()
        {
            var controller = new CollectionController(_repository);

            // Register first discovery
            controller.RegisterDiscovery("event.fruit_pop", "strawberry");

            Assert.IsTrue(controller.IsDiscovered("event.fruit_pop"));
            var entries = controller.GetEntries();
            Assert.AreEqual(1, entries.Count);
            Assert.AreEqual(1, entries[0].DiscoveryCount);
            Assert.IsNotEmpty(entries[0].FirstDiscoveredUtc);

            // Register repeat discovery
            controller.RegisterDiscovery("event.fruit_pop", "strawberry");
            Assert.AreEqual(2, entries[0].DiscoveryCount);
        }

        [Test]
        public void Repository_CorruptJson_RestoresDefaults()
        {
            PlayerPrefs.SetString("FRTE_SquishyCollectionBook", "{invalid_json_text_here");
            PlayerPrefs.Save();

            var data = _repository.Load();
            Assert.IsNotNull(data);
            Assert.AreEqual(0, data.Entries.Count);
        }
    }
}
