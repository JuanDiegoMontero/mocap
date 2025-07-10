import json
import requests
import csv

def refresh_access_token(client_id, client_secret, refresh_token):
    url = "https://api.mercadolibre.com/oauth/token"
    payload = {
        "grant_type":    "refresh_token",
        "client_id":     client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, data=payload, headers=headers)
    if r.status_code != 200:
        print("❌ Refresh token failed:", r.status_code, r.text)
        raise SystemExit("No puedo continuar sin un token válido.")
    return r.json()

# ——————————————————————————
clientId      = "6186476861975930"
secretKey     = "ugoaf8dHeISwO3Sy5n9UzS640r3nyBz8"
refresh_token = "TG-6865510b4cff350001e2eac0-1653870402"
SITE_ID       = "MCO"

# Si caduca, descomenta para refrescar:
# token_data   = refresh_access_token(clientId, secretKey, refresh_token)
# ACCESS_TOKEN = token_data["access_token"]

ACCESS_TOKEN = 'APP_USR-6186476861975930-070211-ba5e2d3e6b0783d7172a3d9b47510b0d-1653870402'

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

with open("categories.json", "r", encoding="utf-8") as f:
    CATEGORIES = json.load(f)

rows = []
for cat in CATEGORIES:
    category_id   = cat["id"]
    category_name = cat["name"]

    url = f"https://api.mercadolibre.com/trends/{SITE_ID}/{category_id}"
    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print(f"⚠️ Error {resp.status_code} en categoría {category_name}: {resp.text}")
        continue

    trends = resp.json()
    for item in trends:
        rows.append({
            "category_id":   category_id,
            "category_name": category_name,
            "keyword":       item.get("keyword", ""),
            "url":           item.get("url", "")
        })

# Escribir CSV
with open("search_trends_by_category.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["category_id", "category_name", "keyword", "url"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("✅ Datos exportados a search_trends_by_category.csv")
