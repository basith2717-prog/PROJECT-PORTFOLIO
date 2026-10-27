import os
import re
from bs4 import BeautifulSoup
import urllib.request

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

imgs = soup.find_all(['img', 'image'])
print(f"Total img/image tags in index.html: {len(imgs)}")

missing_files = []
existing_files = []
for tag in imgs:
    src = tag.get('src') or tag.get('href') or tag.get('xlink:href')
    if not src or src.startswith('data:') or src.startswith('http'):
        continue
    # clean query string
    clean_src = src.split('?')[0].lstrip('./').replace('/', os.sep)
    if os.path.exists(clean_src):
        existing_files.append(src)
    else:
        missing_files.append((src, clean_src))

print(f"Existing images: {len(existing_files)}")
print(f"Missing images: {len(missing_files)}")
for src, clean in missing_files[:15]:
    print(f"  MISSING: {src} -> checked {clean}")
