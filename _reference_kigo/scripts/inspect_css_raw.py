with open('_reference_kigo/index.CY5he_ku.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("Length of index.CY5he_ku.css:", len(css))
# Print the first 1000 chars of index.CY5he_ku.css
print("First 1000 chars:\n", css[:1000])

with open('_reference_kigo/entry.Bmo6-XxB.css', 'r', encoding='utf-8') as f:
    entry_css = f.read()
print("\nLength of entry.Bmo6-XxB.css:", len(entry_css))
print("First 1000 chars of entry:\n", entry_css[:1000])
