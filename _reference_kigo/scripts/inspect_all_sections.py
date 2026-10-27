import sys
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def show(name, tag):
    print(f"\n--- {name} ---")
    if tag:
        lines = tag.prettify().split('\n')
        print('\n'.join(lines[:25]))
    else:
        print("NOT FOUND")

show("HEADER", soup.find('header'))
show("HERO", soup.find(id='hero'))
show("CLIENTS", soup.find(id='clients'))
show("WORK", soup.find(class_='home-work'))
show("TEAM", soup.find(class_='home-team'))
show("FAQ", soup.find(id='faq'))
show("CONTACT", soup.find(id='contact'))
show("FOOTER", soup.find('footer'))
