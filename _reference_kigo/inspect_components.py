import re

files = ['WorkSection.DUSwICN7.css', 'WorkPostcard.C34s6Bd8.css', 'HomeTeam.gle-pIYe.css', 'index.CY5he_ku.css']

for fname in files:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    print(f"\n=================== {fname} ({len(content)} chars) ===================")
    # find selectors
    selectors = re.findall(r'([\.#][a-zA-Z0-9_\-\[\]=:*]+)\s*\{', content)
    print("Selectors preview:", set(selectors[:25]))
