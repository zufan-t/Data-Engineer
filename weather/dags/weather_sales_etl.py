from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import json
from google.oauth2 import service_account

PROJECT_ID = 'proyek1-476022'
DATASET_RAW = 'raw_data_layer'
API_KEY = 'type your APIkey here'
LAT = '-7.052' 
LON = '110.418'
KEY_PATH = '/opt/airflow/keys/gcp_credentials.json'

default_args = {
    'owner': 'zufan_entrepreneur',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_weather_data(**kwargs):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    forecast_list = []
    for item in data['list']:
        forecast_list.append({
            'dt_txt': item['dt_txt'],
            'temp': item['main']['temp'],
            'feels_like': item['main']['feels_like'],
            'humidity': item['main']['humidity'],
            'weather_main': item['weather'][0]['main'],
            'weather_desc': item['weather'][0]['description'],
            'ingestion_time': datetime.now()
        })
    
    df = pd.DataFrame(forecast_list)
    
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    df.to_gbq(
        destination_table=f'{DATASET_RAW}.unnes_weather_forecast',
        project_id=PROJECT_ID,
        credentials=credentials,
        if_exists='replace'
    )
    print("Data Weather Loaded to Raw Layer!")

with DAG(
    'unnes_smart_sales_predictor',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    t1_extract = PythonOperator(
        task_id='fetch_openweather_api',
        python_callable=extract_weather_data
    )

    t2_dbt_run = BashOperator(
        task_id='dbt_transform_logic',
        bash_command='cd /opt/airflow/unnes_weather_dbt && dbt run --profiles-dir .'
    )

    t1_extract >> t2_dbt_run
