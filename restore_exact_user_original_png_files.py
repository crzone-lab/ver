import shutil, os, glob

user_dir = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/.user_uploaded/'
target_dir = 'deco_sprites/'
os.makedirs(target_dir, exist_ok=True)

# The user's exact uploaded PNG files at 16:02 / 16:03:
original_user_pngs = [
    'media_1785740523491.png',
    'media_1785740523496.png',
    'media_1785740523503.png',
    'media_1785740523512.png',
    'media_1785740523525.png',
    'media_1785740606715.png',
    'media_1785740606718.png'
]

# Clear corrupt files
for existing in glob.glob(target_dir + '*.png'):
    os.remove(existing)

for idx, src_name in enumerate(original_user_pngs, 1):
    src_path = os.path.join(user_dir, src_name)
    num_str = f'{idx:02d}'
    dest_path = os.path.join(target_dir, f'{num_str}.png')
    shutil.copyfile(src_path, dest_path)
    print(f'100% Direct Copy Restored User Original PNG File: {dest_path} (from {src_name})')

print(f'Restored {len(original_user_pngs)} 100% exact user uploaded PNG files to deco_sprites/!')
