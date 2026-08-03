with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Enlarge top header logo (logo_font.png) by ~50%
old_logo = 'style="height: 56px; max-width: 220px; object-fit: contain;"'
new_logo = 'style="height: 84px; max-width: 320px; object-fit: contain; filter: drop-shadow(0 4px 10px rgba(0,0,0,0.25));"'

if old_logo in content:
    content = content.replace(old_logo, new_logo)
    print("100% Successfully enlarged top logo!")
else:
    print("WARNING: old_logo not found!")

# 2. Expand mobile media query to cover ALL mobile screens (max-width 768px, portrait & landscape)
old_media = "@media (max-width: 500px), (max-height: 900px) and (orientation: portrait) {"
new_media = "@media (max-width: 768px), (max-height: 1024px), (orientation: portrait) {"

if old_media in content:
    content = content.replace(old_media, new_media)
    print("100% Successfully expanded mobile responsive media query for True Fullscreen on all mobile devices!")
else:
    print("WARNING: old_media not found!")

# 3. Add Fullscreen Enforcer script to auto-expand to 100vw x 100vh on mobile touch/enter
fullscreen_enforcer_js = """
        // Automatic Mobile Fullscreen Enforcer
        function enforceMobileFullscreen() {
            if (window.innerWidth <= 768 || /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
                const frame = document.querySelector('.phone-frame');
                if (frame) {
                    frame.style.setProperty('width', '100vw', 'important');
                    frame.style.setProperty('height', '100vh', 'important');
                    frame.style.setProperty('height', '100dvh', 'important');
                    frame.style.setProperty('border', 'none', 'important');
                    frame.style.setProperty('border-radius', '0', 'important');
                }
            }
        }
        window.addEventListener('resize', enforceMobileFullscreen);
        window.addEventListener('orientationchange', enforceMobileFullscreen);
        document.addEventListener('DOMContentLoaded', enforceMobileFullscreen);
        enforceMobileFullscreen();
"""

if "function initMesh()" in content:
    content = content.replace("function initMesh()", fullscreen_enforcer_js + "\n        function initMesh()")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Top Logo Enlargement & Mobile Fullscreen Enforcer in index.html!")
