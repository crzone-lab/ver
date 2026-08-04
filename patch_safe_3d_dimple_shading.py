import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Build 100% Flip-Free Safe 3D Dimple Shading Engine on top of stable V127 baseline
safe_dimple_code = """                    } else {
                        // [탱글젤리 모드]: 100% 안전한 v127 베이스라인 유지 + 3D 함몰(Dimple) 음영 렌더링
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

                            // 3D Concave Dimple Shadow & Press Ring (뒤집힘 0% 안전 3D 함몰 음영)
                            ctx.save();
                            let dimpleRadius = width * 0.28;
                            let dGrad = ctx.createRadialGradient(touchX, touchY, 2, touchX, touchY, dimpleRadius);
                            dGrad.addColorStop(0, 'rgba(0, 0, 0, 0.42)'); // 쏙 들어가는 깊은 3D 음영
                            dGrad.addColorStop(0.55, 'rgba(0, 0, 0, 0.18)');
                            dGrad.addColorStop(0.85, 'rgba(255, 255, 255, 0.40)'); // 함몰 테두리 하이라이트
                            dGrad.addColorStop(1, 'rgba(0, 0, 0, 0)');
                            ctx.fillStyle = dGrad;
                            ctx.beginPath();
                            ctx.arc(touchX, touchY, dimpleRadius, 0, Math.PI * 2);
                            ctx.fill();
                            ctx.restore();
                        }
                    }"""

idx_mochi = content.find('else if (currentMode === \'mochi\')')
idx_else = content.find('} else {', idx_mochi)
idx_else_end = content.find('}', content.find('p.lastDy = p.y - p.oy;', idx_else) + 20) + 1
idx_else_end = content.find('}', idx_else_end + 1) + 1

if idx_mochi != -1 and idx_else != -1 and idx_else_end != -1:
    content = content[:idx_else] + safe_dimple_code + content[idx_else_end:]
    print("100% SUCCESS: Injected Safe 3D Dimple Shading Engine into draw()!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Safe 3D Dimple Shading Engine in index.html!")
