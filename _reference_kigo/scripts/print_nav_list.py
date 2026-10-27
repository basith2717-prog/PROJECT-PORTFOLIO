import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

nav_list = soup.find(class_='header__navigation')
for li in nav_list.find_all('li', recursive=False):
    print("LI:", li.get('class'), "->", li.get_text(strip=True)[:40])
