using System;
using System.Collections.Generic;

namespace FRTE.Core
{
    /// <summary>
    /// A decoupled, type-safe, and GC-free Event Bus for high-performance messaging between FRTE modules.
    /// Uses specialized handlers to prevent parameter boxing and runtime allocations.
    /// </summary>
    public sealed class FRTEEventBus
    {
        private interface ISubscriptionList
        {
            void Clear();
        }

        private sealed class SubscriptionList<TEvent> : ISubscriptionList
        {
            private readonly List<Action<TEvent>> _handlers = new List<Action<TEvent>>(16);
            private readonly List<Action<TEvent>> _toRemove = new List<Action<TEvent>>(4);
            private bool _isPublishing;

            public void Add(Action<TEvent> handler)
            {
                if (handler == null) return;
                if (!_handlers.Contains(handler))
                {
                    _handlers.Add(handler);
                }
            }

            public void Remove(Action<TEvent> handler)
            {
                if (handler == null) return;
                if (_isPublishing)
                {
                    _toRemove.Add(handler);
                }
                else
                {
                    _handlers.Remove(handler);
                }
            }

            public void Publish(TEvent eventData)
            {
                _isPublishing = true;
                try
                {
                    int count = _handlers.Count;
                    for (int i = 0; i < count; i++)
                    {
                        _handlers[i]?.Invoke(eventData);
                    }
                }
                finally
                {
                    _isPublishing = false;
                    if (_toRemove.Count > 0)
                    {
                        for (int i = 0; i < _toRemove.Count; i++)
                        {
                            _handlers.Remove(_toRemove[i]);
                        }
                        _toRemove.Clear();
                    }
                }
            }

            public void Clear()
            {
                _handlers.Clear();
                _toRemove.Clear();
            }
        }

        private readonly Dictionary<Type, ISubscriptionList> _subscribers = new Dictionary<Type, ISubscriptionList>();

        /// <summary>
        /// Subscribes a listener to a specific event type.
        /// </summary>
        /// <typeparam name="TEvent">The type of the event.</typeparam>
        /// <param name="handler">The delegate action to invoke on event publication.</param>
        public void Subscribe<TEvent>(Action<TEvent> handler)
        {
            var type = typeof(TEvent);
            if (!_subscribers.TryGetValue(type, out var list))
            {
                list = new SubscriptionList<TEvent>();
                _subscribers.Add(type, list);
            }
            ((SubscriptionList<TEvent>)list).Add(handler);
        }

        /// <summary>
        /// Unsubscribes a listener from a specific event type.
        /// </summary>
        /// <typeparam name="TEvent">The type of the event.</typeparam>
        /// <param name="handler">The delegate action to remove.</param>
        public void Unsubscribe<TEvent>(Action<TEvent> handler)
        {
            var type = typeof(TEvent);
            if (_subscribers.TryGetValue(type, out var list))
            {
                ((SubscriptionList<TEvent>)list).Remove(handler);
            }
        }

        /// <summary>
        /// Publishes an event to all subscribed listeners.
        /// Executes without allocating GC memory if the event is a struct/class passed by value.
        /// </summary>
        /// <typeparam name="TEvent">The type of the event.</typeparam>
        /// <param name="eventData">The event arguments payload.</param>
        public void Publish<TEvent>(TEvent eventData)
        {
            var type = typeof(TEvent);
            if (_subscribers.TryGetValue(type, out var list))
            {
                ((SubscriptionList<TEvent>)list).Publish(eventData);
            }
        }

        /// <summary>
        /// Clears all event subscriptions.
        /// </summary>
        public void Clear()
        {
            foreach (var list in _subscribers.Values)
            {
                list.Clear();
            }
            _subscribers.Clear();
        }
    }
}
