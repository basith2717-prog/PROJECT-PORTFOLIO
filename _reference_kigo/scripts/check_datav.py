import os
import re

ref_css_files = [f for f in os.listdir('_reference_kigo') if f.endswith('.css') and f != 'extracted_styles.css']

for f in ref_css_files:
    path = os.path.join('_reference_kigo', f)
    with open(path, 'r', encoding='utf-8', errors='ignore') as cfile:
        text = cfile.read()
    data_vs = set(re.findall(r'\[data-v-[a-z0-9]+\]', text))
    print(f"{f}: {len(data_vs)} data-v attributes -> {data_vs}")
