with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace realJellySpritePaths with ONLY pure genuine real product jelly PNGs
old_paths = """        const realJellySpritePaths = [
            "deco_sprites/real_bunny_1.png", "deco_sprites/real_bunny_2.png", "deco_sprites/real_bunny_3.png",
            "deco_sprites/real_sugar_bear_1.png", "deco_sprites/real_sugar_bear_2.png", "deco_sprites/real_sugar_bear_3.png",
            "deco_sprites/real_gradient_bunny.png", "deco_sprites/real_sparkle_bunny.png",
            "deco_sprites/real_sea_1.png", "deco_sprites/real_sea_2.png", "deco_sprites/real_sea_3.png",
            "deco_sprites/real_sea_4.png", "deco_sprites/real_sea_5.png", "deco_sprites/real_sea_6.png",
            "deco_sprites/real_sea_7.png", "deco_sprites/real_sea_8.png", "deco_sprites/real_sea_9.png",
            "deco_sprites/real_sea_10.png", "deco_sprites/real_sea_11.png", "deco_sprites/real_sea_12.png",
            "deco_sprites/real_jelly_3.png", "deco_sprites/real_jelly_4.png", "deco_sprites/real_jelly_5.png",
            "deco_sprites/real_jelly_6.png", "deco_sprites/real_jelly_7.png", "deco_sprites/real_jelly_8.png"
        ];"""

new_paths = """        const realJellySpritePaths = [
            "deco_sprites/real_bunny_1.png", "deco_sprites/real_bunny_2.png", "deco_sprites/real_bunny_3.png",
            "deco_sprites/real_sugar_bear_1.png", "deco_sprites/real_sugar_bear_2.png", "deco_sprites/real_sugar_bear_3.png",
            "deco_sprites/real_gradient_bunny.png", "deco_sprites/real_sparkle_bunny.png",
            "deco_sprites/real_sea_1.png", "deco_sprites/real_sea_2.png", "deco_sprites/real_sea_3.png",
            "deco_sprites/real_sea_4.png", "deco_sprites/real_sea_5.png", "deco_sprites/real_sea_6.png",
            "deco_sprites/real_sea_7.png", "deco_sprites/real_sea_8.png", "deco_sprites/real_sea_9.png",
            "deco_sprites/real_sea_10.png", "deco_sprites/real_sea_11.png", "deco_sprites/real_sea_12.png"
        ];"""

if old_paths in content:
    content = content.replace(old_paths, new_paths)
    print("100% Successfully cleaned sprite paths! Removed UI screenshot rectangles!")
else:
    print("WARNING: old_paths not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Pure Real Jelly Sprite Paths in index.html!")
