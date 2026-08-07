import re

with open('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Responsive desktop smartphone frame CSS replacement
old_phone_css = """;
        /* 2. Phone Simulator (Viewport) Centered */
        .phone-frame {
            width: 100vw !important;
            height: 100dvh !important;
            max-width: 100vw !important;
            max-height: 100dvh !important;
            margin: 0 !important;
            padding: 0 !important;
            flex-shrink: 0 !important;
            background: #000;
            border-radius: 0 !important;
            border: 0 !important;
            position: fixed;
            top: 0;
            left: 0;
            overflow: hidden;
            box-shadow: none !important;
            display: flex;
            flex-direction: column;
        }"""

new_phone_css = """;
        /* 🎯 Desktop Smartphone Frame Container */
        @media (min-width: 768px) {
            .phone-frame {
                position: relative !important;
                width: 390px !important;
                height: 820px !important;
                max-height: 94vh !important;
                border-radius: 42px !important;
                border: 10px solid #1e293b !important;
                box-shadow: 0 25px 75px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.12) !important;
                overflow: hidden !important;
                background: #07080a !important;
                margin: auto !important;
                top: auto !important;
                left: auto !important;
                display: flex;
                flex-direction: column;
            }
        }
        @media (max-width: 767px) {
            .phone-frame {
                position: fixed !important;
                width: 100vw !important;
                height: 100dvh !important;
                top: 0 !important;
                left: 0 !important;
                border-radius: 0 !important;
                border: none !important;
                display: flex;
                flex-direction: column;
            }
        }"""

if old_phone_css in content:
    content = content.replace(old_phone_css, new_phone_css)
else:
    print("WARNING: old_phone_css not found exactly, doing regex replace")
    content = re.sub(r'/\* 2\. Phone Simulator \(Viewport\) Centered \*/\s*\.phone-frame\s*\{[^}]+\}', new_phone_css, content)

# 2. Add 4th feel pill: bubble (🫧 젤리팝)
old_pills = """        <!-- 5. Unified Global Feel Selector pills (z-index: 25000) -->
        <div class="lobby-feel-selector" style="z-index: 25000; pointer-events: none;">
            <div style="pointer-events: auto !important;" class="feel-pill active" id="pill-jelly" onclick="selectFeelPill('jelly')" ontouchstart="selectFeelPill('jelly')" data-i18n="pill-jelly">탱글젤리</div>
            <div style="pointer-events: auto !important;" class="feel-pill" id="pill-mochi" onclick="selectFeelPill('mochi')" ontouchstart="selectFeelPill('mochi')" data-i18n="pill-mochi">쫀득모찌</div>
            <div style="pointer-events: auto !important;" class="feel-pill" id="pill-slime" onclick="selectFeelPill('slime')" ontouchstart="selectFeelPill('slime')" data-i18n="pill-slime">슬라임</div>
        </div>"""

new_pills = """        <!-- 5. Unified Global Feel Selector pills (z-index: 25000) -->
        <div class="lobby-feel-selector" style="z-index: 25000; pointer-events: none;">
            <div style="pointer-events: auto !important;" class="feel-pill active" id="pill-jelly" onclick="selectFeelPill('jelly')" ontouchstart="selectFeelPill('jelly')" data-i18n="pill-jelly">🍮 탱글젤리</div>
            <div style="pointer-events: auto !important;" class="feel-pill" id="pill-mochi" onclick="selectFeelPill('mochi')" ontouchstart="selectFeelPill('mochi')" data-i18n="pill-mochi">🍡 쫀득모찌</div>
            <div style="pointer-events: auto !important;" class="feel-pill" id="pill-slime" onclick="selectFeelPill('slime')" ontouchstart="selectFeelPill('slime')" data-i18n="pill-slime">💧 슬라임</div>
            <div style="pointer-events: auto !important;" class="feel-pill" id="pill-bubble" onclick="selectFeelPill('bubble')" ontouchstart="selectFeelPill('bubble')" data-i18n="pill-bubble">🫧 젤리팝</div>
        </div>"""

if old_pills in content:
    content = content.replace(old_pills, new_pills)

# 3. Update selectFeelPill function logic
old_select_feel = """        function selectFeelPill(feel) {
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

new_select_feel = """        function selectFeelPill(feel) {
            activeTextureMode = feel;
            ['jelly', 'mochi', 'slime', 'bubble'].forEach(id => {
                const el = document.getElementById("pill-" + id);
                if (el) el.classList.remove("active");
            });

            const activeEl = document.getElementById("pill-" + feel);
            if (activeEl) activeEl.classList.add("active");

            if (feel === "jelly") {
                stiffness = 180; damping = 5;
                showNotification("🍮 탱글젤리: 통통 튕기는 탄성 푸딩!");
            } else if (feel === "mochi") {
                stiffness = 25; damping = 20;
                showNotification("🍡 쫀득모찌: 쭈~욱 늘어나는 쫀득한 찹쌀떡!");
            } else if (feel === "slime") {
                stiffness = 8; damping = 38;
                showNotification("💧 슬라임: 당기면 아주 천천히 복원되는 고점성 슬라임!");
            } else if (feel === "bubble") {
                stiffness = 45; damping = 6;
                showNotification("🫧 젤리팝: 3D 방울 팽창 & 팡! 폭발!");
            }
            
            const stiffnessEl = document.getElementById("spring-stiffness");
            const dampingEl = document.getElementById("dampening");
            if (stiffnessEl) stiffnessEl.value = stiffness;
            if (dampingEl) dampingEl.value = damping;
            syncSliderLabels();
        }"""

if old_select_feel in content:
    content = content.replace(old_select_feel, new_select_feel)

# Save patched index.html
with open('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch applied successfully!")
