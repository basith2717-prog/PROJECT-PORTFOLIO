import re
import json

with open(r"_reference_kigo\kigo_raw.html", "r", encoding="utf-8", errors="ignore") as f:
    html = f.read()

# Find window.__NUXT__ or <script type="application/json" ...
nuxt_scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', html)
print(f"Total script blocks: {len(nuxt_scripts)}")

for i, s in enumerate(nuxt_scripts):
    if "projectResults" in s or "llul" in s or "pago" in s:
        print(f"Found project data in script #{i+1}, length={len(s)}")
        # write out to file for inspection
        with open(r"_reference_kigo\nuxt_payload_data.txt", "w", encoding="utf-8") as out:
            out.write(s)
        break
