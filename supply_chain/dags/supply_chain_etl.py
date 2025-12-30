import os
import random
import uuid
import pandas as pd
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from google.oauth2 import service_account

PROJECT_ID = 'proyek1-476022' 
DATASET_NAME = 'supply_chain_wh'

KEY_PATH = '/opt/airflow/keys/gcp_credentials.json'

default_args = {
    'owner': 'zufan_de',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_and_load_direct(**kwargs):
    print("Generating data...")
    products = [
        {'id': 'SKU-001', 'name': 'Pocari Sweat 350ml', 'category': 'Beverage'},
        {'id': 'SKU-002', 'name': 'Pocari Sweat 500ml', 'category': 'Beverage'},
        {'id': 'SKU-003', 'name': 'Soyjoy Almond', 'category': 'Snack'},
        {'id': 'MAT-001', 'name': 'Raw Sugar', 'category': 'Raw Material'},
        {'id': 'MAT-002', 'name': 'PET Resin', 'category': 'Raw Material'}
    ]
    
    data = []
    
    for _ in range(100):
        prod = random.choice(products)
        row = {
            'transaction_id': str(uuid.uuid4()),
            'product_id': prod['id'],
            'product_name': prod['name'],
            'category': prod['category'],
            'quantity': random.randint(10, 5000),
            'type': random.choice(['INBOUND', 'OUTBOUND']),
            'timestamp': datetime.now()
        }
        data.append(row)
    
    df = pd.DataFrame(data)
    
    print(f"Data generated: {len(df)} rows. Loading to BigQuery...")
    
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    
    df.to_gbq(
        destination_table=f'{DATASET_NAME}.staging_inventory',
        project_id=PROJECT_ID,
        credentials=credentials,
        if_exists='replace', 
        table_schema=[
            {'name': 'transaction_id', 'type': 'STRING'},
            {'name': 'product_id', 'type': 'STRING'},
            {'name': 'product_name', 'type': 'STRING'},
            {'name': 'category', 'type': 'STRING'},
            {'name': 'quantity', 'type': 'INTEGER'},
            {'name': 'type', 'type': 'STRING'},
            {'name': 'timestamp', 'type': 'TIMESTAMP'},
        ]
    )
    print("Success load to Staging!")

with DAG(
    'aio_sandbox_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Direct ETL pipeline for BigQuery Sandbox',
    tags=['aio', 'sandbox']
) as dag:

    t1_direct_load = PythonOperator(
        task_id='extract_and_load_direct',
        python_callable=extract_and_load_direct
    )

    transform_sql = f"""
    -- 1. Create Tables if not exist
    CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_NAME}.dim_product` (
        product_id STRING, 
        product_name STRING, 
        category STRING, 
        updated_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET_NAME}.fact_inventory` (
        transaction_id STRING, 
        product_id STRING, 
        quantity INT64, 
        type STRING, 
        transaction_date TIMESTAMP, 
        job_run_date DATE
    );

    -- 2. Upsert Dimension Table (Product)
    MERGE `{PROJECT_ID}.{DATASET_NAME}.dim_product` T
    USING (
        SELECT DISTINCT product_id, product_name, category 
        FROM `{PROJECT_ID}.{DATASET_NAME}.staging_inventory`
    ) S
    ON T.product_id = S.product_id
    WHEN MATCHED THEN
        UPDATE SET product_name = S.product_name, category = S.category, updated_at = CURRENT_TIMESTAMP()
    WHEN NOT MATCHED THEN
        INSERT (product_id, product_name, category, updated_at)
        VALUES (product_id, product_name, category, CURRENT_TIMESTAMP());

    -- 3. Insert into Fact Table
    INSERT INTO `{PROJECT_ID}.{DATASET_NAME}.fact_inventory`
    SELECT 
        transaction_id,
        product_id,
        quantity,
        type,
        timestamp as transaction_date,
        CURRENT_DATE() as job_run_date
    FROM `{PROJECT_ID}.{DATASET_NAME}.staging_inventory`;
    """

    t2_transform = BigQueryInsertJobOperator(
        task_id='transform_star_schema',
        configuration={
            "query": {
                "query": transform_sql,
                "useLegacySql": False,
            }
        },
        location='US',
        gcp_conn_id='google_cloud_default' 
    )

    t1_direct_load >> t2_transform