import re

with open('_reference_kigo/kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

hero_match = re.search(r'<div class="hero"[^>]*>(.*?)<section class="home-clients"', html, re.DOTALL)
if hero_match:
    with open('hero_snippet.html', 'w', encoding='utf-8') as out:
        out.write(hero_match.group(0))
    print("Wrote hero_snippet.html, length:", len(hero_match.group(0)))
else:
    print("Hero section not found by regex")
