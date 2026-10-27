import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print(f"HTML length: {len(html)}")
print(f"CSS length: {len(css)}")

sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', html)
print("Sections found:")
for s in sections:
    print(" -", s)

# Let's inspect the first 100 lines of index.html
print("\n--- First 40 lines of index.html ---")
lines = html.splitlines()
for l in lines[:40]:
    print(l)
