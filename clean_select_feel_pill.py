with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

select_pill_clean = """function selectFeelPill(feel) {
            activeTextureMode = feel;
            const pJelly = document.getElementById("pill-jelly");
            const pMochi = document.getElementById("pill-mochi");
            const pSlime = document.getElementById("pill-slime");

            [pJelly, pMochi, pSlime].forEach(p => {
                if (p) p.classList.remove("active");
            });

            if (feel === "jelly") {
                if (pJelly) pJelly.classList.add("active");
                stiffness = 50; damping = 8;
                showNotification(i18n.t("notif-jelly") || "탱글젤리 감촉 선택됨");
            } else if (feel === "mochi") {
                if (pMochi) pMochi.classList.add("active");
                stiffness = 110; damping = 18;
                showNotification(i18n.t("notif-mochi") || "쫀득모찌 감촉 선택됨");
            } else if (feel === "slime") {
                if (pSlime) pSlime.classList.add("active");
                stiffness = 15; damping = 3;
                showNotification(i18n.t("notif-slime") || "슬라임 감촉 선택됨");
            }
            
            const stiffnessEl = document.getElementById("spring-stiffness");
            const dampingEl = document.getElementById("dampening");
            if (stiffnessEl) stiffnessEl.value = stiffness;
            if (dampingEl) dampingEl.value = damping;
            syncSliderLabels();
        }"""

idx_s = content.find('function selectFeelPill(')
if idx_s != -1:
    idx_s_end = content.find('function setScreenMode', idx_s)
    content = content[:idx_s] + select_pill_clean + "\n\n        " + content[idx_s_end:]
    print("100% Successfully cleaned selectFeelPill function!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied clean index.html!")
