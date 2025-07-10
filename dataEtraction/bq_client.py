# bq_client.py
from google.cloud import bigquery
from google.oauth2 import service_account
from pathlib import Path

# Ruta absoluta al JSON de credenciales
BASE_DIR = Path(__file__).parent
CRED_PATH = "./auth/tendencias-464719-9591593eb479.json"

# Cargar credenciales explícitamente
credentials = service_account.Credentials.from_service_account_file(
    str(CRED_PATH)
)

# Instanciar cliente BigQuery apuntando al proyecto "tendencias"
client = bigquery.Client(
    credentials=credentials,
    project=credentials.project_id,
)