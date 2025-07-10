import json
import requests
import csv



# ——————————————————————————
# token_data = refresh_access_token(clientId, secretKey, refresh_token)
# ACCESS_TOKEN   = token_data["access_token"]
# refresh_token = token_data["refresh_token"]  # guárdalo para la próxima vez
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

    # Nuevo bloque de diagnóstico:
    if r.status_code != 200:
        print("❌ Refresh token failed")
        print("Status code:", r.status_code)
        print("Response body:", r.text)
        raise SystemExit("No puedo continuar sin un token válido.")

    return r.json()

# ——————————————————————————
clientId     = "6186476861975930"
secretKey    = "ugoaf8dHeISwO3Sy5n9UzS640r3nyBz8"
refresh_token = "TG-6865510b4cff350001e2eac0-1653870402"
redirectURI = 'https://pi.udistrital.edu.co/GICOGE/'

ACCESS_TOKEN = 'APP_USR-6186476861975930-070211-ba5e2d3e6b0783d7172a3d9b47510b0d-1653870402'
SITE_ID     = "MCO"
with open("categories.json", "r", encoding="utf-8") as f:
  CATEGORIES = json.load(f)
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Prepare a list to collect all rows
rows = []

for cat in CATEGORIES:
  category_id = cat["id"]
  category_name = cat["name"]

  url = f"https://api.mercadolibre.com/highlights/{SITE_ID}/category/{category_id}"
  resp = requests.get(url, headers=headers)

  if resp.status_code != 200:
    print(f"⚠️ Error {resp.status_code} en {category_name}: {resp.text}")
    continue

  data = resp.json()
  content = data.get("content", [])
  product_ids = [item["id"] for item in content if "id" in item]

  for prod_id in product_ids:
    prod_url = f"https://api.mercadolibre.com/products/{prod_id}"
    p = requests.get(prod_url, headers=headers)

    if p.status_code == 200:
      prod_data = p.json()
      prod_title = prod_data.get("name", "<sin título>")
    else:
      prod_title = f"<error {p.status_code}>"

    # Collect row data
    rows.append({
      "category_id": category_id,
      "category_name": category_name,
      "product_id": prod_id,
      "product_title": prod_title
    })

# Write to CSV
with open("products_by_category.csv", "w", newline="", encoding="utf-8") as csvfile:
  fieldnames = ["category_id", "category_name", "product_id", "product_title"]
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(rows)

print("✅ Datos exportados a products_by_category.csv")
