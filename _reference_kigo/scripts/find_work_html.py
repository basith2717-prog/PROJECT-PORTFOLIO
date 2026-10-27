import sys
sys.stdout.reconfigure(encoding='utf-8')
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('home-work')
if idx != -1:
    print(html[idx:idx+2500])
