import re

with open('_reference_kigo/entry.Bmo6-XxB.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's inspect the first 25 rules
clean = re.sub(r'\[data-v-[a-z0-9]+\]', '', text)
rules = [r.strip() for r in clean.split('}') if r.strip()]
print(f"Total rules in entry: {len(rules)}")
for r in rules[:25]:
    sel = r.split('{')[0].strip().replace('\n', ' ')
    print("  ", sel)
