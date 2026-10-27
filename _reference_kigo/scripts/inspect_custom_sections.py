import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

for sec_name in ['home-work', 'home-team', 'home-contact', 'site-footer']:
    tag = soup.find(class_=re.compile(sec_name)) if 're' in locals() else soup.find(lambda el: el.has_attr('class') and any(sec_name in c for c in el['class']))
    print(f"\n==================== {sec_name} ====================")
    if tag:
        classes_in_sec = set()
        for t in tag.find_all(True):
            for c in t.get('class', []):
                classes_in_sec.add(c)
        print("Classes used in section:")
        print(", ".join(sorted(classes_in_sec)))
        lines = tag.prettify().split('\n')
        print("First 35 lines:")
        print('\n'.join(lines[:35]))
