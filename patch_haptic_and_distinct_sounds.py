with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Web Audio Sound Synthesis for Pull, Push, Press, Release & Sequential Haptics
new_audio_haptic_code = """        let audioCtx = null;

        function getAudioContext() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            if (audioCtx.state === 'suspended') {
                audioCtx.resume();
            }
            return audioCtx;
        }

        // 🤏 1. Pull Sound (당길 때 고무 고탄성 스트레칭 톤)
        function playPullSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(220, now);
                osc.frequency.exponentialRampToValueAtTime(480, now + 0.14);
                gain.gain.setValueAtTime(0.12, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.14);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.14);
            } catch (e) {}
        }

        // 👈 2. Push Sound (밀 때 젤리 미끄러짐 톤)
        function playPushSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(160, now);
                osc.frequency.linearRampToValueAtTime(280, now + 0.12);
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.12);
            } catch (e) {}
        }

        // 👇 3. Press Sound (꾹 누를 때 3D 중저음 수축 톤)
        function playPressSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(150, now);
                osc.frequency.exponentialRampToValueAtTime(70, now + 0.16);
                gain.gain.setValueAtTime(0.14, now);
                gain.gain.exponentialRampToValueAtTime(0.01, now + 0.16);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.16);
            } catch (e) {}
        }

        // ✨ 4. Release Sound (놓을 때 멋진 화음 3D 탄성 튕김 톤)
        function playReleaseSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;

                // Main spring bounce
                const osc1 = ctx.createOscillator();
                const gain1 = ctx.createGain();
                osc1.type = 'triangle';
                osc1.frequency.setValueAtTime(320, now);
                osc1.frequency.exponentialRampToValueAtTime(620, now + 0.08);
                osc1.frequency.exponentialRampToValueAtTime(420, now + 0.18);
                gain1.gain.setValueAtTime(0.15, now);
                gain1.gain.exponentialRampToValueAtTime(0.01, now + 0.18);
                osc1.connect(gain1);
                gain1.connect(ctx.destination);
                osc1.start(now);
                osc1.stop(now + 0.18);

                // Sub-harmonic shimmer pop
                const osc2 = ctx.createOscillator();
                const gain2 = ctx.createGain();
                osc2.type = 'sine';
                osc2.frequency.setValueAtTime(640, now + 0.04);
                osc2.frequency.exponentialRampToValueAtTime(880, now + 0.15);
                gain2.gain.setValueAtTime(0.08, now + 0.04);
                gain2.gain.exponentialRampToValueAtTime(0.005, now + 0.18);
                osc2.connect(gain2);
                gain2.connect(ctx.destination);
                osc2.start(now + 0.04);
                osc2.stop(now + 0.18);
            } catch (e) {}
        }

        function playSquishSound(isRelease = false) {
            if (isRelease) {
                playReleaseSound();
            } else {
                playPressSound();
            }
        }

        // 📲 5. Sequential Rhythmic Haptic Vibration Pattern ("드드드드" 순차 진동)
        let lastHapticTime = 0;
        function triggerSequentialHaptic() {
            if (!isPlaygroundActive() || !isVibrationEnabled) return;
            const now = Date.now();
            if (now - lastHapticTime > 80) { // Trigger rhythmic steps every 80ms
                if (navigator.vibrate) {
                    navigator.vibrate([12, 18, 12, 18]); // "드드드드" sequential pulse pattern
                }
                lastHapticTime = now;
            }
        }

        function triggerReleaseHaptic() {
            if (!isPlaygroundActive() || !isVibrationEnabled) return;
            if (navigator.vibrate) {
                navigator.vibrate([35, 15, 45]); // Firm release recoil pulse
            }
        }"""

old_sound_def = """        let audioCtx = null;

        function playSquishSound(isRelease = false) {"""

# Replace old sound definition with rich new sound & haptics system
import re
content = re.sub(r'let audioCtx = null;.*?function playSquishSound\(isRelease = false\) \{.*?\n        \}', new_audio_haptic_code, content, flags=re.DOTALL)

# Update releaseGrab to call playReleaseSound & triggerReleaseHaptic
old_release_grab = """        const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && !quiet) {
                playSquishSound(true);
                triggerHaptic(30);
            }
            grabbedPointIndex = null;
            isTouching = false;
            touchTime = 0;
        };"""

new_release_grab = """        const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && !quiet) {
                playReleaseSound();
                triggerReleaseHaptic();
            }
            grabbedPointIndex = null;
            isTouching = false;
            touchTime = 0;
        };"""

if old_release_grab in content:
    content = content.replace(old_release_grab, new_release_grab)

# Trigger sound & sequential haptics on touchmove / mousemove
old_touchmove_head = """        canvas.addEventListener('touchmove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            e.preventDefault();
            let pos = getTouchPos(e);
            if (!pos) return;
            touchX = pos.x;
            touchY = pos.y;
            isTouching = true;"""

new_touchmove_head = """        canvas.addEventListener('touchmove', (e) => {
            if (!isPlaygroundActive() || isAutopilotActive) return;
            e.preventDefault();
            let pos = getTouchPos(e);
            if (!pos) return;
            
            let moveDist = Math.sqrt(Math.pow(pos.x - touchX, 2) + Math.pow(pos.y - touchY, 2));
            if (moveDist > 6) {
                triggerSequentialHaptic(); // "드드드드" sequential haptics
                if (pos.y < touchY) {
                    playPullSound(); // Pulling upward sound
                } else {
                    playPushSound(); // Pushing downward sound
                }
            }

            touchX = pos.x;
            touchY = pos.y;
            isTouching = true;"""

if old_touchmove_head in content:
    content = content.replace(old_touchmove_head, new_touchmove_head)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Distinct Sounds for Pull/Push/Press/Release & Sequential Dr-dr-dr-dr Haptics in index.html!")
