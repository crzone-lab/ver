with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Polish Strawberry Rabbit scaling in initMesh to 1.25x for 100% visual balance with Lemon Rabbit
old_mesh_init = """            let maxW = canvasW * 0.78;
            let maxH = canvasH * 0.49;"""

new_mesh_init = """            let sizeScale = 1.0;
            if (activeBase === "strawberry_rabbit" || (jellyImage && jellyImage.src && jellyImage.src.includes("strawberry_rabbit"))) {
                sizeScale = 1.25;
            }

            let maxW = canvasW * 0.78 * sizeScale;
            let maxH = canvasH * 0.49 * sizeScale;"""

if old_mesh_init in content:
    content = content.replace(old_mesh_init, new_mesh_init)

# 2. Polish selectLobbyCharacter so ALL 17 fruit rabbits switch 100% cleanly with new Image object
old_select_char = """        function selectLobbyCharacter(index, element) {
            stopAutopilot(); releaseGrab(true); releaseGrab(true);
            activeLobbyIndex = index;
            const char = lobbyCharacters[index];
            if (!char) return;
            
            activeEmoji = char.emoji;
            activeBase = char.base;
            activeHue = char.hue;

            // Hide splash screen if open
            const splash = document.getElementById('start-splash-screen');
            if (splash) {
                splash.classList.add('fade-out');
                splash.style.display = 'none';
            }

            jellyImage.onload = function() {
                initMesh();
                draw();
            };

            const imageSrc = char.imgData || char.file || "strawberry_rabbit_jelly.png";

            jellyImage.onload = function() {
                initMesh();
                draw();
            };

            jellyImage.src = imageSrc;

            if (jellyImage.complete && jellyImage.naturalWidth > 0) {
                initMesh();
                draw();
            }
            
            initMesh();
            generateDecoJellies(char.hue);
            setScreenMode("playground");
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

# 3. Polish selectFeelPill to apply stiffness & damping dynamically to active springs
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

print("Applied patch_polish_working_engine.py to index.html!")
