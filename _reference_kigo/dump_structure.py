from bs4 import BeautifulSoup
import json

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

scrollable = soup.find(class_='scrollable')
if not scrollable:
    print("No scrollable found, looking in body")
    container = soup.body
else:
    container = scrollable

elements_info = []

def walk(el, depth=0):
    if el.name in ['script', 'style', 'svg', 'noscript']:
        return
    classes = " ".join(el.get('class', []))
    tag_id = el.get('id', '')
    text = ""
    # if direct text is present
    direct_strings = [s.strip() for s in el.find_all(string=True, recursive=False) if s.strip()]
    if direct_strings:
        text = " ".join(direct_strings)[:80]
    
    if classes or tag_id or el.name in ['header', 'nav', 'section', 'footer', 'h1', 'h2', 'h3', 'button', 'a']:
        indent = "  " * depth
        elements_info.append(f"{indent}<{el.name} class='{classes}' id='{tag_id}'> {text}")
    
    for ch in el.find_all(recursive=False):
        walk(ch, depth + 1)

walk(container)

with open('structure_dump.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(elements_info[:300]))

print("Structure written, total lines:", len(elements_info))
