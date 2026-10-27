import re

with open('_reference_kigo/index.CY5he_ku.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for prefix in ['.hero', '.home-clients', '.sakura-hero', '.home-reel', '.home__content', '.home__group']:
    matches = re.findall(rf'{re.escape(prefix)}[^{{]*\{{[^}}]*\}}', text)
    print(f"Matches for {prefix}: {len(matches)}")
