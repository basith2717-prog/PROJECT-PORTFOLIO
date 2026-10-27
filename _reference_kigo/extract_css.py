import re

with open('kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
all_css = '\n'.join(styles)

with open('extracted_styles.css', 'w', encoding='utf-8') as out:
    out.write(all_css)

keyframes = set(re.findall(r'@keyframes\s+([a-zA-Z0-9_-]+)', all_css))
print(f"Keyframes ({len(keyframes)}):", sorted(list(keyframes)))

# Check custom properties (:root)
root_vars = re.findall(r'(--[a-zA-Z0-9_-]+):\s*([^;]+);', all_css)
print(f"Total CSS variables: {len(root_vars)}")
with open('css_variables.txt', 'w', encoding='utf-8') as out:
    for k, v in sorted(list(set(root_vars))):
        out.write(f"{k}: {v.strip()};\n")

print("Done extracting CSS")
