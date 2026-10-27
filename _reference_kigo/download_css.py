import urllib.request
import re

with open('kigo_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

css_links = re.findall(r'href="(/_nuxt/[^"]+\.css)"', html)
print("CSS links:", css_links)

for link in set(css_links):
    url = "https://kigo.studio" + link
    fname = link.split('/')[-1]
    print(f"Downloading {url} to {fname}...")
    try:
        urllib.request.urlretrieve(url, fname)
        print(f"Downloaded {fname}")
    except Exception as e:
        print(f"Error {url}: {e}")
