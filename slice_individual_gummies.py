import os, glob
from PIL import Image
import numpy as np

output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

# 1. Slice media__1785684944159 (3 Pastel Bunnies: Yellow, Purple, Orange)
try:
    img_bunnies = Image.open('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/media__1785684944159.png').convert("RGBA")
    w, h = img_bunnies.size
    # 3 vertical strips
    strip_w = w // 3
    for i in range(3):
        crop_b = img_bunnies.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        # Remove white bg
        arr = np.array(crop_b)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 240) & (g > 240) & (b > 240)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            res.save(f"{output_dir}/real_bunny_{i+1}.png")
            print(f"Saved real_bunny_{i+1}.png")
except Exception as e:
    print(f"Error slicing bunnies: {e}")

# 2. Slice media__1785685340954 (3 Sugar Bears: Green, Red, Yellow)
try:
    img_bears = Image.open('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/media__1785685340954.png').convert("RGBA")
    w, h = img_bears.size
    strip_w = w // 3
    for i in range(3):
        crop_b = img_bears.crop((i * strip_w, 0, (i + 1) * strip_w, h))
        arr = np.array(crop_b)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        white_mask = (r > 240) & (g > 240) & (b > 240)
        arr[white_mask, 3] = 0
        res = Image.fromarray(arr)
        bbox = res.getbbox()
        if bbox:
            res = res.crop(bbox)
            res.thumbnail((140, 140), Image.Resampling.LANCZOS)
            res.save(f"{output_dir}/real_sugar_bear_{i+1}.png")
            print(f"Saved real_sugar_bear_{i+1}.png")
except Exception as e:
    print(f"Error slicing sugar bears: {e}")

# 3. Slice media__1785685763152 (Gradient Glass Bunny)
try:
    img_grad = Image.open('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/media__1785685763152.png').convert("RGBA")
    arr = np.array(img_grad)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    white_mask = (r > 240) & (g > 240) & (b > 240)
    arr[white_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        res.save(f"{output_dir}/real_gradient_bunny.png")
        print("Saved real_gradient_bunny.png")
except Exception as e:
    print(f"Error slicing gradient bunny: {e}")

# 4. Slice media__1785683872412 (Rainbow Sparkle Bunny - remove black bg)
try:
    img_sparkle = Image.open('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/media__1785683872412.png').convert("RGBA")
    arr = np.array(img_sparkle)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    black_mask = (r < 25) & (g < 25) & (b < 25)
    arr[black_mask, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        res.save(f"{output_dir}/real_sparkle_bunny.png")
        print("Saved real_sparkle_bunny.png")
except Exception as e:
    print(f"Error slicing sparkle bunny: {e}")

# 5. Slice media__1785684944153 (Sea Animals: Crabs, Fish, Turtles, Seahorses, Starfish)
try:
    img_sea = Image.open('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/media__1785684944153.png').convert("RGBA")
    w, h = img_sea.size
    rows, cols = 4, 3
    tile_w = w // cols
    tile_h = h // rows
    sea_count = 0
    for r in range(rows):
        for c in range(cols):
            crop_tile = img_sea.crop((c * tile_w, r * tile_h, (c + 1) * tile_w, (r + 1) * tile_h))
            arr = np.array(crop_tile)
            red, grn, blu, alp = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
            white_mask = (red > 235) & (grn > 235) & (blu > 235)
            arr[white_mask, 3] = 0
            res = Image.fromarray(arr)
            bbox = res.getbbox()
            if bbox and (bbox[2] - bbox[0] > 20) and (bbox[3] - bbox[1] > 20):
                res = res.crop(bbox)
                res.thumbnail((130, 130), Image.Resampling.LANCZOS)
                res.save(f"{output_dir}/real_sea_{sea_count+1}.png")
                sea_count += 1
                print(f"Saved real_sea_{sea_count}.png")
except Exception as e:
    print(f"Error slicing sea animals: {e}")

print("100% Sliced all individual real product gummies!")
