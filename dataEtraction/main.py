from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bq_client import client
from google.cloud import bigquery

print("BigQuery client usando proyecto:", client.project)
## Ejecutar fast api: uvicorn main:app --reload --host 0.0.0.0 --port 8000

app = FastAPI(
    title="Tendencias API",
    description="API para consultar desde BigQuery",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/active-listenings/")
def get_active_listenings():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_active_listings_all_categories`
    """
    try:
        rows = client.query(sql).result()
        data = [dict(row) for row in rows]
        return {"count": len(data), "active_listenings": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/categories/")
def get_categories():
    sql = """
        SELECT category_name
        FROM `tendencias-464719.mercadolibre_analytics.dim_category`
    """
    try:
        rows = client.query(sql).result()
        return [row["category_name"] for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/search-trends-by-category/")
def get_search_trends_by_category():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_search_trends_by_category`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/products-by-category/")
def get_products_by_category():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_products_by_category`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/ofertas-mercado-libre/")
def get_ofertas_mercado_libre():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_ofertas_mercado_libre`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/market-activity/")
def get_market_activity():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.fact_market_activity`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/search-trends/")
def get_dim_search_trend():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.dim_search_trend`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/products/")
def get_dim_product():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.dim_product`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/offers/")
def get_dim_offer():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.dim_offer`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")

@app.get("/active-listing/")
def get_dim_active_listing():
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.dim_active_listing`
    """
    try:
        rows = client.query(sql).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")
