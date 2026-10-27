import os
import glob
from PIL import Image

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"
files = os.listdir(img_dir)

print(f"Total files in IMG: {len(files)}")

for f in sorted(files):
    path = os.path.join(img_dir, f)
    size = os.path.getsize(path)
    if f.endswith('.svg'):
        with open(path, 'r', encoding='utf-8', errors='ignore') as s:
            content = s.read()[:250].replace('\n', ' ')
        print(f"SVG: {f} ({size} bytes) -> {content[:100]}")
    elif f.endswith(('.webp', '.jpeg', '.jpg', '.png', '.gif')):
        try:
            with Image.open(path) as img:
                print(f"IMG: {f} ({size} bytes) -> format={img.format}, size={img.size}, mode={img.mode}")
        except Exception as e:
            print(f"IMG: {f} ({size} bytes) -> Error opening: {e}")
