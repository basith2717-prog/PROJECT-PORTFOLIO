with open('style.css', 'r', encoding='utf-8', errors='ignore') as f:
    local_css = f.read()

print("Does style.css have [data-v-]:", '[data-v-' in local_css)

# Check why user says: "entire css is mismatched and wrongly placed take a look into this website this is how i need it https://kigo.studio/"
# Let's inspect index.html vs what styles are actually applied.
