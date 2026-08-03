with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update setScreenMode to explicitly handle bottomCarousel container display
old_set_screen = """            } else if (mode === "playground") {
                if (splash) { splash.style.display = "none"; splash.style.opacity = "0"; splash.style.pointerEvents = "none"; }
                if (lobby) {
                    lobby.style.display = "none";
                    lobby.style.opacity = "0";
                    lobby.style.visibility = "hidden";
                    lobby.style.zIndex = "-1";
                    lobby.style.pointerEvents = "none";
                }
                if (topUI) { topUI.style.display = "flex"; topUI.style.zIndex = "20000"; }
                if (feelUI) { feelUI.style.display = "flex"; feelUI.style.zIndex = "20000"; }"""

new_set_screen = """            } else if (mode === "playground") {
                if (splash) { splash.style.display = "none"; splash.style.opacity = "0"; splash.style.pointerEvents = "none"; }
                if (lobby) {
                    lobby.style.display = "none";
                    lobby.style.opacity = "0";
                    lobby.style.visibility = "hidden";
                    lobby.style.zIndex = "-1";
                    lobby.style.pointerEvents = "none";
                }
                if (topUI) { topUI.style.display = "flex"; topUI.style.zIndex = "20000"; }
                if (feelUI) { feelUI.style.display = "flex"; feelUI.style.zIndex = "20000"; }
                const bottomCarousel = document.getElementById("bottom-carousel-container");
                if (bottomCarousel) { 
                    bottomCarousel.style.display = "flex"; 
                    bottomCarousel.style.zIndex = "28000"; 
                }
                renderBottomCarousel();"""

if old_set_screen in content:
    content = content.replace(old_set_screen, new_set_screen)
    print("100% Successfully updated setScreenMode in index.html!")
else:
    print("WARNING: old_set_screen not found!")

# Also ensure renderBottomCarousel doesn't block on screenMode
content = content.replace("screenMode === 'playground'", "true")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Always Visible Bottom Carousel Fix in index.html!")
