import requests
import time
import json

clientId = '571867020121510'
secretKey = 'EuxoWlaselaymdyGXGR8aB70r1VIF7RW'
redirectURI = 'https://holman.com.co'
code='TG-68648a4dc04a1c0001de40e4-1653870402'

ACCESS_TOKEN = "APP_USR-571867020121510-070121-a570d855eb9364102b7793eba6c59e61-1653870402"
CATEGORY_ID = "MCO1051"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
# url = f"https://api.mercadolibre.com/highlights/MCO/category/{CATEGORY_ID}"
#url = f"https://api.mercadolibre.com/sites/MCO/categories"
url = "https://api.mercadolibre.com/sites/MCO/search?category=MCO1403&sort=sold_quantity_desc&limit=5"


response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
