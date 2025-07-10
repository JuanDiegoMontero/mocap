import requests
import time
import json
import os


clientId = '571867020121510'
secretKey = 'EuxoWlaselaymdyGXGR8aB70r1VIF7RW'
redirectURI = 'https://holman.com.co'
code='TG-68648a4dc04a1c0001de40e4-1653870402'

ACCESS_TOKEN = "APP_USR-571867020121510-070121-a570d855eb9364102b7793eba6c59e61-1653870402"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

# Configuración
SITE_ID = "MCO"  # Colombia
BASE_URL = "https://api.mercadolibre.com"
DATA_FILE = "data.json"  # Archivo con [{"id":"MCOxxx","name":"..."}, ...]

def load_categories(filepath):
    """
    Carga la lista de categorías desde un JSON local.
    Espera un array de objetos con 'id' y 'name'.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No existe el archivo de categorías: {filepath}")
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

def fetch_top_products_by_category(cat_id, limit=5):
    """
    Obtiene los productos ordenados por cantidad vendida (más vendidos primero).
    API: GET /sites/{site_id}/search
    Parámetros:
      - category: ID de categoría
      - sort: sold_quantity_desc
      - limit: número de resultados
    """
    params = {
        "category": cat_id,
        "sort": "sold_quantity_desc",
        "limit": limit
    }
    url = f"{BASE_URL}/sites/{SITE_ID}/search"
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    products = []
    for item in data.get("results", []):
        products.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "price": item.get("price"),
            "sold_quantity": item.get("sold_quantity"),
            "permalink": item.get("permalink"),
            "thumbnail": item.get("thumbnail"),
        })
    return products

def main():
    # 1. Leer categorías desde data.json
    try:
        categories = load_categories(DATA_FILE)
    except Exception as e:
        print(f"❌ Error cargando categorías: {e}")
        return

    # 2. Para cada categoría, obtener los 5 productos más comprados
    result = {}
    for cat in categories:
        cat_id = cat.get("id")
        cat_name = cat.get("name")
        if not cat_id or not cat_name:
            continue
        print(f"📦 Obteniendo top productos para «{cat_name}» (ID={cat_id})...")
        try:
            products = fetch_top_products_by_category(cat_id, limit=5)
            result[cat_name] = products
        except Exception as e:
            print(f"  ❌ Error en categoría {cat_name}: {e}")
        time.sleep(0.2)  # pequeño delay para no golpear la API

    # 3. Imprimir JSON final
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
