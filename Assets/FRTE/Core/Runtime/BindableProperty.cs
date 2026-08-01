using System;
using System.Collections.Generic;

namespace FRTE.Core
{
    /// <summary>
    /// A lightweight binding class supporting MVVM communication.
    /// Alerts listeners of changes in property value with zero allocation where possible.
    /// </summary>
    /// <typeparam name="T">The type of the bound value.</typeparam>
    public sealed class BindableProperty<T>
    {
        private T _value;
        private Action<T> _onValueChanged;

        /// <summary>
        /// Gets or sets the current value, notifying subscribers on value change.
        /// </summary>
        public T Value
        {
            get => _value;
            set
            {
                if (!EqualityComparer<T>.Default.Equals(_value, value))
                {
                    _value = value;
                    _onValueChanged?.Invoke(_value);
                }
            }
        }

        public BindableProperty(T defaultValue = default)
        {
            _value = defaultValue;
        }

        /// <summary>
        /// Binds a listener action to value updates.
        /// If triggerImmediately is true, invokes the callback immediately with current value.
        /// </summary>
        /// <param name="callback">Action to invoke on change.</param>
        /// <param name="triggerImmediately">Should the listener be invoked with current value immediately?</param>
        public void Bind(Action<T> callback, bool triggerImmediately = true)
        {
            if (callback == null) return;
            _onValueChanged += callback;
            if (triggerImmediately)
            {
                callback.Invoke(_value);
            }
        }

        /// <summary>
        /// Unbinds a listener action from value updates.
        /// </summary>
        /// <param name="callback">Action to remove.</param>
        public void Unbind(Action<T> callback)
        {
            if (callback == null) return;
            _onValueChanged -= callback;
        }

        /// <summary>
        /// Clears all bindings.
        /// </summary>
        public void Clear()
        {
            _onValueChanged = null;
        }

        public override string ToString()
        {
            return _value == null ? "null" : _value.ToString();
        }
    }
}
