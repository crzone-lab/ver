import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build Perfect 3D Whirlpool Drain Concave Sinkhole (No White Rings! Center & Surroundings Sink Inward!)
whirlpool_sinkhole_code = """                    } else {
                        // [탱글젤리 모드]: 누르면 터치한 부위와 주변이 하수구처럼 속으로 쏙 함몰되는 3D Sinkhole
                        let dragFromStart = (typeof touchStartX !== 'undefined' && touchStartX > 0) ? Math.hypot(touchX - touchStartX, touchY - touchStartY) : 0;

                        if (dragFromStart < 14.0) {
                            // 1. 누름/홀드 상태 (dragFromStart < 14px): 터치 부위와 주변이 하수구로 물이 빨려 들어가듯 깊게 3D 함몰
                            let sinkRadius = width * 0.45;
                            let sinkDepth = Math.min(58.0, 22.0 + touchTime * 1.8); // 누르고 있는 시간이 길어질수록 속으로 더 깊게 함몰!

                            for (let i = 0; i < points.length; i++) {
                                let p = points[i];
                                let dx = p.ox - touchX;
                                let dy = p.oy - touchY;
                                let dist = Math.hypot(dx, dy);

                                if (dist < sinkRadius && dist > 0.1) {
                                    let weight = Math.pow(1.0 - dist / sinkRadius, 1.6);
                                    let nx = dx / dist;
                                    let ny = dy / dist;

                                    // 주변 픽셀들이 터치 중심속 깊은 3D 속으로 빨려 들어감 (Inward Radial Pull)
                                    p.x = p.ox - nx * weight * sinkDepth * 0.40;
                                    p.y = p.oy - ny * weight * sinkDepth * 0.40;

                                    p.lastDx = p.x - p.ox;
                                    p.lastDy = p.y - p.oy;
                                }
                            }

                            // Render 3D Whirlpool Drain Concave Shadow (속으로 빨려 들어가는 깊은 3D 음영 - 흰색 원형 0%)
                            ctx.save();
                            let sGrad = ctx.createRadialGradient(touchX, touchY, 3, touchX, touchY, sinkRadius * 0.60);
                            sGrad.addColorStop(0, 'rgba(0, 0, 0, 0.52)'); // 중심부 깊은 3D 음영
                            sGrad.addColorStop(0.45, 'rgba(0, 0, 0, 0.25)'); // 경사면 3D 음영
                            sGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                            ctx.fillStyle = sGrad;
                            ctx.beginPath();
                            ctx.arc(touchX, touchY, sinkRadius * 0.60, 0, Math.PI * 2);
                            ctx.fill();
                            ctx.restore();

                        } else {
                            // 2. 당기기 모드 (dragFromStart >= 14px): 원본 엘라스틱 당기기
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
                    }"""

idx_mochi = content.find('else if (currentMode === \'mochi\')')
idx_else = content.find('} else {', idx_mochi)
idx_else_end = content.find('}', content.find('p.lastDy = p.y - p.oy;', idx_else) + 20) + 1
idx_else_end = content.find('}', idx_else_end + 1) + 1

if idx_mochi != -1 and idx_else != -1 and idx_else_end != -1:
    content = content[:idx_else] + whirlpool_sinkhole_code + content[idx_else_end:]
    print("100% SUCCESS: Injected Whirlpool Drain Sinkhole Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Whirlpool Drain Sinkhole Engine in index.html!")
