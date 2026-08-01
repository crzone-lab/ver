using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace FRTE.Surprise
{
    /// <summary>
    /// Implements ISurpriseEffectPool procedurally instantiating placeholder effects.
    /// Manages recycling of active visual objects.
    /// </summary>
    public sealed class SurpriseEffectPool : MonoBehaviour, ISurpriseEffectPool
    {
        private readonly Dictionary<string, Queue<ISurpriseEffect>> _pool = new Dictionary<string, Queue<ISurpriseEffect>>();
        private readonly List<ISurpriseEffect> _activeEffects = new List<ISurpriseEffect>();

        private const int MaxActiveLimit = 15;

        public ISurpriseEffect Rent(string effectId)
        {
            if (string.IsNullOrEmpty(effectId)) return null;

            // 1. Maintain pool queue
            if (!_pool.TryGetValue(effectId, out var queue))
            {
                queue = new Queue<ISurpriseEffect>();
                _pool.Add(effectId, queue);
            }

            ISurpriseEffect effect;
            if (queue.Count > 0)
            {
                effect = queue.Dequeue();
            }
            else
            {
                // Instantiate new procedural effect instance
                effect = CreateProceduralEffect(effectId);
            }

            if (effect != null)
            {
                _activeEffects.Add(effect);
                effect.GameObject.SetActive(true);
            }

            return effect;
        }

        public void Return(ISurpriseEffect effect)
        {
            if (effect == null) return;

            effect.GameObject.SetActive(false);
            _activeEffects.Remove(effect);

            if (_pool.TryGetValue(effect.EffectId, out var queue))
            {
                queue.Enqueue(effect);
            }
        }

        public void Clear()
        {
            // Stop and destroy active ones
            for (int i = 0; i < _activeEffects.Count; i++)
            {
                if (_activeEffects[i].GameObject != null)
                {
                    Destroy(_activeEffects[i].GameObject);
                }
            }
            _activeEffects.Clear();

            // Destroy pooled ones
            foreach (var kvp in _pool)
            {
                var queue = kvp.Value;
                while (queue.Count > 0)
                {
                    var eff = queue.Dequeue();
                    if (eff.GameObject != null)
                    {
                        Destroy(eff.GameObject);
                    }
                }
            }
            _pool.Clear();
        }

        private ISquishyEffectInstance CreateProceduralEffect(string effectId)
        {
            var rootGo = new GameObject("FX_" + effectId);
            rootGo.transform.SetParent(transform, false);

            var spriteRenderer = rootGo.AddComponent<SpriteRenderer>();
            spriteRenderer.sortingOrder = 50; // Surprise Layer

            var inst = rootGo.AddComponent<ProceduralEffectInstance>();
            inst.Configure(effectId, this, spriteRenderer);
            return inst;
        }

        // Interface helper to match return type
        private interface ISquishyEffectInstance : ISurpriseEffect {}

        private sealed class ProceduralEffectInstance : MonoBehaviour, ISquishyEffectInstance
        {
            public string EffectId { get; private set; }
            public bool IsActive => gameObject.activeSelf;
            public GameObject GameObject => gameObject;

            private SurpriseEffectPool _pool;
            private SpriteRenderer _renderer;
            private float _playTimer;
            private float _duration = 1.5f;

            public void Configure(string id, SurpriseEffectPool pool, SpriteRenderer renderer)
            {
                EffectId = id;
                _pool = pool;
                _renderer = renderer;

                // Create placeholder shape based on ID
                var tex = new Texture2D(32, 32);
                Color color = Color.white;

                if (id.Contains("heart")) color = Color.red;
                else if (id.Contains("star")) color = Color.yellow;
                else if (id.Contains("juice") || id.Contains("ripple")) color = new Color(1f, 0.5f, 0f, 0.7f); // Orange juice
                else if (id.Contains("fruit_pop")) color = Color.green;
                else if (id.Contains("strawberry")) color = new Color(1f, 0.2f, 0.2f, 0.8f);
                else if (id.Contains("watermelon")) color = new Color(0.1f, 0.8f, 0.2f, 0.8f);
                else if (id.Contains("grape")) color = new Color(0.5f, 0.1f, 0.9f, 0.8f);
                else color = Color.cyan;

                for (int y = 0; y < 32; y++)
                {
                    for (int x = 0; x < 32; x++)
                    {
                        tex.SetPixel(x, y, color);
                    }
                }
                tex.Apply();
                _renderer.sprite = Sprite.Create(tex, new Rect(0, 0, 32, 32), new Vector2(0.5f, 0.5f));
            }

            public void Play(Vector2 normalizedUV, float duration)
            {
                _duration = duration;
                _playTimer = 0f;

                // Set position mapping from UV space to world camera space
                transform.position = new Vector3(normalizedUV.x * 5f, normalizedUV.y * 5f, -1f);
                transform.localScale = Vector3.one * 0.2f;

                gameObject.SetActive(true);
            }

            public void Stop()
            {
                if (_pool != null)
                {
                    _pool.Return(this);
                }
            }

            private void Update()
            {
                _playTimer += Time.deltaTime;
                if (_playTimer >= _duration)
                {
                    Stop();
                    return;
                }

                // Simple Tween animation procedurally
                float t = _playTimer / _duration;
                transform.localScale = Vector3.Lerp(Vector3.one * 0.2f, Vector3.one * 0.8f, t);
                transform.position += Vector3.up * Time.deltaTime * 0.5f; // float upwards

                var color = _renderer.color;
                color.a = Mathf.Lerp(1f, 0f, t); // fade out
                _renderer.color = color;
            }
        }
    }
}
