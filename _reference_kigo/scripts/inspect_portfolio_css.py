import re

with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

sections_to_check = ['/* ==========================================================================\n   PORTFOLIO WORK', '/* ==========================================================================\n   EXPERIENCE & ABOUT', '/* ==========================================================================\n   POSTCARD CONTACT', '/* ==========================================================================\n   FOOTER']

for st in sections_to_check:
    pos = css.find(st)
    if pos != -1:
        print("Found section header:", st.split('\n')[1])
        print(css[pos:pos+400])
        print("...\n")
    else:
        print("NOT FOUND:", st.split('\n')[1] if '\n' in st else st)
