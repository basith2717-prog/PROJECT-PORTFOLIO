import os
import re
import json
from PIL import Image

extracted_dir = r"c:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\extracted_kigo"
raw_html_path = r"c:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\_reference_kigo\kigo_raw.html"

with open(raw_html_path, "r", encoding="utf-8", errors="ignore") as f:
    raw_html = f.read()

# Find all image URLs in raw_html
img_srcs = set(re.findall(r'src=["\']([^"\']+\.(?:webp|png|jpg|jpeg|gif|svg))', raw_html, re.I))
img_srcs.update(re.findall(r'srcset=["\']([^"\']+)["\']', raw_html, re.I))

# Analyze extracted files
files = os.listdir(extracted_dir)
print(f"Total files in extracted_kigo: {len(files)}")

info_list = []
for fname in sorted(files):
    fpath = os.path.join(extracted_dir, fname)
    ext = os.path.splitext(fname)[1].lower()
    size = os.path.getsize(fpath)
    dimensions = None
    if ext in [".webp", ".png", ".jpg", ".jpeg", ".gif"]:
        try:
            with Image.open(fpath) as img:
                dimensions = f"{img.width}x{img.height}"
        except Exception as e:
            dimensions = str(e)
    info_list.append({
        "file": fname,
        "size": size,
        "dims": dimensions,
        "ext": ext
    })

# Print summary of categories
with open(r"c:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\_reference_kigo\zip_images_summary.json", "w", encoding="utf-8") as out:
    json.dump(info_list, out, indent=2)

print("Saved zip_images_summary.json with", len(info_list), "entries")
