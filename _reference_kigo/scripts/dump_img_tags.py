import re
from bs4 import BeautifulSoup

with open(r"_reference_kigo\kigo_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

imgs = soup.find_all("img")
print(f"Total img tags: {len(imgs)}")
for i, img in enumerate(imgs):
    src = img.get("src", "")
    alt = img.get("alt", "")
    cls = img.get("class", [])
    parent = img.parent.name if img.parent else ""
    parent_cls = img.parent.get("class", []) if img.parent else []
    print(f"[{i+1}] src={src[:60]} | alt='{alt}' | class={cls} | parent={parent}.{parent_cls}")
