from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

nuxt = soup.find('div', id='__nuxt')
if nuxt:
    print("Direct children of #__nuxt:")
    for c in nuxt.children:
        if c.name:
            classes = ".".join(c.get('class', []))
            print(f"  <{c.name} id='{c.get('id', '')}' class='{classes}'>")

print("\nDirect children of home__group:")
hg = soup.find(class_='home__group')
if hg:
    for c in hg.children:
        if c.name:
            classes = ".".join(c.get('class', []))
            print(f"  <{c.name} id='{c.get('id', '')}' class='{classes}'>")

print("\nDirect children of home__content:")
hc = soup.find(class_='home__content')
if hc:
    for c in hc.children:
        if c.name:
            classes = ".".join(c.get('class', []))
            print(f"  <{c.name} id='{c.get('id', '')}' class='{classes}'>")
