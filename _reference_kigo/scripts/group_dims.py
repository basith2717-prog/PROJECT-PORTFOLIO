import json
import re

with open(r"_reference_kigo\zip_images_summary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Group by dimensions
dim_groups = {}
for item in data:
    dims = item.get("dims") or item.get("ext")
    dim_groups.setdefault(dims, []).append(item)

print(f"Total files: {len(data)}")
for d, items in sorted(dim_groups.items(), key=lambda x: -len(x[1])):
    print(f"\nDimension/Type: {d} ({len(items)} files)")
    for it in items[:6]:
        print(f"  {it['file']} ({it['size']} bytes)")
    if len(items) > 6:
        print(f"  ... and {len(items)-6} more")
