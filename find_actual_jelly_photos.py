from PIL import Image
import glob, os
import numpy as np

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
files = sorted(glob.glob(folder + '*'))

print("Scanning for actual real jelly photos...")

for f in files:
    try:
        img = Image.open(f).convert("RGB")
        w, h = img.size
        arr = np.array(img)
        
        # Calculate color variance and background color
        # Chat UI has large pink areas (#ff4757, #ff6b81, pink/salmon background)
        # Real jelly photos have white background (#ffffff) or black background (#000000)
        
        corner_r = arr[:15, :15, 0].mean()
        corner_g = arr[:15, :15, 1].mean()
        corner_b = arr[:15, :15, 2].mean()
        
        # Check if background is pure white (>230, >230, >230) or pure black (<30, <30, <30)
        is_white_bg = (corner_r > 230) and (corner_g > 230) and (corner_b > 230)
        is_black_bg = (corner_r < 30) and (corner_g < 30) and (corner_b < 30)
        
        if is_white_bg or is_black_bg:
            print(f"FOUND JELLY PHOTO: {os.path.basename(f)} | Size: {w}x{h} | BG: {'WHITE' if is_white_bg else 'BLACK'}")
    except Exception as e:
        pass
