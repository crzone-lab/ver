using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using UnityEngine;
using FRTE.Core;

namespace FRTE.Export
{
    /// <summary>
    /// Implements ISquishyProjectRepository.
    /// Manages transactional JSON writing to prevent data corruption during auto-saves.
    /// </summary>
    public sealed class SquishyProjectRepository : ISquishyProjectRepository
    {
        private readonly string _filePath;
        private readonly string _tempPath;

        public bool HasRecoverableProject => File.Exists(_filePath);

        public SquishyProjectRepository()
        {
            _filePath = Path.Combine(Application.persistentDataPath, "FRTE_ActiveProjectSession.json");
            _tempPath = _filePath + ".tmp";
        }

        public async Task SaveAsync(
            SquishyProjectSessionData session,
            CancellationToken cancellationToken)
        {
            if (session == null) return;

            cancellationToken.ThrowIfCancellationRequested();

            try
            {
                // 1. Serialize to JSON string
                string json = JsonUtility.ToJson(session, true);
                if (string.IsNullOrEmpty(json))
                {
                    throw new InvalidOperationException("Serialization produced empty output.");
                }

                // 2. Write to temporary file
                await File.WriteAllTextAsync(_tempPath, json, cancellationToken);
                cancellationToken.ThrowIfCancellationRequested();

                // 3. Verify file integrity by test-parsing
                string readTemp = await File.ReadAllTextAsync(_tempPath, cancellationToken);
                var testParse = JsonUtility.FromJson<SquishyProjectSessionData>(readTemp);
                if (testParse == null)
                {
                    throw new InvalidDataException("Temp file verification failed.");
                }

                // 4. Atomic swap
                if (File.Exists(_filePath))
                {
                    File.Delete(_filePath);
                }
                File.Move(_tempPath, _filePath);

                Debug.Log("[SquishyProjectRepository] Session saved transactionally.");
            }
            catch (Exception ex)
            {
                Debug.LogError($"[SquishyProjectRepository] SaveAsync failed: {ex.Message}");
                if (File.Exists(_tempPath))
                {
                    File.Delete(_tempPath);
                }
                throw;
            }
        }

        public async Task<SquishyProjectSessionData> LoadAsync(
            CancellationToken cancellationToken)
        {
            if (!HasRecoverableProject)
            {
                return null;
            }

            cancellationToken.ThrowIfCancellationRequested();

            try
            {
                string json = await File.ReadAllTextAsync(_filePath, cancellationToken);
                if (string.IsNullOrEmpty(json))
                {
                    return null;
                }

                var session = JsonUtility.FromJson<SquishyProjectSessionData>(json);
                return session;
            }
            catch (Exception ex)
            {
                Debug.LogError($"[SquishyProjectRepository] LoadAsync failed (deleting corrupted file): {ex.Message}");
                await DeleteAsync(cancellationToken);
                return null;
            }
        }

        public Task DeleteAsync(
            CancellationToken cancellationToken)
        {
            try
            {
                if (File.Exists(_filePath))
                {
                    File.Delete(_filePath);
                }
                if (File.Exists(_tempPath))
                {
                    File.Delete(_tempPath);
                }
            }
            catch (Exception ex)
            {
                Debug.LogWarning($"[SquishyProjectRepository] Delete files failed: {ex.Message}");
            }
            return Task.CompletedTask;
        }
    }
}
