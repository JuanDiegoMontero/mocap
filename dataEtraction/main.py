from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from bq_client import client
from google.cloud import bigquery

print("BigQuery client usando proyecto:", client.project)
# Ejecutar fast api: uvicorn main:app --reload --host 0.0.0.0 --port 8000

app = FastAPI(
    title="Tendencias API",
    description="API para consultar desde BigQuery",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
    # "https://tu-dominio.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/active-listenings/", summary="Obtener registros de active_listenings")
def get_active_listenings(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_active_listings_all_categories`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("limit", "INT64", limit)]
    )
    try:
        rows = client.query(sql, job_config=job_config).result()
        data = [dict(row) for row in rows]
        return {"count": len(data), "active_listenings": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")


@app.get("/categories/", summary="Obtener todos los category_name")
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


@app.get("/search-trends-by-category/", summary="Obtener registros de stg_search_trends_by_category")
def get_search_trends_by_category(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_search_trends_by_category`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("limit", "INT64", limit)]
    )
    try:
        rows = client.query(sql, job_config=job_config).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")


@app.get("/products-by-category/", summary="Obtener registros de stg_products_by_category")
def get_products_by_category(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_products_by_category`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("limit", "INT64", limit)]
    )
    try:
        rows = client.query(sql, job_config=job_config).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")


@app.get("/ofertas-mercado-libre/", summary="Obtener registros de stg_ofertas_mercado_libre")
def get_ofertas_mercado_libre(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_ofertas_mercado_libre`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("limit", "INT64", limit)]
    )
    try:
        rows = client.query(sql, job_config=job_config).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")


@app.get("/market-activity/", summary="Obtener registros de fact_market_activity")
def get_market_activity(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.fact_market_activity`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[bigquery.ScalarQueryParameter("limit", "INT64", limit)]
    )
    try:
        rows = client.query(sql, job_config=job_config).result()
        return [dict(row) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")


@app.get("/search-trends/", summary="Obtener registros de dim_search_trend")
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


@app.get("/products/", summary="Obtener registros de dim_product")
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


@app.get("/offers/", summary="Obtener registros de dim_offer")
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


@app.get("/active-listing/", summary="Obtener registros de dim_active_listing")
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
