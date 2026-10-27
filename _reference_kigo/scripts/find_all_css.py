import urllib.request
import re
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

links = soup.find_all('link', rel='stylesheet')
for l in links:
    print("Stylesheet in live HTML:", l.get('href'))

# Also search for any .css in scripts or html
all_css = set(re.findall(r'/[^"\'\s]+\.css', soup.prettify()))
print("\nAll CSS mentions in HTML:")
for c in all_css:
    print(" ", c)
