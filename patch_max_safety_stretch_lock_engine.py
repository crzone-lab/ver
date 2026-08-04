import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Maximum Elastic Safety Lock Engine (32px Strict Offset Limit)
lock_engine_code = """                // 1. Maximum Elastic Safety Lock Physics Engine (캐릭터 형상 파괴 100% 방지 32px 안전 락)
                if (isTouching) {
                    touchTime++;

                    let maxDragRadius = 38.0; // Hard clamp for drag vector (38px max)
                    let maxNodeOffset = 32.0; // Hard clamp for individual node offset (32px max)

                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        let gNode = points[grabbedPointIndex];
                        let rawDx = touchX - gNode.ox;
                        let rawDy = touchY - gNode.oy;

                        let dragDist = Math.sqrt(rawDx * rawDx + rawDy * rawDy);
                        let dragScale = dragDist > maxDragRadius ? (maxDragRadius / dragDist) : 1.0;

                        let clampedDx = rawDx * dragScale;
                        let clampedDy = rawDy * dragScale;

                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let pdx = p.ox - gNode.ox;
                            let pdy = p.oy - gNode.oy;
                            let dist = Math.sqrt(pdx * pdx + pdy * pdy);

                            let influence = Math.exp(- (dist * dist) / (160.0 * 160.0));
                            p.x = p.ox + clampedDx * influence;
                            p.y = p.oy + clampedDy * influence;
                            p.vx *= 0.30; p.vy *= 0.30;

                            // Enforce strict 32px safety boundary lock from anchor origin
                            let offX = p.x - p.ox;
                            let offY = p.y - p.oy;
                            let offDist = Math.sqrt(offX * offX + offY * offY);
                            if (offDist > maxNodeOffset) {
                                p.x = p.ox + (offX / offDist) * maxNodeOffset;
                                p.y = p.oy + (offY / offDist) * maxNodeOffset;
                            }
                        }
                    } else {
                        let suctionPower = Math.min(0.35, 0.08 + touchTime * 0.003);
                        let maxRadius = width * 0.40;
                        for (let i = 0; i < points.length; i++) {
                            let p = points[i];
                            let pdx = p.ox - touchX;
                            let pdy = p.oy - touchY;
                            let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 1.8);
                                p.x = p.ox + (touchX - p.ox) * weight * suctionPower;
                                p.y = p.oy + (touchY - p.oy) * weight * suctionPower;
                                p.vx *= 0.35; p.vy *= 0.35;

                                // Enforce strict 32px safety boundary lock
                                let offX = p.x - p.ox;
                                let offY = p.y - p.oy;
                                let offDist = Math.sqrt(offX * offX + offY * offY);
                                if (offDist > maxNodeOffset) {
                                    p.x = p.ox + (offX / offDist) * maxNodeOffset;
                                    p.y = p.oy + (offY / offDist) * maxNodeOffset;
                                }
                            }
                        }
                    }
                } else {
                    touchTime = 0;
                    for (let i = 0; i < points.length; i++) {
                        let fx = (points[i].ox - points[i].x) * stiffness * 0.0014;
                        let fy = (points[i].oy - points[i].y) * stiffness * 0.0014;

                        points[i].vx = (points[i].vx + fx) * (1 - damping * 0.008);
                        points[i].vy = (points[i].vy + fy) * (1 - damping * 0.008);

                        points[i].x += points[i].vx;
                        points[i].y += points[i].vy;
                    }
                }"""

# Locate the exact touch physics block in draw()
idx_draw = content.find('function draw()')
idx_touch_start = content.find('if (isTouching)', idx_draw)
idx_touch_end = content.find('// 2. Solve internal springs every frame', idx_touch_start)

if idx_draw != -1 and idx_touch_start != -1 and idx_touch_end != -1:
    content = content[:idx_touch_start] + lock_engine_code + "\n\n                " + content[idx_touch_end:]
    print("100% SUCCESS: Injected Maximum Elastic Safety Lock Physics Engine into index.html!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Maximum Safety Stretch Lock Engine in index.html!")
