import re

with open('_reference_kigo/entry.Bmo6-XxB.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = re.findall(r'\.header[^{]*\{[^}]*\}', text)
print(f"Matches for .header in entry: {len(matches)}")
for m in matches[:5]:
    print("  ", m[:120])
