from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_bucket_name = "YOUR_BUCKET_NAME" # insert your GCS bucket name
    gcs_path = f"{gcs_bucket_name}/data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcp_bucket_block = GcsBucket.load("nyc-taxi-gcp-bucket")
    gcp_bucket_block.get_directory(from_path=gcs_path, local_path=f"./data")

    return Path(f"./data/{color}/{color}_tripdata_{year}-{month:02}.parquet")

@task()
def transform(path: Path) -> pd.DataFrame:
    """Data Cleaning || omit rides with zero passenger count"""
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count : {df['passenger_count'].isna().sum()}")
    df['passenger_count'].fillna(0, inplace = True)
    print(f"post: missing passenger count : {df['passenger_count'].isna().sum()}")

    return df

@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write to Big query"""
    gcp_credentials_block = GcpCredentials.load("gcp-credentials-block-name") # insert your gcp credentials block name

    df.to_gbq(
        destination_table="trips_data_all.table_name", # insert your big query dataset.table_name
        project_id="GCP_PROJECT_ID", # insert your big query prject name
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append"
    )

@flow()
def etc_gcs_to_bg(month, year, column):
    """Main ETL flow to load data into BigQuery"""

    path = extract_from_gcs(color, year, month)
    df = transform(path)
    write_bq(df)

if __name__ == '__main__':
    color = "yellow"
    year = 2021
    months = [1, 2, 3, 4, 5, 6, 7] #only these months are available

    for month in months:
        etc_gcs_to_bg(month, year, color)
