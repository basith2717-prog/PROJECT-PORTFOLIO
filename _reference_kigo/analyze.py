import re

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print('--- TITLE ---')
for m in re.finditer(r'<title>(.*?)</title>', html, re.I):
    print(m.group(1))

print('\n--- HEADINGS ---')
for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.DOTALL | re.I):
    clean = re.sub(r'<[^>]+>', ' ', m.group(2))
    clean = ' '.join(clean.split())
    print(f"{m.group(1)}: {clean}")

print('\n--- KEY CLASSES & CONTAINERS ---')
classes = set(re.findall(r'class="([^"]+)"', html))
key_classes = [c for c in classes if any(k in c for k in ['hero', 'service', 'client', 'project', 'nav', 'reel', 'cursor', 'petal', 'flower', 'footer', 'award', 'about', 'work', 'card', 'slider', 'marquee'])]
for c in sorted(key_classes)[:50]:
    print(c)
