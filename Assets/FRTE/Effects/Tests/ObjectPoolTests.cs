using NUnit.Framework;
using UnityEngine;

namespace FRTE.Effects.Tests
{
    [TestFixture]
    public class ObjectPoolTests
    {
        private class PooledObject
        {
            public bool IsActive;
        }

        [Test]
        public void Pool_InitializesWithCorrectCapacity()
        {
            int capacity = 10;
            var pool = new FRTEObjectPool<PooledObject>(
                createFunc: () => new PooledObject(),
                onGet: obj => obj.IsActive = true,
                onRelease: obj => obj.IsActive = false,
                initialCapacity: capacity
            );

            Assert.AreEqual(capacity, pool.CountInactive);
        }

        [Test]
        public void Pool_GetsAndReleasesObjectsCorrectly()
        {
            var pool = new FRTEObjectPool<PooledObject>(
                createFunc: () => new PooledObject(),
                onGet: obj => obj.IsActive = true,
                onRelease: obj => obj.IsActive = false,
                initialCapacity: 5
            );

            var obj = pool.Get();
            Assert.IsTrue(obj.IsActive);
            Assert.AreEqual(4, pool.CountInactive);

            pool.Release(obj);
            Assert.IsFalse(obj.IsActive);
            Assert.AreEqual(5, pool.CountInactive);
        }
    }
}
