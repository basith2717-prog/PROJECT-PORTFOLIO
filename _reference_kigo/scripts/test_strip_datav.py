import os
import re
from bs4 import BeautifulSoup

ref_files = [
    'entry.Bmo6-XxB.css',
    'index.CY5he_ku.css',
    'WorkSection.DUSwICN7.css',
    'WorkPostcard.C34s6Bd8.css',
    'HomeTeam.gle-pIYe.css',
    'IllustratedFaq.CKUH9x3P.css',
    'ProjectCardMarks.VZ1WhnK8.css',
    'MoreCalligraphy.DceKB5ZG.css',
    'useWorkProjects.Dt8yYixg.css'
]

combined_ref_css = ""
for rf in ref_files:
    path = os.path.join('_reference_kigo', rf)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            combined_ref_css += f"\n/* === SOURCE: {rf} === */\n" + f.read()

# Strip all [data-v-xxxxxxx]
clean_css = re.sub(r'\[data-v-[a-z0-9]+\]', '', combined_ref_css)

# Also let's check how many classes in index.html match!
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

html_classes = set()
for tag in soup.find_all(True):
    for c in tag.get('class', []):
        html_classes.add(c)

css_classes = set(re.findall(r'\.([a-zA-Z0-9_\-]+)', clean_css))

missing = html_classes - css_classes
present = html_classes & css_classes

print(f"Total HTML classes: {len(html_classes)}")
print(f"Total clean Kigo CSS classes: {len(css_classes)}")
print(f"Matches: {len(present)} / {len(html_classes)}")
print(f"Missing count: {len(missing)}")
print("Remaining missing classes (if any):")
for m in sorted(missing)[:30]:
    print(" -", m)
