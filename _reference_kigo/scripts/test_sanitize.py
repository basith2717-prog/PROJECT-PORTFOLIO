import re

with open('_reference_kigo/scripts/kigo_clean_core.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("Original length:", len(css))

# 1. Sanitize main
css = re.sub(r'main\s*\{[^}]*inset:0[^}]*overflow:hidden[^}]*position:fixed[^}]*\}', 
             'main{position:relative;overflow:visible;}', css)

# 2. Sanitize #__nuxt
css = re.sub(r'#__nuxt\s*\{[^}]*position:absolute[^}]*\}', 
             '#__nuxt{position:relative;width:100%;margin:0 auto;max-width:var(--max-width);padding:0 var(--padding-horizontal-page);}', css)

# 3. Sanitize body overflow
css = re.sub(r'(body\s*\{[^}]*);overflow:hidden;([^}]*\})', r'\1;overflow-x:hidden;\2', css)
css = re.sub(r'(html\s*\{[^}]*);overflow:hidden;([^}]*\})', r'\1;overflow-x:hidden;\2', css)

# 4. Sanitize .scrollable
css = re.sub(r'\.scrollable\s*\{[^}]*position:fixed[^}]*\}', 
             '.scrollable{position:relative;width:100%;}', css)

# 5. Sanitize header--wide
css = re.sub(r'\.header--wide\s*\{[^}]*margin-left:calc\(50% - 50vw\)[^}]*\}',
             '.header--wide{width:100%;margin-left:0;padding-inline:var(--edge-padding);}', css)

# 6. Sanitize nav-item__mask opacity
css = re.sub(r'\.nav-item__mask\s*\{[^}]*opacity:0[^}]*\}',
             '.nav-item__mask{opacity:1;display:flex;flex-direction:column;position:relative;row-gap:.2rem;z-index:10;}', css)

# 7. Sanitize spring-calligraphy
css = re.sub(r'\.spring-calligraphy__trace\s*\{[^}]*opacity:0[^}]*\}',
             '.spring-calligraphy__trace{opacity:1;stroke-dasharray:none;stroke-dashoffset:0;stroke:white;}', css)

print("Sanitized length:", len(css))

# Test that main has relative
for m in re.finditer(r'main\s*\{[^}]+\}', css):
    print("MAIN:", m.group(0)[:80])

# Test that #__nuxt has relative
for m in re.finditer(r'#__nuxt\s*\{[^}]+\}', css):
    print("NUXT:", m.group(0)[:80])
