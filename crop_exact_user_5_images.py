import os, glob
from PIL import Image
import numpy as np

output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

# 1. Clear output directory
for f in glob.glob(f'{output_dir}/*'):
    os.remove(f)

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'

# Let's target the exact newest files uploaded by user:
# media_1785742520040.png (1024x620)
# media_1785742274547.png (1024x671)
# media_1785742428641.png (746x1024)
# media_1785742428609.png (1024x1024)
# media_1785742428595.png (1024x1024)
# media_1785742428567.png (1024x1024)

files_to_crop = [
    'media_1785742520040.png',
    'media_1785742274547.png',
    'media_1785742428641.png',
    'media_1785742428609.png',
    'media_1785742428595.png',
    'media_1785742428567.png'
]

sprite_count = 0

for filename in files_to_crop:
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        img = Image.open(path).convert("RGBA")
        w, h = img.size
        arr = np.array(img)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        
        # Check background color (white vs black)
        corner_r = r[:10, :10].mean()
        if corner_r > 200:
            # White background
            bg_mask = (r > 230) & (g > 230) & (b > 230)
        else:
            # Black background
            bg_mask = (r < 30) & (g < 30) & (b < 30)
            
        arr[bg_mask, 3] = 0
        res = Image.fromarray(arr)
        
        # Crop into sub-items or bounding box
        if w > 800 and h > 500:
            # Grid crop into 3x3 tiles
            rows, cols = 3, 3
            tw, th = w // cols, h // rows
            for row in range(rows):
                for col in range(cols):
                    tile = res.crop((col * tw, row * th, (col + 1) * tw, (row + 1) * th))
                    bbox = tile.getbbox()
                    if bbox and (bbox[2] - bbox[0] > 30) and (bbox[3] - bbox[1] > 30):
                        tile = tile.crop(bbox)
                        tile.thumbnail((140, 140), Image.Resampling.LANCZOS)
                        out_p = f"{output_dir}/real_jelly_candy_{sprite_count+1}.png"
                        tile.save(out_p)
                        sprite_count += 1
                        print(f"Saved {out_p} from {filename}")
        else:
            bbox = res.getbbox()
            if bbox:
                res = res.crop(bbox)
                res.thumbnail((160, 160), Image.Resampling.LANCZOS)
                out_p = f"{output_dir}/real_jelly_candy_{sprite_count+1}.png"
                res.save(out_p)
                sprite_count += 1
                print(f"Saved {out_p} from {filename}")

print(f"Total extracted real jelly candy PNGs: {sprite_count}")
