with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Audio & Haptics to Soft Liquid Jelly Pops & Soft Silk Micro-Haptics
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

        // 🫧 1. Soft Liquid Jelly Squish Sound (말랑말랑 촉촉한 젤리 눌림 톤)
        function playJellySquishSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(320, now);
                osc.frequency.exponentialRampToValueAtTime(450, now + 0.05);
                osc.frequency.exponentialRampToValueAtTime(260, now + 0.12);
                
                gain.gain.setValueAtTime(0.12, now);
                gain.gain.exponentialRampToValueAtTime(0.005, now + 0.12);
                
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.12);
            } catch (e) {}
        }

        // 🤏 2. Soft Jelly Pull Sound (쫀득하게 늘어나는 젤리 톤)
        function playJellyPullSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(260, now);
                osc.frequency.exponentialRampToValueAtTime(520, now + 0.14);
                
                gain.gain.setValueAtTime(0.1, now);
                gain.gain.exponentialRampToValueAtTime(0.005, now + 0.14);
                
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.14);
            } catch (e) {}
        }

        // ✨ 3. Soft Jelly Release Bounce Sound (탱글하게 튕겨 퍼지는 젤리 복원 톤)
        function playJellyReleaseSound() {
            if (!isPlaygroundActive() || !isSoundEnabled) return;
            try {
                const ctx = getAudioContext();
                const now = ctx.currentTime;

                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                
                osc.type = 'sine';
                osc.frequency.setValueAtTime(420, now);
                osc.frequency.exponentialRampToValueAtTime(780, now + 0.07);
                osc.frequency.exponentialRampToValueAtTime(520, now + 0.16);
                
                gain.gain.setValueAtTime(0.15, now);
                gain.gain.exponentialRampToValueAtTime(0.005, now + 0.16);
                
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start(now);
                osc.stop(now + 0.16);
            } catch (e) {}
        }

        // 📲 4. Soft Silk Micro-Haptic Pulse (말랑촉촉 비단결 젤리 햅틱)
        let lastJellyHapticTime = 0;
        function triggerJellyHaptic() {
            if (!isPlaygroundActive() || !isVibrationEnabled) return;
            const now = Date.now();
            if (now - lastJellyHapticTime > 90) {
                if (navigator.vibrate) {
                    navigator.vibrate(6); // Gentle 6ms micro-tap
                }
                lastJellyHapticTime = now;
            }
        }

        function triggerJellyReleaseHaptic() {
            if (!isPlaygroundActive() || !isVibrationEnabled) return;
            if (navigator.vibrate) {
                navigator.vibrate([15, 10, 20]); // Soft spring bounce pulse
            }
        }"""

# Replace old audio & haptic block
import re
content = re.sub(r'let audioCtx = null;.*?function triggerReleaseHaptic\(\) \{.*?\n        \}', new_audio_haptic_code, content, flags=re.DOTALL)

# 2. Update draw() touch code for Pure 3D Z-Depth Sinking Right Under Finger (Screen Y-shift = 0)
old_touch_code = """                // 1. Steep Localized 3D Pit Indentation (누른 곳이 깊숙하게 푹 파이고, 멀어질수록 미세해짐)
                if (isTouching) {
                    touchTime++;

                    // Deep local indentation accumulates smoothly with holding duration (25px up to 90px deep pit!)
                    let deepPitIndentation = Math.min(90, 25 + touchTime * 2.2);

                    if (touchTime % 5 === 0) {
                        triggerSequentialHaptic();
                        if (touchTime % 10 === 0) playPressSound();
                    }

                    // Tight local radius (28% of width) prevents whole character from shrinking!
                    let maxRadius = width * 0.28;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            // Cubic steep falloff (power = 3.2): Center sinks DEEPLY, distant nodes remain untouched!
                            let weight = Math.pow(1 - dist / maxRadius, 3.2);
                            
                            // 1. Steep local Z-depth downward pit
                            p.y = p.oy + deepPitIndentation * weight;

                            // 2. Subtle local inward squeeze at press core
                            p.x = p.ox + (touchX - p.ox) * weight * 0.35;
                            p.vx *= 0.25; p.vy *= 0.25;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY + deepPitIndentation * 0.45;
                    }
                } else {"""

new_touch_code = """                // 1. Pure 3D Z-Depth Sinking Right Under Finger (Screen Y-Shift = 0)
                if (isTouching) {
                    touchTime++;

                    // Compression factor accumulates continuously into 3D Z-depth (0.20 up to 0.85)
                    let zDepthCompression = Math.min(0.85, 0.20 + touchTime * 0.04);

                    if (touchTime % 4 === 0) {
                        triggerJellyHaptic();
                        if (touchTime % 8 === 0) playJellySquishSound();
                    }

                    // Localized influence radius (30% of width)
                    let maxRadius = width * 0.30;
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        let pdx = p.ox - touchX;
                        let pdy = p.oy - touchY;
                        let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                        if (dist < maxRadius) {
                            let weight = Math.pow(1 - dist / maxRadius, 2.5);
                            
                            // ZERO screen-Y shift towards bottom of screen!
                            // All points converge 360 degrees directly UNDER THE FINGER into 3D Z-depth
                            p.x = p.ox + (touchX - p.ox) * weight * zDepthCompression;
                            p.y = p.oy + (touchY - p.oy) * weight * zDepthCompression;
                            p.vx *= 0.25; p.vy *= 0.25;
                        }
                    }

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        points[grabbedPointIndex].x = touchX;
                        points[grabbedPointIndex].y = touchY;
                    }
                } else {"""

if old_touch_code in content:
    content = content.replace(old_touch_code, new_touch_code)
    print("Successfully replaced touch code in index.html!")
else:
    print("WARNING: old_touch_code not found!")

# Replace release function calls with playJellyReleaseSound & triggerJellyReleaseHaptic
content = content.replace("playReleaseSound();", "playJellyReleaseSound();")
content = content.replace("triggerReleaseHaptic();", "triggerJellyReleaseHaptic();")
content = content.replace("triggerSequentialHaptic();", "triggerJellyHaptic();")
content = content.replace("playPullSound();", "playJellyPullSound();")
content = content.replace("playPushSound();", "playJellySquishSound();")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Pure 3D Z-Depth Sinking Right Under Finger & Soft Jelly Liquid Sounds in index.html!")
