import re
from bs4 import BeautifulSoup

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

out = []
out.append("=== TITLE & META ===")
for m in re.finditer(r'<title>(.*?)</title>', html, re.I):
    out.append(m.group(1))

# Check stylesheets and fonts
out.append("\n=== FONTS & ASSETS ===")
for m in re.finditer(r'href="([^"]+(?:fonts|css|woff2|svg|png|webp|jpg)[^"]*)"', html, re.I):
    out.append(m.group(1))

# Let's extract the main tags structure
soup = BeautifulSoup(html, 'html.parser')

main = soup.find('main')
if main:
    out.append(f"\n=== MAIN CHILDREN ({len(main.find_all(recursive=False))}) ===")
    for child in main.find_all(recursive=False):
        out.append(f"<{child.name} class='{child.get('class', [])}' id='{child.get('id', '')}'>")

out.append("\n=== ALL SECTIONS ===")
for sec in soup.find_all(['section', 'header', 'footer']):
    cls = sec.get('class', [])
    sec_id = sec.get('id', '')
    h = sec.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(strip=True) if h else "No heading"
    out.append(f"<{sec.name} class='{' '.join(cls)}' id='{sec_id}'> -> {h_text}")

# Let's inspect hero specifically
hero = soup.find(class_=re.compile(r'hero'))
if hero:
    out.append("\n=== HERO INNER TEXT ===")
    out.append(hero.get_text(separator=' | ', strip=True))

# Let's inspect clients
clients = soup.find(class_=re.compile(r'client'))
if clients:
    out.append("\n=== CLIENTS INNER TEXT ===")
    out.append(clients.get_text(separator=' | ', strip=True)[:1000])

# Let's inspect services
services = soup.find_all(class_=re.compile(r'service'))
out.append(f"\n=== SERVICES COUNT: {len(services)} ===")
for s in services[:5]:
    out.append(s.get_text(separator=' | ', strip=True)[:300])

# Let's inspect faq
faqs = soup.find_all(class_=re.compile(r'faq'))
out.append(f"\n=== FAQ COUNT: {len(faqs)} ===")
for q in faqs[:5]:
    out.append(q.get_text(separator=' | ', strip=True)[:500])

# Let's inspect footer
footer = soup.find('footer')
if footer:
    out.append("\n=== FOOTER ===")
    out.append(footer.get_text(separator=' | ', strip=True))

with open('site_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Analysis written to site_analysis.txt")
