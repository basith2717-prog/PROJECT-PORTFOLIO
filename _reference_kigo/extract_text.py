import re

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's find all text blocks and elements
print("=== TEXT SNIPPETS ===")
# find paragraphs, list items, buttons
for tag in ['p', 'button', 'a', 'span']:
    items = re.findall(rf'<{tag}[^>]*>(.*?)</{tag}>', html, re.DOTALL | re.I)
    cleaned = []
    for it in items:
        c = re.sub(r'<[^>]+>', ' ', it).strip()
        c = ' '.join(c.split())
        if len(c) > 15 and c not in cleaned:
            cleaned.append(c)
    print(f"\n--- {tag} (sample {len(cleaned)}) ---")
    for c in cleaned[:10]:
        print(" •", c[:120])
