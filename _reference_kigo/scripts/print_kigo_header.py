from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.find('header')
print(header.prettify())
