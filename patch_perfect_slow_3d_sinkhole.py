import re, shutil

# Revert to clean baseline v127
shutil.copyfile('v127.0.0_PERFECT_MASTER_RELEASE.html', 'index.html')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Exact surgical replacement for Tangle Jelly
target_str = '''                    } else {
                        // [탱글젤리 모드]: 터치 부위가 길고 쫀쫀하게 당겨짐
                        if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                            let gNode = points[grabbedPointIndex];
                            let dragDx = touchX - gNode.ox;
                            let dragDy = touchY - gNode.oy;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let pdx = p.ox - gNode.ox;
                                let pdy = p.oy - gNode.oy;
                                let dist = Math.hypot(pdx, pdy);

                                let sigma = 100.0;
                                let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                p.x = p.ox + dragDx * weight * 1.35;
                                p.y = p.oy + dragDy * weight * 1.35;

                                p.lastDx = p.x - p.ox;
                                p.lastDy = p.y - p.oy;
                            }
                        }
                    }'''

replacement_str = '''                    } else {
                        // [탱글젤리 모드]: 누르면 터치한 지점과 주변이 천천히 속으로 쏙 함몰되고 한계 깊이에서 스톱!
                        let dragFromStart = (typeof touchStartX !== 'undefined' && touchStartX > 0) ? Math.hypot(touchX - touchStartX, touchY - touchStartY) : 0;

                        if (dragFromStart < 14.0) {
                            // 1. 누름/홀드 상태 (dragFromStart < 14px): 1.2초 동안 천천히 3D 속으로 들어간 후 스톱!
                            let sinkProgress = Math.min(1.0, touchTime / 75.0);
                            let smoothEase = 1.0 - Math.pow(1.0 - sinkProgress, 2.0); // 부드러운 감속 이징
                            let maxDepth = 45.0; // 스톱 한계 깊이
                            let sinkDepth = smoothEase * maxDepth;

                            let sinkRadius = width * 0.45;

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let dx = p.ox - touchX;
                                let dy = p.oy - touchY;
                                let dist = Math.hypot(dx, dy);

                                if (dist < sinkRadius) {
                                    let weight = Math.pow(1.0 - dist / sinkRadius, 1.4);
                                    let nx = (dist > 0.1) ? (dx / dist) : 0; // Division by zero 방지 (사라짐 0%)
                                    let ny = (dist > 0.1) ? (dy / dist) : 0;

                                    let shift = weight * sinkDepth * 0.55;
                                    p.x = p.ox - nx * shift;
                                    p.y = p.oy - ny * shift;

                                    // Verlet Integration Synchronization (스프링 적분기와 위치 동기화)
                                    p.oldx = p.x;
                                    p.oldy = p.y;
                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }

                            // Render 3D Whirlpool Drain Concave Shadow
                            ctx.save();
                            let sGrad = ctx.createRadialGradient(touchX, touchY, 3, touchX, touchY, sinkRadius * 0.60);
                            sGrad.addColorStop(0, `rgba(0, 0, 0, ${0.52 * smoothEase})`);
                            sGrad.addColorStop(0.45, `rgba(0, 0, 0, ${0.22 * smoothEase})`);
                            sGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                            ctx.fillStyle = sGrad;
                            ctx.beginPath();
                            ctx.arc(touchX, touchY, sinkRadius * 0.60, 0, Math.PI * 2);
                            ctx.fill();
                            ctx.restore();

                        } else {
                            // 2. 당기기 모드 (dragFromStart >= 14px): 원본 엘라스틱 당기기 (100% 보존)
                            if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                                let gNode = points[grabbedPointIndex];
                                let dragDx = touchX - gNode.ox;
                                let dragDy = touchY - gNode.oy;

                                for (let i = 0; i < points.length; i++) {
                                    let p = points[i];
                                    let pdx = p.ox - gNode.ox;
                                    let pdy = p.oy - gNode.oy;
                                    let dist = Math.hypot(pdx, pdy);

                                    let sigma = 100.0;
                                    let weight = Math.exp(-(dist * dist) / (2.0 * sigma * sigma));

                                    p.x = p.ox + dragDx * weight * 1.35;
                                    p.y = p.oy + dragDy * weight * 1.35;

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }
                        }
                    }'''

# Update touch start handlers
content = content.replace(
    'grabbedPointIndex = closestIdx;\n                isTouching = true;\n                touchX = tx;\n                touchY = ty;',
    'grabbedPointIndex = closestIdx;\n                isTouching = true;\n                touchX = tx;\n                touchY = ty;\n                touchStartX = tx;\n                touchStartY = ty;'
)
content = content.replace(
    'isTouching = true;\n            touchX = mx;\n            touchY = my;\n            lastTouchX = mx;\n            lastTouchY = my;\n            touchTime = 0;',
    'isTouching = true;\n            touchX = mx;\n            touchY = my;\n            lastTouchX = mx;\n            lastTouchY = my;\n            touchStartX = mx;\n            touchStartY = my;\n            touchTime = 0;'
)
content = content.replace(
    'isTouching = true;\n            touchX = pos.x;\n            touchY = pos.y;\n            lastTouchX = pos.x;\n            lastTouchY = pos.y;\n            touchTime = 0;',
    'isTouching = true;\n            touchX = pos.x;\n            touchY = pos.y;\n            lastTouchX = pos.x;\n            lastTouchY = pos.y;\n            touchStartX = pos.x;\n            touchStartY = pos.y;\n            touchTime = 0;'
)

if target_str in content:
    content = content.replace(target_str, replacement_str)
    print('100% SURGICAL SUCCESS: Replaced Tangle Jelly block cleanly!')
else:
    print('ERROR: target_str not found!')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
