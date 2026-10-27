import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<svg[^>]*class="[^"]*spring-calligraphy[^"]*".*?</svg>', html, re.DOTALL)
if m:
    print(m.group(0)[:800])
    print('...')
    print(m.group(0)[-800:])
