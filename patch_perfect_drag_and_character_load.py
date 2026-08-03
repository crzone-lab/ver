with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update selectLobbyCharacter so ANY character (Lemon, Peach, Kiwi, etc.) loads 100% cleanly
old_select = """        function selectLobbyCharacter(index, element) {
            try {
                stopAutopilot(); releaseGrab(true); releaseGrab(true);
                activeLobbyIndex = index;
                const char = lobbyCharacters[index];
                if (!char) return;
                
                activeEmoji = char.emoji || "🍓";
                activeBase = char.base || "custom";
                activeHue = char.hue || 350;

                // 1. ALWAYS transition screen to 3D jelly playground page IMMEDIATELY
                setScreenMode("playground");

                // Hide splash screen if open
                const splash = document.getElementById('start-splash-screen');
                if (splash) {
                    splash.classList.add('fade-out');
                    splash.style.display = 'none';
                }

                const imageSrc = char.imgData || char.file || "strawberry_rabbit_jelly.png";

                const loadAndInit = () => {
                    initMesh();
                    generateDecoJellies(activeHue);
                    draw();
                };

                jellyImage.onload = loadAndInit;
                jellyImage.src = imageSrc;

                if (jellyImage.complete && jellyImage.naturalWidth > 0) {
                    loadAndInit();
                }

                showNotification(`${char.name} ${i18n.t("notif-selected") || "선택되었습니다!"}`);

                // Highlight selected bubble
                document.querySelectorAll('.grid-char-bubble').forEach(b => b.classList.remove('active'));
                if (element) {
                    element.classList.add('active');
                } else {
                    const bubbles = document.querySelectorAll('.grid-char-bubble');
                    if (bubbles[index]) {
                        bubbles[index].classList.add('active');
                    }
                }
            } catch (err) {
                console.error("selectLobbyCharacter error:", err);
                setScreenMode("playground");
            }
        }"""

new_select = """        function selectLobbyCharacter(index, element) {
            try {
                releaseGrab(true); releaseGrab(true);
                activeLobbyIndex = index;
                const char = lobbyCharacters[index];
                if (!char) return;
                
                activeEmoji = char.emoji || "🍓";
                activeBase = char.base || "custom";
                activeHue = char.hue || 350;

                setScreenMode("playground");

                const splash = document.getElementById('start-splash-screen');
                if (splash) {
                    splash.classList.add('fade-out');
                    splash.style.display = 'none';
                }

                const imageSrc = char.imgData || char.file || "strawberry_rabbit_jelly.png";

                const newImg = new Image();
                const loadAndInit = () => {
                    jellyImage = newImg;
                    initMesh();
                    generateDecoJellies(activeHue);
                    draw();
                };

                newImg.onload = loadAndInit;
                newImg.src = imageSrc;

                if (newImg.complete && newImg.naturalWidth > 0) {
                    loadAndInit();
                }

                showNotification(`${char.name} ${i18n.t("notif-selected") || "선택되었습니다!"}`);

                document.querySelectorAll('.grid-char-bubble').forEach(b => b.classList.remove('active'));
                if (element) {
                    element.classList.add('active');
                } else {
                    const bubbles = document.querySelectorAll('.grid-char-bubble');
                    if (bubbles[index]) {
                        bubbles[index].classList.add('active');
                    }
                }
            } catch (err) {
                console.error("selectLobbyCharacter error:", err);
                setScreenMode("playground");
            }
        }"""

if old_select in content:
    content = content.replace(old_select, new_select)

# 2. Update draw() drag physics: Move 100% of all points together by (dx, dy) on touch/mouse drag (ZERO squishing down!)
old_draw_drag = """                // 1. Clean Drag & Spring Physics (No downward squishing on hover)
                if (isTouching) {
                    if (grabbedPointIndex !== null && points[grabbedPointIndex]) {
                        let grabbedPoint = points[grabbedPointIndex];
                        grabbedPoint.x = touchX;
                        grabbedPoint.y = touchY;
                        grabbedPoint.vx = 0;
                        grabbedPoint.vy = 0;

                        let maxRadius = width * 0.38;
                        for (let i = 0; i < points.length; i++) {
                            if (i === grabbedPointIndex) continue;
                            let p = points[i];
                            let pdx = p.ox - grabbedPoint.ox;
                            let pdy = p.oy - grabbedPoint.oy;
                            let dist = Math.sqrt(pdx * pdx + pdy * pdy);
                            if (dist < maxRadius) {
                                let weight = Math.pow(1 - dist / maxRadius, 2.0);
                                p.x = p.ox + (touchX - grabbedPoint.ox) * weight * 0.6;
                                p.y = p.oy + (touchY - grabbedPoint.oy) * weight * 0.6;
                                p.vx *= 0.5; p.vy *= 0.5;
                            }
                        }
                    }
                } else {"""

new_draw_drag = """                // 1. Single Solid Cohesive Touch Drag Physics (No downward squishing!)
                if (isTouching) {
                    let dx = touchX - lastTouchX;
                    let dy = touchY - lastTouchY;
                    lastTouchX = touchX;
                    lastTouchY = touchY;

                    // Move 100% of all points together smoothly as ONE SINGLE SOLID COHESIVE BODY
                    for (let i = 0; i < points.length; i++) {
                        points[i].x += dx;
                        points[i].y += dy;
                        points[i].vx *= 0.5;
                        points[i].vy *= 0.5;
                    }
                } else {"""

if old_draw_drag in content:
    content = content.replace(old_draw_drag, new_draw_drag)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied patch_perfect_drag_and_character_load.py!")
