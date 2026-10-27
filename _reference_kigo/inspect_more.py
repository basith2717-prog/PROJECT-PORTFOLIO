import re

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's see what is inside the Nuxt state or payload, or what components are loaded
matches = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Total script tags: {len(matches)}")

# Check for Nuxt payload or data
for idx, s in enumerate(matches):
    if len(s) > 100:
        print(f"Script {idx}: length {len(s)}, preview: {s[:200]}")

# Let's find all words or IDs
with open('extracted_scripts.txt', 'w', encoding='utf-8') as out:
    for idx, s in enumerate(matches):
        if '__NUXT_DATA__' in s or 'window.__NUXT__' in s or 'payload' in s or len(s) > 500:
            out.write(f"\n--- SCRIPT {idx} ---\n")
            out.write(s)

print("Done extracting scripts")
