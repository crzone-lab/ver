from PIL import Image
import glob, os

folder = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
files = sorted(glob.glob(folder + '*'), key=os.path.getmtime, reverse=True)

print(f"Scanning all {len(files)} files in .user_uploaded sorted by newest timestamp...")

for f in files:
    try:
        img = Image.open(f)
        w, h = img.size
        # Check aspect ratio - chat screenshots are phone aspect ratio (e.g. 540x1024, 550x1024, etc.)
        # Original uploaded photos usually have different aspect ratios (e.g. 1024x1024 square, 1024x956, etc.)
        aspect = w / h
        filename = os.path.basename(f)
        print(f"File: {filename} | Size: {w}x{h} | Aspect: {aspect:.2f} | Path: {f}")
    except Exception as e:
        pass
