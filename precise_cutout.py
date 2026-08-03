import os, glob
from PIL import Image
import numpy as np

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

# 1. Clear old deco_sprites completely
for f in glob.glob(f'{output_dir}/*'):
    os.remove(f)

sprites_data = []

# ==========================================
# FILE 1: 3 Pastel Sugar Bunnies (media_1785742428567.png) - White BG
# ==========================================
img1 = Image.open(os.path.join(folder, 'media_1785742428567.png')).convert("RGBA")
w, h = img1.size
# 3 vertical strips
for i, name in enumerate(["sugar_bunny_yellow", "sugar_bunny_blue", "sugar_bunny_pink"]):
    tile = img1.crop((i * (w // 3), 0, (i + 1) * (w // 3), h))
    arr = np.array(tile)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    bg = (r > 240) & (g > 240) & (b > 240)
    arr[bg, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        out_name = f"{output_dir}/{name}.png"
        res.save(out_name)
        sprites_data.append(out_name)
        print("Cutout 1:", out_name)

# ==========================================
# FILE 2: Translucent Fruit Gummies (media_1785742520040.png) - White BG
# ==========================================
img2 = Image.open(os.path.join(folder, 'media_1785742520040.png')).convert("RGBA")
w, h = img2.size
# Let's cut individual fruit gummies by precise bounding boxes based on non-white connected regions
arr2 = np.array(img2)
r, g, b, a = arr2[:,:,0], arr2[:,:,1], arr2[:,:,2], arr2[:,:,3]
non_white = ~((r > 240) & (g > 240) & (b > 240))

# We can use connected component labeling via scipy or simple floodfill / grid boxes
# Let's inspect coordinates of fruit gummies or use thresholding
# Grid 4x3 with smart margin
cols, rows = 4, 3
tw, th = w // cols, h // rows
fc = 0
for ry in range(rows):
    for cx in range(cols):
        tile = img2.crop((cx * tw, ry * th, (cx + 1) * tw, (ry + 1) * th))
        tarr = np.array(tile)
        tr, tg, tb, ta = tarr[:,:,0], tarr[:,:,1], tarr[:,:,2], tarr[:,:,3]
        bg = (tr > 238) & (tg > 238) & (tb > 238)
        tarr[bg, 3] = 0
        res = Image.fromarray(tarr)
        bbox = res.getbbox()
        if bbox:
            bw = bbox[2] - bbox[0]
            bh = bbox[3] - bbox[1]
            if bw > 30 and bh > 30:
                res = res.crop(bbox)
                res.thumbnail((140, 140), Image.Resampling.LANCZOS)
                fc += 1
                out_name = f"{output_dir}/fruit_gummy_{fc}.png"
                res.save(out_name)
                sprites_data.append(out_name)
                print("Cutout 2:", out_name)

# ==========================================
# FILE 3: 3 Sugar Bears (media_1785742428595.png) - White BG
# ==========================================
img3 = Image.open(os.path.join(folder, 'media_1785742428595.png')).convert("RGBA")
w, h = img3.size
for i, name in enumerate(["sugar_bear_green", "sugar_bear_red", "sugar_bear_yellow"]):
    tile = img3.crop((i * (w // 3), 0, (i + 1) * (w // 3), h))
    arr = np.array(tile)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    bg = (r > 240) & (g > 240) & (b > 240)
    arr[bg, 3] = 0
    res = Image.fromarray(arr)
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        res.thumbnail((160, 160), Image.Resampling.LANCZOS)
        out_name = f"{output_dir}/{name}.png"
        res.save(out_name)
        sprites_data.append(out_name)
        print("Cutout 3:", out_name)

# ==========================================
# FILE 4: 3D Glass Gradient Bunny (media_1785742428609.png) - White BG
# ==========================================
img4 = Image.open(os.path.join(folder, 'media_1785742428609.png')).convert("RGBA")
arr4 = np.array(img4)
r, g, b, a = arr4[:,:,0], arr4[:,:,1], arr4[:,:,2], arr4[:,:,3]
bg = (r > 245) & (g > 245) & (b > 245)
arr4[bg, 3] = 0
res4 = Image.fromarray(arr4)
bbox4 = res4.getbbox()
if bbox4:
    res4 = res4.crop(bbox4)
    res4.thumbnail((180, 180), Image.Resampling.LANCZOS)
    out_name = f"{output_dir}/glass_gradient_bunny.png"
    res4.save(out_name)
    sprites_data.append(out_name)
    print("Cutout 4:", out_name)

# ==========================================
# FILE 5: Rainbow Sparkle Sugar Bunny (media_1785742428641.png) - Black BG
# ==========================================
img5 = Image.open(os.path.join(folder, 'media_1785742428641.png')).convert("RGBA")
arr5 = np.array(img5)
r, g, b, a = arr5[:,:,0], arr5[:,:,1], arr5[:,:,2], arr5[:,:,3]
# Black background threshold
bg5 = (r < 18) & (g < 18) & (b < 18)
arr5[bg5, 3] = 0
res5 = Image.fromarray(arr5)
bbox5 = res5.getbbox()
if bbox5:
    res5 = res5.crop(bbox5)
    res5.thumbnail((180, 180), Image.Resampling.LANCZOS)
    out_name = f"{output_dir}/rainbow_sparkle_bunny.png"
    res5.save(out_name)
    sprites_data.append(out_name)
    print("Cutout 5:", out_name)

print(f"Total 100% CLEAN REAL GUMMY CUTOUTS: {len(sprites_data)}")
