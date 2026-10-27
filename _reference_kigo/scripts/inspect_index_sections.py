from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.find('body')
for child in body.children:
    if child.name:
        classes = ".".join(child.get('class', []))
        id_str = f"#{child.get('id')}" if child.get('id') else ""
        print(f"<{child.name} {id_str} {classes}>")

main = soup.find('main')
if main:
    print("\nInside <main>:")
    for child in main.children:
        if child.name:
            classes = ".".join(child.get('class', []))
            id_str = f"#{child.get('id')}" if child.get('id') else ""
            print(f"  <{child.name} {id_str} {classes}>")
