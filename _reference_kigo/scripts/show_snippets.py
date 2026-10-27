import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

def show_around(idx, length=400):
    start = max(0, idx - 50)
    end = min(len(css), idx + length)
    print("--- SNIPPET AT", idx, "---")
    print(css[start:end])
    print()

show_around(20162, 500) # .header{
show_around(8047, 300) # .p-wrap
show_around(63504, 500) # .hero{
show_around(64789, 400) # .home{
show_around(67211, 300) # .home__group
show_around(67283, 300) # .home__content
