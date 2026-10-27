import os
import re

ref_order = [
    'entry.Bmo6-XxB.css',
    'index.CY5he_ku.css',
    'IllustratedFaq.CKUH9x3P.css',
    'WorkSection.DUSwICN7.css',
    'WorkPostcard.C34s6Bd8.css',
    'HomeTeam.gle-pIYe.css',
    'ProjectCardMarks.VZ1WhnK8.css',
    'MoreCalligraphy.DceKB5ZG.css',
    'useWorkProjects.Dt8yYixg.css'
]

combined_ref = ""
for rf in ref_order:
    p = os.path.join('_reference_kigo', rf)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            combined_ref += f"\n/* =================== FROM {rf} =================== */\n"
            combined_ref += f.read()

# Strip all [data-v-xxxxxx]
clean = re.sub(r'\[data-v-[a-z0-9]+\]', '', combined_ref)

print(f"Extracted {len(clean)} characters of clean Kigo CSS")

# Check what body, #__nuxt, and main are doing in this clean css
for tag in ['body', '#__nuxt', 'main', '.scrollable']:
    matches = re.findall(rf'(?:^|\}}|\s)({re.escape(tag)}\s*\{{[^}}]*\}})', clean)
    print(f"\nRules for {tag} ({len(matches)}):")
    for m in matches:
        print("  ", m.strip())
