import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    css_text = f.read()

# Extract all classes used in index.html
html_classes = set()
for tag in soup.find_all(True):
    for c in tag.get('class', []):
        html_classes.add(c)

# Extract all class selectors in style.css
css_classes = set(re.findall(r'\.([a-zA-Z0-9_\-]+)', css_text))

missing_in_css = html_classes - css_classes
present_in_css = html_classes & css_classes

print(f"Total distinct classes in index.html: {len(html_classes)}")
print(f"Total distinct class selectors in style.css: {len(css_classes)}")
print(f"Classes in HTML found in CSS: {len(present_in_css)}")
print(f"Classes in HTML MISSING from CSS: {len(missing_in_css)}")
print("\nSample missing classes from style.css:")
for c in sorted(missing_in_css)[:40]:
    print(" -", c)
