import os
import re

ref_css_files = [f for f in os.listdir('_reference_kigo') if f.endswith('.css')]

for f in ref_css_files:
    path = os.path.join('_reference_kigo', f)
    with open(path, 'r', encoding='utf-8', errors='ignore') as cfile:
        text = cfile.read()
    print(f"{f}: has .header={'header' in text}, has .hero={'hero' in text}, has .faq={'faq' in text}, has .home-clients={'home-clients' in text}")
