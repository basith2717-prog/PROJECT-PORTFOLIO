import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html_local = f.read()

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    html_ref = f.read()

soup_local = BeautifulSoup(html_local, 'html.parser')
soup_ref = BeautifulSoup(html_ref, 'html.parser')

print("--- LOCAL STRUCTURE ---")
for tag in soup_local.find_all(['header', 'main', 'section', 'footer']):
    cls = tag.get('class', [])
    id_ = tag.get('id', '')
    parent = tag.parent.name if tag.parent else 'none'
    parent_cls = tag.parent.get('class', []) if tag.parent else []
    print(f"<{tag.name} id='{id_}' class='{' '.join(cls)}'> parent: <{parent} class='{' '.join(parent_cls)}'>")

print("\n--- REFERENCE KIGO STRUCTURE ---")
for tag in soup_ref.find_all(['header', 'main', 'section', 'footer']):
    cls = tag.get('class', [])
    id_ = tag.get('id', '')
    parent = tag.parent.name if tag.parent else 'none'
    parent_cls = tag.parent.get('class', []) if tag.parent else []
    print(f"<{tag.name} id='{id_}' class='{' '.join(cls)}'> parent: <{parent} class='{' '.join(parent_cls)}'>")
