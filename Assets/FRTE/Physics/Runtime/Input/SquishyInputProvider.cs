using System.Collections.Generic;
using UnityEngine;

#if FRTE_INPUT_SYSTEM
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.Controls;
#endif

namespace FRTE.Physics
{
    /// <summary>
    /// Implements touch/mouse input tracking using the Unity Input System.
    /// Manages persistent pointer identifiers and delta speed calculations.
    /// </summary>
    public sealed class SquishyInputProvider : MonoBehaviour, ISquishyInputProvider
    {
        private readonly List<SquishyTouchData> _activeTouches = new List<SquishyTouchData>();
        private readonly Dictionary<int, TouchRecord> _history = new Dictionary<int, TouchRecord>();

        private struct TouchRecord
        {
            public Vector2 Position;
            public float StartTime;
            public float Duration;
        }

        public int ActiveTouchCount => _activeTouches.Count;

        public void GetActiveTouches(List<SquishyTouchData> results)
        {
            if (results == null) return;
            results.Clear();
            results.AddRange(_activeTouches);
        }

        private void Update()
        {
            _activeTouches.Clear();

#if FRTE_INPUT_SYSTEM
            var touchscreen = Touchscreen.current;
            var mouse = Mouse.current;

            // 1. Process Mobile Multi-Touch Inputs
            if (touchscreen != null)
            {
                var touches = touchscreen.touches;
                for (int i = 0; i < touches.Count; i++)
                {
                    var touchControl = touches[i];
                    if (touchControl.isInProgress || touchControl.press.wasReleasedThisFrame)
                    {
                        int id = touchControl.touchId.ReadValue();
                        Vector2 screenPos = touchControl.position.ReadValue();
                        Vector2 delta = touchControl.delta.ReadValue();

                        SquishyTouchPhase phase = SquishyTouchPhase.Stationary;
                        if (touchControl.press.wasPressedThisFrame) phase = SquishyTouchPhase.Began;
                        else if (touchControl.press.wasReleasedThisFrame) phase = SquishyTouchPhase.Ended;
                        else if (delta.sqrMagnitude > 0.01f) phase = SquishyTouchPhase.Moved;

                        RegisterTouch(id, screenPos, delta, phase);
                    }
                }
            }

            // 2. Process Unity Editor Mouse fallback (TouchId = 99 to avoid clash)
            if (_activeTouches.Count == 0 && mouse != null)
            {
                bool isPressed = mouse.leftButton.isPressed;
                bool wasPressed = mouse.leftButton.wasPressedThisFrame;
                bool wasReleased = mouse.leftButton.wasReleasedThisFrame;

                if (isPressed || wasReleased)
                {
                    Vector2 screenPos = mouse.position.ReadValue();
                    Vector2 delta = mouse.delta.ReadValue();

                    SquishyTouchPhase phase = SquishyTouchPhase.Stationary;
                    if (wasPressed) phase = SquishyTouchPhase.Began;
                    else if (wasReleased) phase = SquishyTouchPhase.Ended;
                    else if (delta.sqrMagnitude > 0.01f) phase = SquishyTouchPhase.Moved;

                    RegisterTouch(99, screenPos, delta, phase);
                }
            }
#else
            // Legacy Input System fallback if new Input System package is not active
            if (Input.touchCount > 0)
            {
                for (int i = 0; i < Input.touchCount; i++)
                {
                    var touch = Input.GetTouch(i);
                    SquishyTouchPhase phase = MapLegacyPhase(touch.phase);
                    RegisterTouch(touch.fingerId, touch.position, touch.deltaPosition, phase);
                }
            }
            else if (Input.GetMouseButton(0) || Input.GetMouseButtonUp(0))
            {
                Vector2 screenPos = Input.mousePosition;
                Vector2 delta = new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y")) * 10f;

                SquishyTouchPhase phase = SquishyTouchPhase.Stationary;
                if (Input.GetMouseButtonDown(0)) phase = SquishyTouchPhase.Began;
                else if (Input.GetMouseButtonUp(0)) phase = SquishyTouchPhase.Ended;
                else if (delta.sqrMagnitude > 0.01f) phase = SquishyTouchPhase.Moved;

                RegisterTouch(99, screenPos, delta, phase);
            }
#endif

            // Clean up history records for ended touches
            List<int> toRemove = null;
            foreach (var key in _history.Keys)
            {
                bool stillActive = false;
                for (int i = 0; i < _activeTouches.Count; i++)
                {
                    if (_activeTouches[i].TouchId == key && _activeTouches[i].Phase != SquishyTouchPhase.Ended)
                    {
                        stillActive = true;
                        break;
                    }
                }
                if (!stillActive)
                {
                    if (toRemove == null) toRemove = new List<int>();
                    toRemove.Add(key);
                }
            }
            if (toRemove != null)
            {
                for (int i = 0; i < toRemove.Count; i++)
                {
                    _history.Remove(toRemove[i]);
                }
            }
        }

        private void RegisterTouch(int id, Vector2 screenPos, Vector2 delta, SquishyTouchPhase phase)
        {
            float duration = 0f;
            Vector2 previousPos = screenPos - delta;

            if (phase == SquishyTouchPhase.Began)
            {
                _history[id] = new TouchRecord
                {
                    Position = screenPos,
                    StartTime = Time.time,
                    Duration = 0f
                };
            }
            else if (_history.TryGetValue(id, out var record))
            {
                duration = Time.time - record.StartTime;
                previousPos = record.Position;
                _history[id] = new TouchRecord
                {
                    Position = screenPos,
                    StartTime = record.StartTime,
                    Duration = duration
                };
            }

            float dt = Time.deltaTime > 0f ? Time.deltaTime : 0.016f;
            float speed = delta.magnitude / dt;

            _activeTouches.Add(new SquishyTouchData
            {
                TouchId = id,
                ScreenPosition = screenPos,
                PreviousScreenPosition = previousPos,
                Delta = delta,
                Duration = duration,
                Speed = speed,
                Phase = phase
            });
        }

#if !FRTE_INPUT_SYSTEM
        private SquishyTouchPhase MapLegacyPhase(TouchPhase phase)
        {
            switch (phase)
            {
                case TouchPhase.Began: return SquishyTouchPhase.Began;
                case TouchPhase.Moved: return SquishyTouchPhase.Moved;
                case TouchPhase.Ended: return SquishyTouchPhase.Ended;
                case TouchPhase.Canceled: return SquishyTouchPhase.Canceled;
                default: return SquishyTouchPhase.Stationary;
            }
        }
#endif
    }
}
