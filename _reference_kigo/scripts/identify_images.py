import os
from PIL import Image

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"

for f in sorted(os.listdir(img_dir)):
    if f.endswith(('.webp', '.jpeg', '.jpg', '.png', '.gif')):
        p = os.path.join(img_dir, f)
        im = Image.open(p)
        # analyze corners and center
        w, h = im.size
        center = im.convert('RGB').crop((w//4, h//4, 3*w//4, 3*h//4)).resize((1, 1)).getpixel((0, 0))
        top_left = im.convert('RGB').crop((0, 0, w//4, h//4)).resize((1, 1)).getpixel((0, 0))
        print(f"{f}: {w}x{h}, Center RGB={center}, TopLeft RGB={top_left}")
