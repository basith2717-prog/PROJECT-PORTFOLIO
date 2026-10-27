import os
from PIL import Image

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"

for f in sorted(os.listdir(img_dir)):
    p = os.path.join(img_dir, f)
    if f.endswith(('.webp', '.jpeg', '.jpg', '.png', '.gif')):
        im = Image.open(p)
        print(f"\n--- {f} ---")
        print(f"Format: {im.format}, Size: {im.size}, Mode: {im.mode}")
        # check if there's any info or text chunk
        print(f"Info keys: {list(im.info.keys())}")
