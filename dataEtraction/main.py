from fastapi import FastAPI, HTTPException, Query
from bq_client import client
from google.cloud import bigquery

print("BigQuery client usando proyecto:", client.project)
# Ejecutar fast api: uvicorn main:app --reload --host 0.0.0.0 --port 8000


app = FastAPI(
    title="Tendencias API",
    description="API para consultar desde BigQuery",
    version="1.0.0",
)

@app.get("/active-listenings/", summary="Obtener registros de active_listenings")
def get_active_listenings(
    limit: int = Query(100, ge=1, le=1000, description="Número máximo de filas a retornar")
):
    """
    Devuelve hasta `limit` filas de la tabla mercadolibre.dim_active_listenings.
    """
    sql = """
        SELECT *
        FROM `tendencias-464719.mercadolibre_analytics.stg_active_listings_all_categories`
        LIMIT @limit
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("limit", "INT64", limit)
        ]
    )
    try:
        query_job = client.query(sql, job_config=job_config)  # ejecuta la consulta
        rows = query_job.result()  # espera a que termine
        data = [dict(row) for row in rows]
        return {"count": len(data), "active_listenings": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar BigQuery: {e}")
