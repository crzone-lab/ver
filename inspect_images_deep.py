from PIL import Image
import glob, os
import numpy as np

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
files = sorted(glob.glob(folder + '*'), key=os.path.getmtime, reverse=True)

print("Deep inspection of image files...")

for f in files:
    try:
        img = Image.open(f).convert("RGB")
        w, h = img.size
        # Skip long vertical chat screenshots (typically ~540x1024)
        if h > 900 and w < 600:
            continue
            
        arr = np.array(img)
        # Calculate color histograms to detect white background images
        r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
        white_pixels = np.sum((r > 240) & (g > 240) & (b > 240))
        black_pixels = np.sum((r < 15) & (g < 15) & (b < 15))
        total_pixels = w * h
        
        white_ratio = white_pixels / total_pixels
        black_ratio = black_pixels / total_pixels
        
        filename = os.path.basename(f)
        if white_ratio > 0.35 or black_ratio > 0.35:
            print(f"CANDIDATE JELLY PHOTO: {filename} | size: {w}x{h} | White: {white_ratio:.2f} | Black: {black_ratio:.2f}")
    except Exception as e:
        pass
