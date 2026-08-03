import os, glob
from PIL import Image, ImageChops
import numpy as np

output_dir = 'deco_sprites'
os.makedirs(output_dir, exist_ok=True)

uploaded_files = sorted(glob.glob('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/*'))
print(f"Found {len(uploaded_files)} total uploaded files.")

sprite_count = 0

def remove_background_white(img_path):
    img = Image.open(img_path).convert("RGBA")
    data = np.array(img)
    
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Identify near-white background pixels (R>235, G>235, B>235)
    white_mask = (r > 230) & (g > 230) & (b > 230)
    
    # Set alpha to 0 for white background
    data[white_mask, 3] = 0
    
    # Smooth edges with slight alpha transition
    near_white_mask = (r > 215) & (g > 215) & (b > 215) & ~white_mask
    data[near_white_mask, 3] = 160
    
    return Image.fromarray(data)

def remove_background_black(img_path):
    img = Image.open(img_path).convert("RGBA")
    data = np.array(img)
    
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # Identify near-black background pixels (R<25, G<25, B<25)
    black_mask = (r < 25) & (g < 25) & (b < 25)
    data[black_mask, 3] = 0
    
    return Image.fromarray(data)

# Process each uploaded image
for idx, filepath in enumerate(uploaded_files[-12:]):
    try:
        raw_img = Image.open(filepath)
        print(f"Processing image {idx}: {os.path.basename(filepath)}, size: {raw_img.size}")
        
        # Check if background is mostly black or white
        img_rgba = raw_img.convert("RGBA")
        arr = np.array(img_rgba)
        corner_pixels = arr[:20, :20, :3]
        avg_corner = np.mean(corner_pixels)
        
        if avg_corner < 40:
            transparent_img = remove_background_black(filepath)
        else:
            transparent_img = remove_background_white(filepath)
            
        # Extract individual connected components or grid tiles
        w, h = transparent_img.size
        
        # Crop into 2x2 or 3x3 tiles if large grid, or crop bounding box
        # Save transparent sprite
        out_name = f"{output_dir}/real_jelly_{sprite_count}.png"
        
        # Trim transparent borders
        bbox = transparent_img.getbbox()
        if bbox:
            cropped = transparent_img.crop(bbox)
            # Resize into crisp max 160x160 thumbnail
            cropped.thumbnail((160, 160), Image.Resampling.LANCZOS)
            
            # Save sprite
            cropped.save(out_name)
            sprite_count += 1
            print(f"Saved real jelly sprite: {out_name}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

print(f"Total extracted real jelly sprites: {sprite_count}")
