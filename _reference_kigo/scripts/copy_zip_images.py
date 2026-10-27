"""
Map extracted zip images to their correct kigo.studio public paths.
Based on decoded Netlify URLs from kigo_raw.html.
"""
import os
import shutil
from PIL import Image

EXTRACTED = r"c:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\extracted_kigo"
PUBLIC = r"c:\Users\Basith\OneDrive\Documents\PROJECT-PORTFOLIO\public\images"

def dims(path):
    try:
        with Image.open(path) as img:
            return img.width, img.height
    except:
        return (0, 0)

def find_by_dims(w, h):
    candidates = []
    for fname in os.listdir(EXTRACTED):
        fpath = os.path.join(EXTRACTED, fname)
        ext = os.path.splitext(fname)[1].lower()
        if ext not in [".webp", ".png", ".jpg", ".jpeg", ".gif"]:
            continue
        fw, fh = dims(fpath)
        if fw == w and fh == h:
            candidates.append(fname)
    return candidates

def find_by_size_range(min_bytes, max_bytes):
    candidates = []
    for fname in os.listdir(EXTRACTED):
        fpath = os.path.join(EXTRACTED, fname)
        size = os.path.getsize(fpath)
        if min_bytes <= size <= max_bytes:
            candidates.append((fname, size))
    return candidates

