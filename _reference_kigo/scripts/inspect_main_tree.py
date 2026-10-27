import re
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

main = soup.find('main')
print("Main tag:", main.name, main.get('class'))

def describe(tag, depth=0):
    if depth > 4:
        return
    indent = "  " * depth
    classes = ".".join(tag.get('class', []))
    id_str = f"#{tag.get('id')}" if tag.get('id') else ""
    child_tags = [c for c in tag.children if c.name]
    summary = f"<{tag.name} {id_str} {classes}> ({len(child_tags)} children)"
    print(indent + summary)
    for c in child_tags:
        describe(c, depth + 1)

describe(main)
