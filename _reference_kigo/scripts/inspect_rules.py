import re

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find all comments and major blocks
blocks = re.findall(r'/\* ==+ (.*?) ==+ \*/', text)
print("Comments/Sections in style.css:")
for b in blocks:
    print(" -", b.strip())

# Sample some rules
rules = re.findall(r'([^{]+)\{([^}]+)\}', text)
print(f"\nTotal rules in style.css: {len(rules)}")
for selector, body in rules[20:45]:
    selector = selector.strip().replace('\n', ' ')
    if len(selector) < 60:
        print("  Rule:", selector)
