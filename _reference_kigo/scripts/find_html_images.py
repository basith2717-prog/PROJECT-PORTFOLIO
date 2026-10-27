import json
import re
from PIL import Image
import os

with open(r"_reference_kigo\kigo_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Find all img src, srcset, data-src, background-image in kigo_raw.html
all_urls = re.findall(r'(?:src|srcset|href|content)=["\']([^"\']+\.(?:webp|png|jpg|jpeg|gif|svg))', html, re.I)
print(f"Total image references found in HTML: {len(all_urls)}")

# Check client logos in html
client_matches = re.findall(r'<img[^>]+alt=["\']([^"\']+)["\'][^>]+>', html)
print(f"Alts found: {len(client_matches)}")
for a in client_matches[:20]:
    print(" ", a)
