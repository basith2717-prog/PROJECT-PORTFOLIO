import re
import json

with open('extracted_scripts.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

# Let's find strings inside the script
matches = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', txt)
unique_strings = []
for m in matches:
    if len(m) > 3 and m not in unique_strings:
        unique_strings.append(m)

with open('nuxt_strings.txt', 'w', encoding='utf-8') as out:
    for s in unique_strings:
        out.write(s + '\n')

print(f"Total unique strings extracted: {len(unique_strings)}")
