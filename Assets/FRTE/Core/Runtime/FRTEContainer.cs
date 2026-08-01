using System;
using System.Collections.Generic;

namespace FRTE.Core
{
    /// <summary>
    /// A lightweight, GC-free Service Locator/Dependency Injection container for the FRTE Core SDK.
    /// Provides decoupled interface resolution across independent modules.
    /// </summary>
    public sealed class FRTEContainer
    {
        private readonly Dictionary<Type, object> _registrations = new Dictionary<Type, object>();

        /// <summary>
        /// Registers an instance as the implementation of a specific service interface.
        /// </summary>
        /// <typeparam name="TService">The service interface type.</typeparam>
        /// <param name="implementation">The implementation instance.</param>
        public void Register<TService>(TService implementation) where TService : class
        {
            var type = typeof(TService);
            if (_registrations.ContainsKey(type))
            {
                _registrations[type] = implementation;
            }
            else
            {
                _registrations.Add(type, implementation);
            }
        }

        /// <summary>
        /// Unregisters a registered service interface implementation.
        /// </summary>
        /// <typeparam name="TService">The service interface type to remove.</typeparam>
        public void Unregister<TService>() where TService : class
        {
            var type = typeof(TService);
            _registrations.Remove(type);
        }

        /// <summary>
        /// Resolves the registered implementation for the specified service interface.
        /// Throws an exception if the service is not registered.
        /// </summary>
        /// <typeparam name="TService">The service interface type to resolve.</typeparam>
        /// <returns>The registered implementation instance.</returns>
        public TService Resolve<TService>() where TService : class
        {
            var type = typeof(TService);
            if (_registrations.TryGetValue(type, out var obj))
            {
                return obj as TService;
            }
            throw new InvalidOperationException($"Service of type '{type.FullName}' is not registered in FRTEContainer.");
        }

        /// <summary>
        /// Attempts to resolve the service interface, returning true if successful.
        /// </summary>
        /// <typeparam name="TService">The service interface type.</typeparam>
        /// <param name="service">The resolved implementation instance (null if failed).</param>
        /// <returns>True if the service was resolved, false otherwise.</returns>
        public bool TryResolve<TService>(out TService service) where TService : class
        {
            var type = typeof(TService);
            if (_registrations.TryGetValue(type, out var obj))
            {
                service = obj as TService;
                return true;
            }
            service = null;
            return false;
        }

        /// <summary>
        /// Clears all registered services from the container.
        /// </summary>
        public void Clear()
        {
            _registrations.Clear();
        }
    }
}
