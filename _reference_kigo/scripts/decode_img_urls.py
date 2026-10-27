import re
import urllib.parse
from bs4 import BeautifulSoup

with open(r"_reference_kigo\kigo_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

imgs = soup.find_all("img")
print(f"Total img tags: {len(imgs)}")
decoded_urls = []
for i, img in enumerate(imgs):
    src = img.get("src", "")
    alt = img.get("alt", "")
    cls = " ".join(img.get("class", []))
    
    # decode netlify url if present
    match = re.search(r'url=([^&]+)', src)
    if match:
        original_path = urllib.parse.unquote(match.group(1))
    else:
        original_path = src
    print(f"[{i+1}] {original_path} | alt='{alt}' | class='{cls}'")
    decoded_urls.append({
        "index": i+1,
        "src": src,
        "path": original_path,
        "alt": alt,
        "class": cls
    })
