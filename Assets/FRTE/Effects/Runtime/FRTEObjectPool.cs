using System;
using System.Collections.Generic;
using UnityEngine;

namespace FRTE.Effects
{
    /// <summary>
    /// Generic, zero-allocation object pool utility to recycle instances and avoid runtime GC spikes.
    /// </summary>
    /// <typeparam name="T">Type of object to pool.</typeparam>
    public class FRTEObjectPool<T> where T : class
    {
        private readonly Stack<T> _pool;
        private readonly Func<T> _createFunc;
        private readonly Action<T> _onGet;
        private readonly Action<T> _onRelease;

        public int CountInactive => _pool.Count;

        public FRTEObjectPool(Func<T> createFunc, Action<T> onGet = null, Action<T> onRelease = null, int initialCapacity = 16)
        {
            _createFunc = createFunc ?? throw new ArgumentNullException(nameof(createFunc));
            _onGet = onGet;
            _onRelease = onRelease;
            _pool = new Stack<T>(initialCapacity);

            for (int i = 0; i < initialCapacity; i++)
            {
                _pool.Push(_createFunc());
            }
        }

        /// <summary>
        /// Retrieves an item from the pool. Creates a new one if the pool is empty.
        /// </summary>
        public T Get()
        {
            T element = _pool.Count == 0 ? _createFunc() : _pool.Pop();
            _onGet?.Invoke(element);
            return element;
        }

        /// <summary>
        /// Returns an item back to the pool to be recycled.
        /// </summary>
        public void Release(T element)
        {
            if (element == null) return;
            _onRelease?.Invoke(element);
            _pool.Push(element);
        }

        /// <summary>
        /// Clears the pool.
        /// </summary>
        public void Clear()
        {
            _pool.Clear();
        }
    }

    /// <summary>
    /// GameObject-specific wrapper for object pooling, managing instantiation and active states.
    /// </summary>
    public sealed class FRTEGameObjectPool
    {
        private readonly GameObject _prefab;
        private readonly Transform _parent;
        private readonly FRTEObjectPool<GameObject> _internalPool;

        public FRTEGameObjectPool(GameObject prefab, Transform parent = null, int initialCapacity = 16)
        {
            _prefab = prefab;
            _parent = parent;
            _internalPool = new FRTEObjectPool<GameObject>(CreateNewInstance, OnGet, OnRelease, initialCapacity);
        }

        private GameObject CreateNewInstance()
        {
            var go = UnityEngine.Object.Instantiate(_prefab, _parent);
            go.SetActive(false);
            return go;
        }

        private void OnGet(GameObject go)
        {
            go.SetActive(true);
        }

        private void OnRelease(GameObject go)
        {
            go.SetActive(false);
        }

        public GameObject Get() => _internalPool.Get();
        public void Release(GameObject go) => _internalPool.Release(go);
        public void Clear() => _internalPool.Clear();
    }
}
