import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def summarize_tag(tag, depth=0):
    if not tag or not tag.name or depth > 3:
        return
    classes = ".".join(tag.get('class', []))
    id_val = f"#{tag.get('id')}" if tag.get('id') else ""
    cls_val = f".{classes}" if classes else ""
    text_preview = tag.get_text(strip=True)[:35]
    print(f"{'  '*depth}<{tag.name}{id_val}{cls_val}>: {text_preview}")
    for c in tag.find_all(recursive=False):
        summarize_tag(c, depth + 1)

print("=== HERO ===")
summarize_tag(soup.find(id='hero'))

print("\n=== CLIENTS ===")
summarize_tag(soup.find(id='clients'))

print("\n=== WORK ===")
summarize_tag(soup.find(class_='home-work'))

print("\n=== EXPERIENCE ===")
summarize_tag(soup.find(id='experience'))
