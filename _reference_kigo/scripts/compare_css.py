import re

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    local_css = f.read()

# Let's inspect sections in local_css
sections = re.findall(r'/\* ==+ (.*?) ==+ \*/', local_css)
print("Sections in style.css:")
for s in sections:
    print(" -", s)

# Let's check some major classes in style.css vs original css
ref_css_files = ['entry.Bmo6-XxB.css', 'index.CY5he_ku.css', 'WorkSection.DUSwICN7.css', 'WorkPostcard.C34s6Bd8.css', 'HomeTeam.gle-pIYe.css', 'IllustratedFaq.CKUH9x3P.css']

all_ref_css = ""
for f in ref_css_files:
    with open(f'_reference_kigo/{f}', 'r', encoding='utf-8', errors='ignore') as rf:
        all_ref_css += rf.read() + "\n"

print(f"\nTotal original reference CSS size: {len(all_ref_css)} chars")
print(f"Total local style.css size: {len(local_css)} chars")
