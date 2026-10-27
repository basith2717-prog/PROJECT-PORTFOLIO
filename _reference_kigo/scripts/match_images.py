import os
import hashlib

def get_hash(p):
    with open(p, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

img_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"
public_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\public"

hashes = {}
for root, dirs, files in os.walk(public_dir):
    for f in files:
        full = os.path.join(root, f)
        hashes[get_hash(full)] = os.path.relpath(full, public_dir)

print("Matching files from IMG with public directory:")
for f in os.listdir(img_dir):
    p = os.path.join(img_dir, f)
    h = get_hash(p)
    if h in hashes:
        print(f"{f}  ===>  public/{hashes[h]}")
    else:
        print(f"{f}  (new, not in public yet, size={os.path.getsize(p)})")
