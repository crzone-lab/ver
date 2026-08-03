with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if 'let isAutopilotActive = false;' in line:
        start_idx = i
    if start_idx != -1 and 'const lobbyCharacters = [' in line:
        end_idx = i
        break

print(f"Replacing lines {start_idx+1} to {end_idx}")

replacement = '''        let isAutopilotActive = false;
        let autoFingerX = 0, autoFingerY = 0;
        let autoFingerVisible = false;
        let autoStepPhase = 0;
        let autoGestureType = 0;
        let autoStepTimer = 0;

        function toggleAutopilot() {
            const lobby = document.getElementById("lobby-screen");
            if (lobby && lobby.style.display !== "none") {
                const bubble = document.querySelectorAll(".grid-char-bubble")[activeLobbyIndex];
                selectLobbyCharacter(activeLobbyIndex, bubble);
                setTimeout(() => {
                    isAutopilotActive = true;
                    applyAutopilotUIState(true);
                }, 400);
                return;
            }

            isAutopilotActive = !isAutopilotActive;
            applyAutopilotUIState(isAutopilotActive);
            if (!isAutopilotActive) {
                stopAutopilot();
            }
        }

        function applyAutopilotUIState(active) {
            const btn = document.getElementById("autopilot-btn");
            if (btn) {
                if (active) {
                    btn.style.borderColor = "#00d2ff";
                    btn.style.background = "rgba(0, 210, 255, 0.25)";
                    btn.style.boxShadow = "0 0 12px rgba(0, 210, 255, 0.5)";
                } else {
                    btn.style.borderColor = "";
                    btn.style.background = "";
                    btn.style.boxShadow = "";
                }
            }
        }

        function stopAutopilot() {
            isAutopilotActive = false;
            autoFingerVisible = false;
            applyAutopilotUIState(false);
            releaseGrab(true);
            if (points && points.length > 0) {
                for (let i = 0; i < points.length; i++) {
                    points[i].x = points[i].ox;
                    points[i].y = points[i].oy;
                    points[i].vx = 0; points[i].vy = 0;
                }
            }
            showNotification(i18n.t("notif-auto-stop") || "오토 모드 정지됨");
        }

        function updateAutopilotFrame() {
            if (!isAutopilotActive || !points || points.length === 0) return;

            autoStepTimer++;

            let centerIdx = Math.floor(rows / 2) * cols + Math.floor(cols / 2);
            let centerPoint = points[centerIdx] || points[0];
            if (!centerPoint || isNaN(centerPoint.ox) || isNaN(centerPoint.oy)) return;

            if (autoStepPhase === 0) {
                autoGestureType = (autoGestureType + 1) % 3;
                autoStepPhase = 1;
                autoStepTimer = 0;
                autoFingerVisible = true;

                if (autoGestureType === 0) {
                    showNotification(i18n.t("notif-auto-pull") || "🤖 오토: [통째로 쭈-욱 당겨서 튕기기]");
                } else if (autoGestureType === 1) {
                    showNotification(i18n.t("notif-auto-press") || "🤖 오토: [캐릭터 꾹 눌러 오목하게 하기]");
                } else {
                    showNotification(i18n.t("notif-auto-push") || "🤖 오토: [측면 쓱 밀어서 튕기기]");
                }
            } else if (autoStepPhase === 1) {
                let progress = Math.min(1.0, autoStepTimer / 45);
                let moveX = 0, moveY = 0;

                if (autoGestureType === 0) {
                    moveX = 110 * Math.sin(progress * Math.PI);
                    moveY = -100 * Math.sin(progress * Math.PI);
                } else if (autoGestureType === 1) {
                    moveY = 75 * Math.sin(progress * Math.PI);
                } else {
                    moveX = 120 * Math.sin(progress * Math.PI);
                }

                autoFingerX = centerPoint.ox + moveX;
                autoFingerY = centerPoint.oy + moveY;

                // Move 100% of all points together as ONE SINGLE SOLID COHESIVE BODY (no tearing, no NaN)
                for (let i = 0; i < points.length; i++) {
                    if (points[i] && !isNaN(points[i].ox) && !isNaN(points[i].oy)) {
                        points[i].x = points[i].ox + moveX;
                        points[i].y = points[i].oy + moveY;
                        points[i].vx *= 0.5; points[i].vy *= 0.5;
                    }
                }

                if (autoStepTimer >= 45) {
                    autoStepPhase = 2;
                    autoStepTimer = 0;
                    autoFingerVisible = false;
                    playSquishSound(true);
                }
            } else if (autoStepPhase === 2) {
                if (autoStepTimer >= 25) {
                    autoStepPhase = 0;
                }
            }
        }\n\n'''

final_lines = lines[:start_idx] + [replacement] + lines[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Successfully patched index.html!")
