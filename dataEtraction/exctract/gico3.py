import json
import requests
import csv

# ————— Parámetros —————
ACCESS_TOKEN = "APP_USR-6186476861975930-070211-ba5e2d3e6b0783d7172a3d9b47510b0d-1653870402"
HEADERS      = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
CATEGORIES_FILE = "categories.json"    # tu fichero de categorías

# ————— Carga categorías —————
with open(CATEGORIES_FILE, "r", encoding="utf-8") as f:
    categories = json.load(f)

rows = []
for cat in categories:
    cid  = cat["id"]
    name = cat["name"]

    url  = f"https://api.mercadolibre.com/categories/{cid}"
    resp = requests.get(url, headers=HEADERS)

    if resp.status_code != 200:
        print(f"⚠️ Error {resp.status_code} en categoría {cid} ({name})")
        continue

    total = resp.json().get("total_items_in_this_category", 0)
    rows.append({
        "category_id": cid,
        "category_name": name,
        "active_listings": total
    })

# ————— Ordena y exporta —————
# Orden de mayor a menor
rows.sort(key=lambda x: x["active_listings"], reverse=True)

with open("active_listings_all_categories.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["category_id", "category_name", "active_listings"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ Exportado a active_listings_all_categories.csv")
