// ==========================================
// 🧪 AGY Decoupled Physics Engine & Presets
// ==========================================

function solvePhysicsStep(isTouching, releaseTime, currentMode, points, springs) {
    try {
        if (!points || points.length === 0) return;

        if (currentMode === 'mochi') {
            // 🍡 1. Mochi Mode: Dedicated 12-Second Slow Viscous Return
            if (!isTouching) {
                let tSec = releaseTime * 0.016;
                if (releaseTime <= 750) {
                    let viscousDecay = Math.exp(-0.18 * tSec);
                    for (let i = 0; i < points.length; i++) {
                        let p = points[i];
                        if (p) {
                            let baseDx = (typeof p.lastDx === 'number' && !isNaN(p.lastDx)) ? p.lastDx : 0;
                            let baseDy = (typeof p.lastDy === 'number' && !isNaN(p.lastDy)) ? p.lastDy : 0;

                            p.x = p.ox + baseDx * viscousDecay;
                            p.y = p.oy + baseDy * viscousDecay;

                            p.oldx = p.x;
                            p.oldy = p.y;
                        }
                    }
                } else {
                    for (let i = 0; i < points.length; i++) {
                        if (points[i]) {
                            points[i].x = points[i].ox;
                            points[i].y = points[i].oy;
                            points[i].oldx = points[i].ox;
                            points[i].oldy = points[i].oy;
                            points[i].vx = 0;
                            points[i].vy = 0;
                            points[i].lastDx = 0;
                            points[i].lastDy = 0;
                        }
                    }
                }
            }
        } else if (currentMode === 'slime') {
            // 💧 2. Slime Mode: 100% Pure Liquid Spring Physics (Zero Shivering/Flickering!)
            if (isTouching || releaseTime > 0) {
                for (let step = 0; step < 4; step++) {
                    for (let i = 0; i < springs.length; i++) {
                        springs[i].solve();
                    }
                }
                for (let i = 0; i < points.length; i++) {
                    points[i].update();
                }
            }
        } else {
            // 🐰 3. Tangle Jelly Mode: 100% Pure v157 96px High Jump & 3D Bowl Sinkhole
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

            if (!isTouching) {
                let tSec = releaseTime * 0.016;

                if (releaseTime <= 450) {
                    let floatEnv = Math.exp(-0.45 * tSec);
                    let jumpHeight = Math.abs(Math.sin(2.2 * tSec)) * floatEnv * 96.0;
                    let swayX = Math.sin(1.5 * tSec) * floatEnv * 54.0;
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
                        let baseDx = (typeof p.lastDx === 'number' && !isNaN(p.lastDx) && p.lastDx !== 0) ? p.lastDx : (p.x - p.ox);
                        let baseDy = (typeof p.lastDy === 'number' && !isNaN(p.lastDy) && p.lastDy !== 0) ? p.lastDy : (p.y - p.oy);

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
                    for (let i = 0; i < points.length; i++) {
                        if (points[i]) {
                            points[i].x = points[i].ox;
                            points[i].y = points[i].oy;
                            points[i].oldx = points[i].ox;
                            points[i].oldy = points[i].oy;
                            points[i].vx = 0;
                            points[i].vy = 0;
                            points[i].lastDx = 0;
                            points[i].lastDy = 0;
                        }
                    }
                }
            }
        }
    } catch(err) {
        console.error("[Physics Module Error]", err);
    }
}
