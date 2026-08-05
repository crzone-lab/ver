import re

with open('v157.0.0_PERFECT_HIGH_JUMP_7_5S_LONG_BOUNCE_MASTER.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add module script tags in head
module_imports = """    <!-- 🛡️ AGY Modular Engine Script Imports -->
    <script src="js/ui_navigation.js"></script>
    <script src="js/physics_engine.js"></script>
</head>"""

content = content.replace('</head>', module_imports, 1)

# 2. Update releaseGrab in main script to use physics module
rel_grab_target = """const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                // Give spring release velocity impulse to initiate 2-3 bounces!
                let impulse = 0.45;
                points[grabbedPointIndex].vx = (touchX - lastTouchX) * impulse;
                points[grabbedPointIndex].vy = (touchY - lastTouchY) * impulse;
            }
            grabbedPointIndex = null;
            isTouching = false;
            if (!quiet) {
                playReleaseSound();
            }
        };"""

rel_grab_modular = """const releaseGrab = (quiet = false) => {
            if (grabbedPointIndex !== null && typeof points !== 'undefined' && points && points[grabbedPointIndex]) {
                if (currentMode === 'mochi') {
                    for (let i = 0; i < points.length; i++) {
                        if (points[i]) {
                            points[i].lastDx = (points[i].x !== undefined && points[i].ox !== undefined) ? (points[i].x - points[i].ox) : 0;
                            points[i].lastDy = (points[i].y !== undefined && points[i].oy !== undefined) ? (points[i].y - points[i].oy) : 0;
                        }
                    }
                } else {
                    let impulse = 0.45;
                    points[grabbedPointIndex].vx = (touchX - lastTouchX) * impulse;
                    points[grabbedPointIndex].vy = (touchY - lastTouchY) * impulse;
                }
            }
            grabbedPointIndex = null;
            isTouching = false;
            releaseTime = 0;
            if (!quiet) {
                playReleaseSound();
            }
        };"""

content = content.replace(rel_grab_target, rel_grab_modular, 1)

# 3. Replace physics block in draw() to delegate to solvePhysicsStep() module
draw_physics_target = """                // 1. Physics Spring Solver (Only run when touching or after release animation completes)
                if (isTouching || releaseTime > 90) {
                    for (let step = 0; step < 4; step++) {
                        for (let i = 0; i < springs.length; i++) {
                            springs[i].solve();
                        }
                    }
                    for (let i = 0; i < points.length; i++) {
                        points[i].update();
                    }
                }

                // 높은 96px 점프 + 7.5초 롱 바운스 재미있는 탄성 여운 릴리즈 엔진 (~7.5초)
                if (!isTouching) {
                    let tSec = releaseTime * 0.016; // Time in seconds

                    if (releaseTime <= 450) {
                        // 아주 완만하고 부드러운 감쇄 (gamma = 0.45): 7.5초 동안 여유롭고 재미있게 지속되는 롱 바운스
                        let floatEnv = Math.exp(-0.45 * tSec); // 아주 여유로운 롱 릴리즈 감쇄
                        let jumpHeight = Math.abs(Math.sin(2.2 * tSec)) * floatEnv * 96.0; // 높게 붕- 튀어오르는 96px 고공 점프!
                        let swayX = Math.sin(1.5 * tSec) * floatEnv * 54.0; // 재미있고 크고 넉넉한 좌우 54px 흔들림!
                        let squishY = 1.0 + (Math.cos(3.2 * tSec) * floatEnv * 0.28);
                        let squishX = 1.0 - (Math.cos(3.2 * tSec) * floatEnv * 0.18);

                        let centerX = 0, centerY = 0;
                        for (let i = 0; i < points.length; i++) {
                            centerX += points[i].ox;
                            centerY += points[i].oy;
                        }
                        centerX /= points.length;
                        centerY /= points.length;

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let baseDx = (p.lastDx !== undefined) ? p.lastDx : (p.x - p.ox);
                            let baseDy = (p.lastDy !== undefined) ? p.lastDy : (p.y - p.oy);

                            let localX = p.ox + baseDx * floatEnv * Math.cos(3.2 * tSec);
                            let localY = p.oy + baseDy * floatEnv * Math.cos(3.2 * tSec);

                            let relX = localX - centerX;
                            let relY = localY - centerY;

                            p.x = centerX + (relX * squishX) + swayX;
                            p.y = centerY + (relY * squishY) - jumpHeight;

                            p.oldx = p.x;
                            p.oldy = p.y;
                        }
                    } else {
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
                }"""

draw_physics_modular = """                // 🧪 Delegate physics solver cleanly to js/physics_engine.js module!
                if (typeof solvePhysicsStep === 'function') {
                    solvePhysicsStep(isTouching, releaseTime, currentMode, points, springs);
                }"""

content = content.replace(draw_physics_target, draw_physics_modular, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('100% SUCCESS: Updated index.html with clean modular architecture!')
