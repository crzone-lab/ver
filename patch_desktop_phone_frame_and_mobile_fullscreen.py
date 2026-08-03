with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update default .phone-frame CSS for Desktop PCs (Centred Sleek Mobile Phone Frame)
old_frame_css = """        .phone-frame {
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

new_frame_css = """        .phone-frame {
            width: 412px;
            height: 840px;
            max-height: 92vh;
            background: #000;
            border-radius: 48px;
            border: 12px solid #0d0f12;
            position: relative;
            overflow: hidden;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.08);
            display: flex;
            flex-direction: column;
            margin: auto;
        }"""

if old_frame_css in content:
    content = content.replace(old_frame_css, new_frame_css)

# Restore phone notch for desktop phone simulator frame
content = content.replace(".phone-notch { display: none !important;", ".phone-notch {")

# 2. Update Responsive Mobile Overrides so Real Mobile Phones (@media max-width: 600px) expand to 100% Fullscreen
old_mobile_media = """        /* 📱 Responsive Mobile Overrides (True Fullscreen on Mobile Devices) */
        @media (max-width: 500px), (max-height: 900px) and (orientation: portrait) {"""

new_mobile_media = """        /* 📱 Responsive Mobile Overrides (True Fullscreen on Mobile Devices & Phones) */
        @media (max-width: 600px) {"""

if old_mobile_media in content:
    content = content.replace(old_mobile_media, new_mobile_media)

# Remove the JS maintainFullscreenMode event listener that was forcing Desktop PCs into Web Fullscreen
content = content.replace("window.addEventListener('click', window.maintainFullscreenMode);", "// window.addEventListener('click', window.maintainFullscreenMode);")
content = content.replace("window.addEventListener('touchstart', window.maintainFullscreenMode);", "// window.addEventListener('touchstart', window.maintainFullscreenMode);")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Desktop Centered Mobile Phone Frame & Mobile Responsive Fullscreen in index.html!")
