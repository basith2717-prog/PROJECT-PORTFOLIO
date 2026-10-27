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

print("=== CHECKING RULES IN EACH REF CSS FILE ===")
for rf in ref_order:
    path = os.path.join('_reference_kigo', rf)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    # Strip data-v
    clean = re.sub(r'\[data-v-[a-z0-9]+\]', '', content)
    # Count keyframes
    keyframes = re.findall(r'@keyframes\s+([a-zA-Z0-9_\-]+)', clean)
    print(f"{rf}: {len(clean)} chars, {len(keyframes)} keyframes: {keyframes[:4]}")