def copy_to(src_name, dest_rel_path):
    src = os.path.join(EXTRACTED, src_name)
    dest = os.path.join(PUBLIC, dest_rel_path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy2(src, dest)
    print(f"  COPIED: {src_name} -> {dest_rel_path}")

print("=== MAPPING KIGO.STUDIO IMAGES FROM ZIP ===\n")

# 1. Misty landscape (1774x887) -> /images/sakura/misty-landscape-v2.webp
landscape_candidates = find_by_dims(1774, 887)
print(f"Landscape (1774x887): {landscape_candidates}")
if landscape_candidates:
    copy_to(landscape_candidates[0], "sakura/misty-landscape-v2.webp")

# 2. Showreel GIF (407x304) -> /images/showreel-preview.gif
gif_candidates = find_by_dims(407, 304)
print(f"Showreel GIF (407x304): {gif_candidates}")
if gif_candidates:
    copy_to(gif_candidates[0], "showreel-preview.gif")

# 3. Dancer poses (1024x1536) - already handled
print("\nDancer poses (1024x1536):")
for f in ["clients-dance-pose-1-v6.webp", "clients-dance-pose-2-v6.webp"]:
    src = os.path.join(EXTRACTED, f)
    if os.path.exists(src):
        copy_to(f, f"clients/{f}")
        copy_to(f, f"illustrations/{f}")

# 4. Service Posters (640x960) - these are the tall vertical posters
print("\nService posters (640x960):")
poster_640_960 = find_by_dims(640, 960)
print(f"  Found: {poster_640_960}")
# From the reference: websites, ecommerce, apps, automations
# We have 4 files at 640x960: images_20, images_42, images_64, images_67
poster_map = {
    "images_20.webp": "services/poster-ecommerce.webp",
    "images_42.webp": "services/poster-apps.webp",
    "images_64.webp": "services/poster-websites.webp",
    "images_67.webp": "services/poster-automations.webp",
}
for src_name, dest_path in poster_map.items():
    if os.path.exists(os.path.join(EXTRACTED, src_name)):
        copy_to(src_name, dest_path)

# Also copy as subject/bg variants for service menu
poster_subject_map = {
    "images_20.webp": "services/posters/ecommerce-subject-v5-640.webp",
    "images_42.webp": "services/posters/apps-subject-v4-640.webp",
    "images_64.webp": "services/posters/websites-subject-v3-640.webp",
    "images_67.webp": "services/posters/automations-subject-v2-640.webp",
}
for src_name, dest_path in poster_subject_map.items():
    if os.path.exists(os.path.join(EXTRACTED, src_name)):
        copy_to(src_name, dest_path)

# Service BG versions (640x640 square - floral/abstract backgrounds)
print("\nService BG (640x640):")
bg_640_640 = find_by_dims(640, 640)
print(f"  Found: {bg_640_640}")
# Map 640x640 to background variants
bg_map = {
    "images_22.webp": "services/posters/ecommerce-background-v2-768.webp",
    "images_39.webp": "services/posters/apps-background-v2-768.webp",
    "images_56.webp": "services/posters/websites-background-v2-768.webp",
    "images_59.webp": "services/posters/automations-background-v2-768.webp",
}
for src_name, dest_path in bg_map.items():
    if os.path.exists(os.path.join(EXTRACTED, src_name)):
        copy_to(src_name, dest_path)

# 5. Project postcard images (480x720 and 320x480)
print("\nProject postcards:")
proj_480_720 = find_by_dims(480, 720)
proj_320_480 = find_by_dims(320, 480)
print(f"  480x720: {proj_480_720}")
print(f"  320x480: {proj_320_480}")

# Projects: llul, usandplus, recken, celtrev, minu, brio, etc.
# 480x720 (4 files)
if len(proj_480_720) >= 4:
    copy_to(proj_480_720[0], "projects/project-llul.webp")
    copy_to(proj_480_720[1], "projects/project-usplus.webp")
    copy_to(proj_480_720[2], "projects/project-recken.webp")
    copy_to(proj_480_720[3], "projects/project-minu.webp")

# 320x480 (4 files)
if len(proj_320_480) >= 4:
    copy_to(proj_320_480[0], "projects/project-celtrev.webp")
    copy_to(proj_320_480[1], "projects/project-brio.webp")
    copy_to(proj_320_480[2], "projects/project-pago.webp")
    copy_to(proj_320_480[3], "projects/project-artist.webp")

# 6. Client logos (various sizes)
print("\nClient logos:")
# 287x104 -> gobierno-de-mexico
govt_candidates = find_by_dims(287, 104)
print(f"  gobierno-de-mexico (287x104): {govt_candidates}")
if govt_candidates:
    copy_to(govt_candidates[0], "clients/gobierno-de-mexico.webp")

# 290x94 -> fifa  
fifa_candidates = find_by_dims(290, 94)
print(f"  fifa (290x94): {fifa_candidates}")
if fifa_candidates:
    copy_to(fifa_candidates[0], "clients/fifa.webp")

# 290x143 -> tequila-campo-azul
tca_candidates = find_by_dims(290, 143)
print(f"  tequila-campo-azul (290x143): {tca_candidates}")
if tca_candidates:
    copy_to(tca_candidates[0], "clients/tequila-campo-azul.webp")

# 290x85 -> wera-workout
wera_candidates = find_by_dims(290, 85)
print(f"  wera-workout (290x85): {wera_candidates}")
if wera_candidates:
    copy_to(wera_candidates[0], "clients/wera-workout.webp")

# 145x42 -> tu-potencial (small)
tu_candidates = find_by_dims(145, 42)
print(f"  tu-potencial (145x42): {tu_candidates}")
if tu_candidates:
    copy_to(tu_candidates[0], "clients/tu-potencial.webp")

# 7. Floral illustration background (768x512 is very likely)
print("\nFloral background (768x512):")
floral_candidates = find_by_dims(768, 512)
print(f"  Found: {floral_candidates}")
if floral_candidates:
    copy_to(floral_candidates[0], "illustrations/clients-floral-background-v1.webp")

# 8. Omamori (720x1080 tall)
print("\nOmamori (720x1080):")
omamori_candidates = find_by_dims(720, 1080)
print(f"  Found: {omamori_candidates}")
if omamori_candidates:
    copy_to(omamori_candidates[0], "home/faqs/omamori-sakura-v1.webp")

# 9. OG image (1200x630)
print("\nOG image (1200x630):")
og_candidates = find_by_dims(1200, 630)
print(f"  Found: {og_candidates}")
if og_candidates:
    copy_to(og_candidates[0], "og-en.jpeg")

# 10. Copy SVG files (globe icon, language icon, etc.)
print("\nSVG files:")
svgs = [f for f in os.listdir(EXTRACTED) if f.endswith(".svg")]
for i, svg in enumerate(svgs):
    size = os.path.getsize(os.path.join(EXTRACTED, svg))
    print(f"  [{i}] {svg}: {size} bytes")

# Globe / language icon is typically small SVG
small_svgs = sorted([(f, os.path.getsize(os.path.join(EXTRACTED, f))) for f in svgs], key=lambda x: x[1])
print(f"\nSmall SVGs (by size): {small_svgs}")

# Hollywood wordmark SVG
hollywood_src = os.path.join(EXTRACTED, "hollywood-wordmark.svg")
if os.path.exists(hollywood_src):
    copy_to("hollywood-wordmark.svg", "clients/hollywood-wordmark.svg")

print("\n=== DONE ===")
