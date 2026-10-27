import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== HEADER IN KIGO_LIVE.HTML ===")
header = soup.find('header')
if header:
    print(header.prettify()[:2000])

print("\n=== HERO IN KIGO_LIVE.HTML ===")
hero = soup.find(class_='hero')
if hero:
    print(hero.prettify()[:2500])
