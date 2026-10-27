import re

with open('_reference_kigo/entry.Bmo6-XxB.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find header nav layout
for kw in ['grid-template-columns', 'contact-postcard-cta', 'language', 'header__navigation']:
    matches = re.findall(rf'[^{{}}]*{kw}[^{{}}]*\{{[^}}]*\}}', text)
    print(f"--- Matches for {kw} ({len(matches)}) ---")
    for m in matches[:3]:
        print(" ", m.strip()[:100])
