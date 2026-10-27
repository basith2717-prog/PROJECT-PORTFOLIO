import re

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# remove comments
clean = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
# find all selectors before {
selectors = [s.strip() for s in re.findall(r'([^{}]+)\{', clean)]
# print distinct top-level class names found in selectors
classes = set()
for s in selectors:
    if s.startswith('@'):
        continue
    for c in re.findall(r'\.([a-zA-Z0-9_\-]+)', s):
        classes.add(c)

print(f"Total unique classes targeted in style.css: {len(classes)}")
print("First 80 classes targeted in style.css:")
print(", ".join(sorted(classes)[:80]))
