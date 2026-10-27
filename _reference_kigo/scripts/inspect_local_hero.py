import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== LOCAL HEADER ===")
header = soup.find('header')
if header:
    print(header.prettify()[:1000])

print("\n=== LOCAL HERO ===")
hero = soup.find(id='hero')
if hero:
    print(hero.prettify()[:1500])
