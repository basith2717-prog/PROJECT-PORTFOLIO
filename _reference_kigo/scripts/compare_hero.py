from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    local_soup = BeautifulSoup(f.read(), 'html.parser')

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    kigo_soup = BeautifulSoup(f.read(), 'html.parser')

print("--- LOCAL HERO ---")
local_hero = local_soup.find(class_='hero')
if local_hero:
    print(local_hero.prettify()[:600])

print("--- KIGO HERO ---")
kigo_hero = kigo_soup.find(class_='hero')
if kigo_hero:
    print(kigo_hero.prettify()[:600])
