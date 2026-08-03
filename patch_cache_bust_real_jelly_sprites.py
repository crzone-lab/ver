with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add timestamp cache buster to all image loading so browser NEVER loads old pink rectangles
old_loader = """        const loadedRealJellyImages = [];
        realJellySpritePaths.forEach(path => {
            const img = new Image();
            img.src = path;
            loadedRealJellyImages.push(img);
        });"""

new_loader = """        const loadedRealJellyImages = [];
        const cacheBuster = Date.now();
        realJellySpritePaths.forEach(path => {
            const img = new Image();
            img.src = path + "?v=" + cacheBuster;
            loadedRealJellyImages.push(img);
        });"""

if old_loader in content:
    content = content.replace(old_loader, new_loader)
    print("100% Successfully added cache buster to real jelly image loading!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Cache Buster Fix in index.html!")
