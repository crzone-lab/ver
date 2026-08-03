with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .phone-frame CSS to ALWAYS be 100vw x 100vh True Fullscreen across ALL devices
old_frame_css = """        .phone-frame {
            width: 412px;
            height: 840px;
            background: #000;
            border-radius: 48px;
            border: 12px solid var(--phone-border);
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.05);
            display: flex;
            flex-direction: column;
        }"""

new_frame_css = """        .phone-frame {
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important;
            background: #000;
            border: none !important;
            border-radius: 0 !important;
            box-shadow: none !important;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            margin: 0 !important;
            padding: 0 !important;
        }"""

if old_frame_css in content:
    content = content.replace(old_frame_css, new_frame_css)

# Hide mock notch globally for true fullscreen
content = content.replace(".phone-notch {", ".phone-notch { display: none !important; ")

# 2. Enlarge Top Logo image (logo_font.png) to height 72px and max-width 280px (~30% larger!)
old_logo = """<img src="logo_font.png" alt="Logo" style="height: 56px; max-width: 220px; object-fit: contain;">"""
new_logo = """<img src="logo_font.png" alt="Logo" style="height: 72px; max-width: 280px; object-fit: contain;">"""

if old_logo in content:
    content = content.replace(old_logo, new_logo)

# 3. Add JS Fullscreen Keeper to request Fullscreen on any touch/click/navigation
js_fullscreen = """
    // Always enforce Fullscreen mode on user interaction & screen transitions
    window.maintainFullscreenMode = function() {
        try {
            if (document.documentElement.requestFullscreen && !document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(() => {});
            } else if (document.documentElement.webkitRequestFullscreen && !document.webkitFullscreenElement) {
                document.documentElement.webkitRequestFullscreen().catch(() => {});
            }
        } catch (e) {}
    };

    window.addEventListener('click', window.maintainFullscreenMode);
    window.addEventListener('touchstart', window.maintainFullscreenMode);
"""

if "</head>" in content:
    content = content.replace("</head>", "<script>" + js_fullscreen + "</script>\n</head>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied ALWAYS TRUE FULLSCREEN & 30% Enlarged Top Logo in index.html!")
