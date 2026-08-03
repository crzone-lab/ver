import os, glob
from PIL import Image
import numpy as np
import base64

output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

# 1. Clear output directory
for f in glob.glob(f'{output_dir}/*'):
    os.remove(f)

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'

cropped_sprites = []

# --- 1. Image 1: media__1785684944159.png (3 Pastel Sugar Bunnies) ---
path1 = os.path.join(folder, 'media__1785684944159.png')
if os.path.exists(path1):
    img = Image.open(path1).convert("RGBA")
    w, h = img.size
    strip_w = w // 3
    names = ["bunny_yellow", "bunny_purple", "bunny_orange"]
    for i in range(3):
        tile = img.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        arr = np.array(tile)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 235) & (g > 235) & (b > 235)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            out_p = f"{output_dir}/user_1_{names[i]}.png"
            res.save(out_p)
            cropped_sprites.append(out_p)
            print(f"Extracted {out_p}")

# --- 2. Image 2: media__1785684944153.png (Translucent Fruit Gummies) ---
path2 = os.path.join(folder, 'media__1785684944153.png')
if os.path.exists(path2):
    img = Image.open(path2).convert("RGBA")
    w, h = img.size
    rows, cols = 3, 3
    tile_w = w // cols
    tile_h = h // rows
    count = 0
    for r in range(rows):
        for c in range(cols):
            tile = img.crop((c * tile_w, r * tile_h, (c + 1) * tile_w, (r + 1) * tile_h))
            arr = np.array(tile)
            red, grn, blu, alp = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
            white_mask = (red > 230) & (grn > 230) & (blu > 230)
            arr[white_mask, 3] = 0
            res = Image.fromarray(arr)
            bbox = res.getbbox()
            if bbox and (bbox[2] - bbox[0] > 35) and (bbox[3] - bbox[1] > 35):
                res = res.crop(bbox)
                res.thumbnail((130, 130), Image.Resampling.LANCZOS)
                out_p = f"{output_dir}/user_2_fruit_{count+1}.png"
                res.save(out_p)
                cropped_sprites.append(out_p)
                count += 1
                print(f"Extracted {out_p}")

# --- 3. Image 3: media__1785685340954.png (3 Sugar Bears) ---
path3 = os.path.join(folder, 'media__1785685340954.png')
if os.path.exists(path3):
    img = Image.open(path3).convert("RGBA")
    w, h = img.size
    strip_w = w // 3
    names = ["bear_green", "bear_red", "bear_yellow"]
    for i in range(3):
        tile = img.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        arr = np.array(tile)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 235) & (g > 235) & (b > 235)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            out_p = f"{output_dir}/user_3_{names[i]}.png"
            res.save(out_p)
            cropped_sprites.append(out_p)
            print(f"Extracted {out_p}")

# --- 4. Image 4: media__1785685763152.png (3D Glass Gradient Bunny) ---
path4 = os.path.join(folder, 'media__1785685763152.png')
if os.path.exists(path4):
    img = Image.open(path4).convert("RGBA")
    arr = np.array(img)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    white_mask = (r > 235) & (g > 235) & (b > 235)
    arr[white_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        out_p = f"{output_dir}/user_4_glass_gradient_bunny.png"
        res.save(out_p)
        cropped_sprites.append(out_p)
        print(f"Extracted {out_p}")

# --- 5. Image 5: media__1785683872412.png (Rainbow Sparkle Bunny) ---
path5 = os.path.join(folder, 'media__1785683872412.png')
if os.path.exists(path5):
    img = Image.open(path5).convert("RGBA")
    arr = np.array(img)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    black_mask = (r < 25) & (g < 25) & (b < 25)
    arr[black_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        out_p = f"{output_dir}/user_5_sparkle_bunny.png"
        res.save(out_p)
        cropped_sprites.append(out_p)
        print(f"Extracted {out_p}")

print(f"Total extracted user gummy sprites: {len(cropped_sprites)}")
