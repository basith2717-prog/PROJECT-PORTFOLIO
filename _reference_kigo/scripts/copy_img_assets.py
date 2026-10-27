import os
import shutil

src_dir = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\IMG"
dest_base = r"C:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\public\images"

os.makedirs(dest_base, exist_ok=True)
os.makedirs(os.path.join(dest_base, "IMG"), exist_ok=True)
os.makedirs(os.path.join(dest_base, "services"), exist_ok=True)
os.makedirs(os.path.join(dest_base, "projects"), exist_ok=True)
os.makedirs(os.path.join(dest_base, "clients"), exist_ok=True)

# 1. Copy everything to public/images/IMG/ exactly as is
for f in os.listdir(src_dir):
    s = os.path.join(src_dir, f)
    d = os.path.join(dest_base, "IMG", f)
    shutil.copy2(s, d)

# 2. Semantic mappings
mappings = {
    "images.webp": "landscape.webp",
    "images (1).webp": "sakura/misty-landscape-v2.webp",
    "images (2).webp": "sakura/ink-watercolor-entry-v2.webp",
    "images (3).webp": "clients/featured-character.webp",
    "images (4).webp": "services/poster-ecommerce.webp",
    "images (5).webp": "services/poster-apps.webp",
    "images (6).webp": "services/poster-websites.webp",
    "images (7).webp": "services/poster-automations.webp",
    "images (8).webp": "projects/project-pago.webp",
    "images (9).webp": "projects/project-usplus.webp",
    "images (10).webp": "projects/project-minu.webp",
    "images (11).webp": "projects/project-llul.webp",
    "clients-dance-pose-1-v6.webp": "clients/clients-dance-pose-1-v6.webp",
    "clients-dance-pose-2-v6.webp": "clients/clients-dance-pose-2-v6.webp",
    "og-en.jpeg": "og-en.jpeg",
    "images.gif": "showreel-preview.gif",
    "e804fa0b-b38a-4146-9ec8-baf939f6ed4f.svg": "sakura-hero-art.svg",
    "ed4fa376-9a9b-40dc-9f59-9927f892f98a.svg": "globe-kigo.svg"
}

for src_name, rel_dest in mappings.items():
    src_path = os.path.join(src_dir, src_name)
    if os.path.exists(src_path):
        target = os.path.join(dest_base, rel_dest)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(src_path, target)
        print(f"Copied {src_name} -> {rel_dest}")

print("Done copying all images from IMG folder!")
