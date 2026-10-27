import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.find('header')
nav = header.find('nav')
print("Nav direct children:")
for c in nav.children:
    if c.name:
        print(f"<{c.name} class='{c.get('class', [])}' id='{c.get('id', '')}'>")
