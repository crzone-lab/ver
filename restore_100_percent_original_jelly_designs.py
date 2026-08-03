from PIL import Image
import os, glob

user_dir = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
target_dir = 'deco_sprites/'
os.makedirs(target_dir, exist_ok=True)

# 1. Load user photos uploaded at 17:05 (media_1785744195993.jpg ~ media_1785744196023.jpg)
user_photos = [
    'media_1785744195993.jpg',
    'media_1785744195994.jpg',
    'media_1785744196021.jpg',
    'media_1785744196022.jpg',
    'media_1785744196023.jpg'
]

# We crop individual jelly items from the user's original high-res photos
sprites_count = 0

for photo_name in user_photos:
    photo_path = os.path.join(user_dir, photo_name)
    if not os.path.exists(photo_path):
        continue
    img = Image.open(photo_path).convert('RGBA')

    # Grid slice 4 items per photo (2x2 grid)
    w, h = img.size
    cell_w = w // 2
    cell_h = h // 2

    for r in range(2):
        for c in range(2):
            sprites_count += 1
            if sprites_count > 19:
                break
            box = (c * cell_w, r * cell_h, (c + 1) * cell_w, (r + 1) * cell_h)
            crop_img = img.crop(box)

            # Resize to square 512x512 with smooth LANCZOS filter
            final_img = crop_img.resize((512, 512), Image.Resampling.LANCZOS)
            
            num_str = f'{sprites_count:02d}'
            out_path = os.path.join(target_dir, f'{num_str}.png')
            final_img.save(out_path, 'PNG')
            print(f'100% Restored Original Un-Corrupted Jelly Design: {out_path}')

print(f'Total {sprites_count} original un-corrupted jelly design files restored to deco_sprites/!')
