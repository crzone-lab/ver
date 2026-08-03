import os, glob
from PIL import Image
import numpy as np

output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

# Delete ALL old files in deco_sprites first to be 100% clean!
old_files = glob.glob(f'{output_dir}/*')
for of in old_files:
    os.remove(of)
print(f"Cleared {len(old_files)} old files in {output_dir}.")

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'

# 1. media__1785685763152.png (3D Glass Gradient Bunny - Black BG)
try:
    path = os.path.join(folder, 'media__1785685763152.png')
    img = Image.open(path).convert("RGBA")
    arr = np.array(img)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    # Black background threshold
    black_mask = (r < 25) & (g < 25) & (b < 25)
    arr[black_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        res.save(f"{output_dir}/real_gradient_glass_bunny.png")
        print("Saved real_gradient_glass_bunny.png")
except Exception as e:
    print(f"Error: {e}")

# 2. media__1785683872412.png (Rainbow Sparkle Bunny - Black BG)
try:
    path = os.path.join(folder, 'media__1785683872412.png')
    img = Image.open(path).convert("RGBA")
    arr = np.array(img)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    black_mask = (r < 25) & (g < 25) & (b < 25)
    arr[black_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        res.save(f"{output_dir}/real_rainbow_sparkle_bunny.png")
        print("Saved real_rainbow_sparkle_bunny.png")
except Exception as e:
    print(f"Error: {e}")

# 3. media__1785685340954.png (3 Sugar Bears: Green, Red, Yellow - White BG)
try:
    path = os.path.join(folder, 'media__1785685340954.png')
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    strip_w = w // 3
    bear_names = ["green_bear", "red_bear", "yellow_bear"]
    for i in range(3):
        crop_tile = img.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        arr = np.array(crop_tile)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 235) & (g > 235) & (b > 235)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            res.save(f"{output_dir}/real_sugar_{bear_names[i]}.png")
            print(f"Saved real_sugar_{bear_names[i]}.png")
except Exception as e:
    print(f"Error: {e}")

# 4. media__1785684944159.png (3 Pastel Sugar Bunnies: Yellow, Purple, Orange - White BG)
try:
    path = os.path.join(folder, 'media__1785684944159.png')
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    strip_w = w // 3
    bunny_names = ["yellow_bunny", "purple_bunny", "orange_bunny"]
    for i in range(3):
        crop_tile = img.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        arr = np.array(crop_tile)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 235) & (g > 235) & (b > 235)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            res.save(f"{output_dir}/real_pastel_{bunny_names[i]}.png")
            print(f"Saved real_pastel_{bunny_names[i]}.png")
except Exception as e:
    print(f"Error: {e}")

# 5. media__1785684944153.png (Sea Animals Gummies - White BG)
try:
    path = os.path.join(folder, 'media__1785684944153.png')
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    rows, cols = 4, 3
    tile_w = w // cols
    tile_h = h // rows
    count = 0
    for r in range(rows):
        for c in range(cols):
            crop_tile = img.crop((c * tile_w, r * tile_h, (c + 1) * tile_w, (r + 1) * tile_h))
            arr = np.array(crop_tile)
            red, grn, blu, alp = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
            white_mask = (red > 230) & (grn > 230) & (blu > 230)
            arr[white_mask, 3] = 0
            res = Image.fromarray(arr)
            bbox = res.getbbox()
            if bbox and (bbox[2] - bbox[0] > 30) and (bbox[3] - bbox[1] > 30):
                res = res.crop(bbox)
                res.thumbnail((130, 130), Image.Resampling.LANCZOS)
                res.save(f"{output_dir}/real_sea_gummy_{count+1}.png")
                count += 1
                print(f"Saved real_sea_gummy_{count}.png")
except Exception as e:
    print(f"Error: {e}")

print(f"Total pure real jelly product PNGs created: {len(glob.glob(f'{output_dir}/*.png'))}")
