import re

with open('_reference_kigo/entry.Bmo6-XxB.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for target in ['body{', '#__nuxt{', 'main{', '.scrollable{', '.header{', '.hero{']:
    idx = text.find(target)
    if idx != -1:
        end = text.find('}', idx)
        print(f"--- {target} ---")
        print(text[idx:end+1])
    else:
        print(f"NOT FOUND: {target}")
