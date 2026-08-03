with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove all deformMesh calls from mousedown, mousemove, touchstart, touchmove
content = content.replace("deformMesh(mx, my, 18);", "// deformMesh removed")
content = content.replace("deformMesh(mx, my, 15);", "// deformMesh removed")
content = content.replace("deformMesh(pos.x, pos.y, 18);", "// deformMesh removed")
content = content.replace("deformMesh(pos.x, pos.y, 15);", "// deformMesh removed")
content = content.replace("deformMesh(touchX, touchY, 12);", "// deformMesh removed")

# 2. Fix selectLobbyCharacter to create fresh Image object so Lemon, Peach, Kiwi etc. load 100% correctly!
old_select_char = """        function selectLobbyCharacter(index, element) {
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

new_select_char = """        function selectLobbyCharacter(index, element) {
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

if old_select_char in content:
    content = content.replace(old_select_char, new_select_char)

# 3. Update selectFeelPill to apply stiffness and damping directly to existing springs
old_feel_pill = """        function selectFeelPill(feel) {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            activeFeel = feel;
            
            const pJelly = document.getElementById("pill-jelly");
            const pMochi = document.getElementById("pill-mochi");
            const pSlime = document.getElementById("pill-slime");

            [pJelly, pMochi, pSlime].forEach(p => {
                if (p) {
                    p.classList.remove("active");
                    p.style.cssText = "";
                }
            });

            if (feel === "jelly") {
                if (pJelly) pJelly.classList.add("active");
                stiffness = 50; damping = 8;
                showNotification(i18n.t("notif-jelly") || "탱글젤리 감촉 선택됨");
            } else if (feel === "mochi") {
                if (pMochi) pMochi.classList.add("active");
                stiffness = 120; damping = 22;
                showNotification(i18n.t("notif-mochi") || "쫀득모찌 감촉 선택됨");
            } else if (feel === "slime") {
                if (pSlime) pSlime.classList.add("active");
                stiffness = 22; damping = 2.5;
                showNotification(i18n.t("notif-slime") || "슬라임 감촉 선택됨");
            }
            
            const stiffnessEl = document.getElementById("spring-stiffness");
            const dampingEl = document.getElementById("dampening");
            if (stiffnessEl) stiffnessEl.value = stiffness;
            if (dampingEl) dampingEl.value = damping;
            syncSliderLabels();
        }"""

new_feel_pill = """        function selectFeelPill(feel) {
            releaseGrab(true); releaseGrab(true);
            activeFeel = feel;
            
            const pJelly = document.getElementById("pill-jelly");
            const pMochi = document.getElementById("pill-mochi");
            const pSlime = document.getElementById("pill-slime");

            [pJelly, pMochi, pSlime].forEach(p => {
                if (p) {
                    p.classList.remove("active");
                    p.style.cssText = "";
                }
            });

            if (feel === "jelly") {
                if (pJelly) pJelly.classList.add("active");
                stiffness = 50; damping = 8;
                showNotification(i18n.t("notif-jelly") || "탱글젤리 감촉 선택됨");
            } else if (feel === "mochi") {
                if (pMochi) pMochi.classList.add("active");
                stiffness = 120; damping = 22;
                showNotification(i18n.t("notif-mochi") || "쫀득모찌 감촉 선택됨");
            } else if (feel === "slime") {
                if (pSlime) pSlime.classList.add("active");
                stiffness = 22; damping = 2.5;
                showNotification(i18n.t("notif-slime") || "슬라임 감촉 선택됨");
            }
            
            for (let i = 0; i < springs.length; i++) {
                springs[i].stiffness = stiffness * 0.005;
                springs[i].damping = damping * 0.05;
            }

            const stiffnessEl = document.getElementById("spring-stiffness");
            const dampingEl = document.getElementById("dampening");
            if (stiffnessEl) stiffnessEl.value = stiffness;
            if (dampingEl) dampingEl.value = damping;
            syncSliderLabels();
        }"""

if old_feel_pill in content:
    content = content.replace(old_feel_pill, new_feel_pill)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied complete fix for Character selection, Feel Pills & Touch interaction in index.html!")
