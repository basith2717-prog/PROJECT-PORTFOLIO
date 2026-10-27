import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def print_tree(el, depth=0):
    if not el.name:
        return
    cls = ".".join(el.get('class', []))
    id_str = f"#{el.get('id')}" if el.get('id') else ""
    cls_str = f".{cls}" if cls else ""
    print("  " * depth + f"<{el.name}{id_str}{cls_str}>")
    for child in el.find_all(recursive=False):
        print_tree(child, depth + 1)

print_tree(soup.find('body'))
