import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def print_sections(soup):
    for sec in soup.find_all(['section', 'header', 'footer']):
        cls = sec.get('class', [])
        id_ = sec.get('id', '')
        print(f"<{sec.name} id='{id_}' class='{' '.join(cls)}'>")

print_sections(soup)
