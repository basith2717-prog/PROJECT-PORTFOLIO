import glob
import re

css_files = glob.glob("*.css")
print("Found CSS files:", css_files)

all_keyframes = set()
for f in css_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        kfs = re.findall(r'@keyframes\s+([a-zA-Z0-9_-]+)', c)
        for k in kfs:
            all_keyframes.add((f, k))

print("\n--- ALL KEYFRAMES ---")
for f, k in sorted(all_keyframes):
    print(f"{f}: {k}")

# Check fonts
fonts = set()
for f in css_files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        ff = re.findall(r'font-family:\s*([^;}]+)', c)
        for fam in ff:
            fonts.add(fam.strip())

print("\n--- FONTS USED ---")
for fnt in sorted(fonts)[:15]:
    print(fnt)
