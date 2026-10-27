import re
import urllib.request
import urllib.parse
import os

with open('_reference_kigo/kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find all image URLs
img_urls = re.findall(r'(?:src|url)=["\']([^"\']+\.(?:png|webp|jpg|svg))["\']', html)
netlify_urls = re.findall(r'url=([^"\'&]+\.(?:webp|png|jpg|svg))', html)

all_images = set(img_urls + netlify_urls)
print(f"Found {len(all_images)} image references")

os.makedirs('public/images/sakura', exist_ok=True)
os.makedirs('public/images/clients', exist_ok=True)

for img in all_images:
    decoded = urllib.parse.unquote(img)
    clean_path = decoded.lstrip('/')
    if clean_path.startswith('images/'):
        target = os.path.join('public', clean_path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        full_url = f"https://kigo.studio/{clean_path}"
        try:
            print(f"Downloading {full_url} -> {target}")
            urllib.request.urlretrieve(full_url, target)
        except Exception as e:
            print(f"Failed {full_url}: {e}")
