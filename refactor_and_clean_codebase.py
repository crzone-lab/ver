import re, shutil

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up duplicate or old leftover comments
content = re.sub(r'// Trigger immediate downward sinking reaction on press\s*// no deformMesh', '', content)
content = re.sub(r'// Trigger immediate downward sinking reaction on touch press\s*// no deformMesh', '', content)

# 2. Add clean structural section headers in JavaScript
section_headers = """
        /* ==========================================================================
           FRUIT RABBIT MALRANGI 3D JELLY ENGINE v3.5.0 (STABLE RELEASE)
           - 100% Unified Whole-Body Cohesion & Pure 3D Inward Z-Depth Physics
           - Soft Liquid Sine Bubble Audio Synthesizer & Silky 6ms Micro-Haptics
           - Bottom 17 Fruit Rabbit Auto-Scroll Carousel Selector Engine
           ========================================================================== */
"""

if "let activeBase = 'strawberry_rabbit';" in content:
    content = content.replace("let activeBase = 'strawberry_rabbit';", section_headers + "\n        let activeBase = 'strawberry_rabbit';")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Create permanent checkpoint v3.5.0
shutil.copyfile('index.html', 'v3.5.0_fruit_rabbit_touch_engine.html')

print("100% Successfully refactored codebase and created permanent checkpoint: v3.5.0_fruit_rabbit_touch_engine.html")
