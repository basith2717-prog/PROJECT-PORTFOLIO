import re

with open('_reference_kigo/kigo_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Search for spring calligraphy
matches = re.findall(r'(<svg[^>]*spring-calligraphy[^>]*>.*?</svg>)', c, re.DOTALL)
print(f"spring-calligraphy SVGs found: {len(matches)}")
if matches:
    with open('public/images/spring-calligraphy.svg', 'w', encoding='utf-8') as out:
        out.write(matches[0])
    print("Wrote public/images/spring-calligraphy.svg, length:", len(matches[0]))
else:
    # search for any SVG with 春 or path
    print("Searching for SVG with kanji...")
    all_svgs = re.findall(r'(<svg[^>]*>.*?</svg>)', c, re.DOTALL)
    print(f"Total SVGs: {len(all_svgs)}")
    for i, s in enumerate(all_svgs):
        if 'calligraphy' in s or 'spring' in s or 'viewBox="0 0 1' in s:
            print(f"SVG {i}: {s[:100]}")
            with open(f'public/images/extracted_svg_{i}.svg', 'w', encoding='utf-8') as out:
                out.write(s)
