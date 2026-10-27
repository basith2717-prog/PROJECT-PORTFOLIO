import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('HEADER:', soup.find('header').get('class') if soup.find('header') else None)
print('MAIN:', soup.find('main').get('class') if soup.find('main') else None)

for sec in soup.find_all('section'):
    cls = ' '.join(sec.get('class', []))
    id_ = sec.get('id', '')
    print(f'SECTION: id="{id_}" class="{cls}"')

footer = soup.find('footer')
print('FOOTER:', footer.get('class') if footer else None)
