import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

def trace(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    print(f"=== {filename} ===")
    for tag_name in ['header', 'section', 'footer']:
        for tag in soup.find_all(tag_name):
            p = tag
            chain = []
            while p and p.name != '[document]':
                cls = '.'.join(p.get('class', []))
                id_ = f"#{p.get('id')}" if p.get('id') else ""
                chain.append(f"{p.name}{id_}{'.'+cls if cls else ''}")
                p = p.parent
            print(" -> ".join(reversed(chain)))

trace('_reference_kigo/kigo_live.html')
print()
trace('index.html')
