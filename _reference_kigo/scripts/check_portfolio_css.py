import re

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

keywords = ['home-work', 'home-team', 'home-contact', 'site-footer', 'team-card', 'work-filter', 'postcard']
for kw in keywords:
    matches = re.findall(rf'([^{{}}]+)\{{[^{{}}]*{kw}[^{{}}]*\}}', css)
    matches2 = re.findall(rf'([^{{}}]*\.{kw}[^{{}}]*)\{{', css)
    print(f"Keyword '{kw}': {len(matches2)} rule selectors")
    for s in matches2[:3]:
        print("   ", s.strip()[:60])
