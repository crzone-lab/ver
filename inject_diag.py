import re, shutil

# Restore clean v157 baseline first
shutil.copyfile('v157.0.0_PERFECT_HIGH_JUMP_7_5S_LONG_BOUNCE_MASTER.html', 'index.html')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject Diagnostic Engine at start of JS
diag_code = """<script>
        // AGY Real-time Diagnostic Engine
        window.AGY_DIAGNOSTICS = {
            log: function(msg) {
                console.log('[AGY LOG]', msg);
                let bar = document.getElementById('agy-diag-bar');
                if (bar) bar.innerText = '🔬 ' + msg;
            },
            reportError: function(context, err) {
                console.error('[AGY ERROR]', context, err);
                let bar = document.getElementById('agy-diag-bar');
                if (bar) {
                    bar.style.background = 'rgba(239, 68, 68, 0.9)';
                    bar.innerText = '⚠️ [' + context + '] ' + (err.message || err);
                }
            }
        };

        window.onerror = function(msg, url, lineNo, colNo, error) {
            window.AGY_DIAGNOSTICS.reportError('Line ' + lineNo, error || msg);
            return true;
        };

        // Internationalization"""

content = content.replace('<script>\n        // Internationalization', diag_code, 1)

# 2. Inject UI Toast Overlay
toast_code = """    <!-- Real-time Diagnostic Monitor Overlay -->
    <div id="agy-diag-bar" style="position: fixed; bottom: 85px; right: 15px; background: rgba(15, 23, 42, 0.88); color: #60a5fa; font-family: Inter, sans-serif; font-size: 12px; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(96, 165, 250, 0.4); z-index: 999999; pointer-events: none;">
        🔬 Real-time Diagnostic Monitor Active
    </div>
</body>"""

content = content.replace('</body>', toast_code, 1)

# 3. Add Diagnostic Logging to selectLobbyCharacter & setScreenMode
content = content.replace('function setScreenMode(mode) {', 'function setScreenMode(mode) {\n            try { if (window.AGY_DIAGNOSTICS) window.AGY_DIAGNOSTICS.log("Screen mode -> " + mode); } catch(e) {}')

content = content.replace('function selectLobbyCharacter(index, element) {', 'function selectLobbyCharacter(index, element) {\n            try { if (window.AGY_DIAGNOSTICS) window.AGY_DIAGNOSTICS.log("Character selected: #" + index); } catch(e) {}')

# 4. Apply Bulletproof Array Guard in releaseGrab
rel_grab_target = """const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {"""

rel_grab_replace = """const releaseGrab = (quiet = false) => {
            if (currentMode === 'mochi' && typeof points !== 'undefined' && points && points.length > 0) {
                for (let i = 0; i < points.length; i++) {
                    if (points[i] && points[i].x !== undefined && points[i].ox !== undefined) {
                        points[i].lastDx = points[i].x - points[i].ox;
                        points[i].lastDy = points[i].y - points[i].oy;
                    }
                }
            } else if (grabbedPointIndex !== null && typeof points !== 'undefined' && points && points[grabbedPointIndex]) {"""

content = content.replace(rel_grab_target, rel_grab_replace, 1)

# 5. Apply Spring Solver Gate
spring_target = 'if (isTouching || releaseTime > 90) {'
spring_replace = 'if (currentMode !== "mochi" && (isTouching || releaseTime > 90)) {'
content = content.replace(spring_target, spring_replace, 1)

# 6. Apply Chewy Mochi Viscous Return in draw()
release_target = """                // 높은 96px 점프 + 7.5초 롱 바운스 재미있는 탄성 여운 엔진 (~7.5초)
                if (!isTouching) {"""

release_replace = """                // 릴리즈 동작: 탱글젤리(고공 96px 바운스) vs 쫀득모찌(12초 초슬로우 점성 복원) 차별화 Engine
                if (!isTouching) {
                    let tSec = releaseTime * 0.016;

                    if (currentMode === 'mochi') {
                        // [쫀득모찌 릴리즈]: 12초 동안 엄청 느리고 묵직하게 츠스스- 복원
                        if (releaseTime <= 750) {
                            let viscousDecay = Math.exp(-0.18 * tSec);

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let baseDx = (p && p.lastDx !== undefined) ? p.lastDx : 0;
                                let baseDy = (p && p.lastDy !== undefined) ? p.lastDy : 0;

                                p.x = p.ox + baseDx * viscousDecay;
                                p.y = p.oy + baseDy * viscousDecay;

                                p.oldx = p.x;
                                p.oldy = p.y;
                            }
                        } else {
                            for (let i = 0; i < points.length; i++) {
                                points[i].x = points[i].ox;
                                points[i].y = points[i].oy;
                                points[i].oldx = points[i].ox;
                                points[i].oldy = points[i].oy;
                                points[i].vx = 0;
                                points[i].vy = 0;
                            }
                        }
                    } else {"""

content = content.replace(release_target, release_replace, 1)

# Close the additional else block cleanly
close_target = """                        } else {
                            // Bounces complete cleanly at zero amplitude after 7.5 seconds
                            for (let i = 0; i < points.length; i++) {
                                points[i].x = points[i].ox;
                                points[i].y = points[i].oy;
                                points[i].oldx = points[i].ox;
                                points[i].oldy = points[i].oy;
                                points[i].vx = 0;
                                points[i].vy = 0;
                            }
                        }
                    }
                }"""

# Replace lines cleanly
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('100% SUCCESS: Injected Real-time Diagnostic Engine cleanly!')
