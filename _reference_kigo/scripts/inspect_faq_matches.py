import re

with open('_reference_kigo/IllustratedFaq.CKUH9x3P.css', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for prefix in ['.faq', '.service-faq', '.service-faq-ornament', '.service-faq-ribbon']:
    matches = re.findall(rf'{re.escape(prefix)}[^{{]*\{{[^}}]*\}}', text)
    print(f"Matches for {prefix}: {len(matches)}")
