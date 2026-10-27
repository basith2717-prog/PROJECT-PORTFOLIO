import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    html_ref = f.read()

soup = BeautifulSoup(html_ref, 'html.parser')

main = soup.find('main')
if main:
    print(f"Main tag: {main.name}, classes: {main.get('class')}")
    for child in main.children:
        if child.name:
            print(f"  Child: <{child.name} class='{child.get('class')}'>")
            for sub in child.children:
                if sub.name:
                    print(f"    Sub: <{sub.name} class='{sub.get('class')}'>")
