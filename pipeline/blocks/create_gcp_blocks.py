from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp.bigquery import BigQueryWarehouse
# programmatic way for creating GCP blocks instead creation in the UI
# insert your own service_account_file path or service_account_info dictionary from the json file

# copy your gcp credentials info or use the file method.
service_account_info = {
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "SERVICE_ACCOUNT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"
}


credentials_block = GcpCredentials(
    service_account_info= service_account_info
)
credentials_block.save("gcp-credentials-block-name", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("gcp-credentials-block-name"),
    bucket="bucket-name",  # insert your GCS bucket name
)

bucket_block.save("block-gcp-bucket", overwrite=True)

bigquery_block = BigQueryWarehouse(
    gcp_credentials=GcpCredentials.load("gcp-credentials-block-name"),
)

bigquery_block.save("bq-bucket-block-name", overwrite=True)