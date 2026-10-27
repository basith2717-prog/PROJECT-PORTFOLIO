import os
from PIL import Image

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"

for f in sorted(os.listdir(img_dir)):
    if f.endswith(('.webp', '.jpeg', '.jpg', '.png', '.gif')):
        p = os.path.join(img_dir, f)
        with Image.open(p) as im:
            # Let's get dominant colors or info
            im_thumb = im.convert('RGB').resize((10, 10))
            colors = sorted(im_thumb.getcolors(100), key=lambda x: x[0], reverse=True)
            top_color = colors[0][1]
            print(f"{f}: size={im.size}, dominant RGB={top_color}")
