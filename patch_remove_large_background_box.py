with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_container_css = """        .bottom-carousel-container {
            position: absolute;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            width: calc(100% - 32px);
            max-width: 380px;
            height: 102px;
            z-index: 28000;
            background: rgba(255, 255, 255, 0.48);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border-radius: 26px;
            border: 2px solid rgba(255, 255, 255, 0.85);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.16), inset 0 2px 4px rgba(255, 255, 255, 0.8);
            overflow: hidden;
            pointer-events: auto;
            display: flex;
            align-items: center;
            padding: 0 6px;
        }"""

new_container_css = """        .bottom-carousel-container {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 412px;
            height: 98px;
            z-index: 28000;
            background: transparent;
            backdrop-filter: none;
            -webkit-backdrop-filter: none;
            border-radius: 0;
            border: none;
            box-shadow: none;
            overflow: hidden;
            pointer-events: auto;
            display: flex;
            align-items: center;
            padding: 0 4px;
        }"""

if old_container_css in content:
    content = content.replace(old_container_css, new_container_css)
    print("100% Successfully removed large white background box from bottom container!")
else:
    print("WARNING: old_container_css not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied CSS update in index.html!")
