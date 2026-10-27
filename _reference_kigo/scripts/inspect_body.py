from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.find('body')
for c in body.children:
    if c.name:
        classes = ".".join(c.get('class', []))
        id_str = f"#{c.get('id')}" if c.get('id') else ""
        print(f"BODY CHILD: <{c.name} {id_str} {classes}>")

nuxt = soup.find('div', id='__nuxt')
if nuxt:
    for c in nuxt.children:
        if c.name:
            classes = ".".join(c.get('class', []))
            id_str = f"#{c.get('id')}" if c.get('id') else ""
            print(f"  NUXT CHILD: <{c.name} {id_str} {classes}>")
            if c.name != 'main':
                for gc in c.children:
                    if gc.name:
                        gclasses = ".".join(gc.get('class', []))
                        print(f"    <{gc.name} {gclasses}>")
