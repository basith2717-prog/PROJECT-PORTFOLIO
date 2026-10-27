import re

with open('main.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

# find document.querySelector / getElementById / classList
selectors = set(re.findall(r'querySelector(?:All)?\([\'"]([^\'"]+)[\'"]\)', js))
by_ids = set(re.findall(r'getElementById\([\'"]([^\'"]+)[\'"]\)', js))
classes_toggled = set(re.findall(r'classList\.(?:add|remove|toggle|contains)\([\'"]([^\'"]+)[\'"]\)', js))

print("DOM IDs used in main.js:")
for i in sorted(by_ids):
    print("  #", i)

print("\nCSS Selectors in main.js:")
for s in sorted(selectors)[:25]:
    print("  ", s)

print("\nClasses toggled in main.js:")
for c in sorted(classes_toggled):
    print("  .", c)
