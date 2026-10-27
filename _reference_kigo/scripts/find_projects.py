import re
import urllib.parse
from bs4 import BeautifulSoup

with open(r"_reference_kigo\kigo_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Search for work projects in script tags or html
matches = re.findall(r'/images/projects/[^"\'\s&]+', html)
print(f"Direct project matches: {set(matches)}")

# Search for any string mentioning llul, minu, pago, recken, us
for kw in ['llul', 'minu', 'pago', 'recken', 'us', 'celtrev', 'brio']:
    hits = re.findall(rf'[^"\'>\s]*{kw}[^"\'<\s]*', html, re.I)
    print(f"Keyword '{kw}' matches ({len(hits)}): {set(hits[:6])}")
