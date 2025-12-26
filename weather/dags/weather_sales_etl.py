from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
import json
from google.oauth2 import service_account

# --- KONFIGURASI ---
PROJECT_ID = 'proyek1-476022' # Ganti Project ID kamu
DATASET_RAW = 'raw_data_layer' # Dataset untuk data mentah
API_KEY = '4f4cc497beb8ac56b8c43f4cd04c12a9'
LAT = '-7.052' # UNNES
LON = '110.418'
KEY_PATH = '/opt/airflow/keys/gcp_credentials.json'

default_args = {
    'owner': 'zufan_entrepreneur',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_weather_data(**kwargs):
    # URL API untuk 5 day forecast
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    # Ambil list forecast
    forecast_list = []
    for item in data['list']:
        forecast_list.append({
            'dt_txt': item['dt_txt'],
            'temp': item['main']['temp'],
            'feels_like': item['main']['feels_like'],
            'humidity': item['main']['humidity'],
            'weather_main': item['weather'][0]['main'], # Rain, Clear, Clouds
            'weather_desc': item['weather'][0]['description'],
            'ingestion_time': datetime.now()
        })
    
    df = pd.DataFrame(forecast_list)
    
    # Load ke BigQuery Raw
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    df.to_gbq(
        destination_table=f'{DATASET_RAW}.unnes_weather_forecast',
        project_id=PROJECT_ID,
        credentials=credentials,
        if_exists='replace' # Kita replace tiap hari biar fresh
    )
    print("Data Weather Loaded to Raw Layer!")

with DAG(
    'unnes_smart_sales_predictor',
    default_args=default_args,
    schedule_interval='@daily', # Update tiap pagi buat persiapan jualan
    catchup=False
) as dag:

    # 1. Ambil Data Cuaca
    t1_extract = PythonOperator(
        task_id='fetch_openweather_api',
        python_callable=extract_weather_data
    )

    # 2. Transformasi Pakai dbt (Menghitung Prediksi)
    # Kita jalankan perintah "dbt run" via terminal docker
    t2_dbt_run = BashOperator(
        task_id='dbt_transform_logic',
        bash_command='cd /opt/airflow/unnes_weather_dbt && dbt run --profiles-dir .'
    )

    t1_extract >> t2_dbt_run