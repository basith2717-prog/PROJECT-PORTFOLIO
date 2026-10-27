import sys
sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup

with open('_reference_kigo/kigo_live.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

scrollable = soup.find(class_='scrollable')
if scrollable:
    print("Children of scrollable:")
    for child in scrollable.find_all(recursive=False):
        print(f"<{child.name} class='{child.get('class')}'>")
        for sub in child.find_all(recursive=False):
            print(f"  <{sub.name} class='{sub.get('class')}'>")
            for subsub in sub.find_all(recursive=False):
                print(f"    <{subsub.name} class='{subsub.get('class')}'>")
