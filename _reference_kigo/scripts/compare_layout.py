import re
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    kigo_soup = BeautifulSoup(f.read(), 'html.parser')

with open('index.html', 'r', encoding='utf-8') as f:
    local_soup = BeautifulSoup(f.read(), 'html.parser')

print("=== KIGO SECTIONS / HIGH LEVEL LAYOUT ===")
main = kigo_soup.find('main') or kigo_soup.find('div', id='__nuxt')
for el in kigo_soup.find_all(['header', 'section', 'footer', 'nav', 'main']):
    classes = ' '.join(el.get('class', []))
    id_attr = el.get('id', '')
    print(f"<{el.name} class='{classes}' id='{id_attr}'>")

print("\n=== LOCAL SECTIONS / HIGH LEVEL LAYOUT ===")
for el in local_soup.find_all(['header', 'section', 'footer', 'nav', 'main']):
    classes = ' '.join(el.get('class', []))
    id_attr = el.get('id', '')
    print(f"<{el.name} class='{classes}' id='{id_attr}'>")
