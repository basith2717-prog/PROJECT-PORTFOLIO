import os
import re

ref_order = [
    'entry.Bmo6-XxB.css',
    'index.CY5he_ku.css',
    'IllustratedFaq.CKUH9x3P.css',
    'WorkSection.DUSwICN7.css',
    'WorkPostcard.C34s6Bd8.css',
    'HomeTeam.gle-pIYe.css',
    'ProjectCardMarks.VZ1WhnK8.css',
    'MoreCalligraphy.DceKB5ZG.css',
    'useWorkProjects.Dt8yYixg.css'
]

combined_ref = ""
for rf in ref_order:
    p = os.path.join('_reference_kigo', rf)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            combined_ref += f"\n/* --- SOURCE: {rf} --- */\n" + f.read()

# Strip [data-v-xxxxxx]
clean_kigo_css = re.sub(r'\[data-v-[a-z0-9]+\]', '', combined_ref)

# Also let's check for any image URLs in ref css to make sure paths are correct
# In ref css, URLs might be /.netlify/images?url=... or /images/...
def fix_urls(match):
    url = match.group(1)
    if 'url=%2F' in url:
        # decode netlify url
        import urllib.parse
        parsed = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        if 'url' in parsed:
            target = parsed['url'][0].lstrip('/')
            return f"url('./public/{target}')"
    elif url.startswith('/images/'):
        return f"url('./public{url}')"
    elif url.startswith('/fonts/'):
        return f"url('./public{url}')"
    return match.group(0)

clean_kigo_css = re.sub(r'url\(([^)]+)\)', fix_urls, clean_kigo_css)

print(f"Processed clean Kigo CSS: {len(clean_kigo_css)} chars")

with open('_reference_kigo/scripts/kigo_clean_core.css', 'w', encoding='utf-8') as f:
    f.write(clean_kigo_css)
