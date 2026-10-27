import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<li class="work-card">.*?</li>', html, re.DOTALL)
if m:
    print(m.group(0))
