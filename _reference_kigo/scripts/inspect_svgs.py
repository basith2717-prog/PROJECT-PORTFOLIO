import os

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"

# Check SVGs
for f in os.listdir(img_dir):
    if f.endswith('.svg'):
        path = os.path.join(img_dir, f)
        print(f"\n=== SVG: {f} ===")
        with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
            data = fp.read()
            print(data[:300])

