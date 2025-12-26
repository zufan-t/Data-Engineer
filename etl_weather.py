import os
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import pytz

API_KEY = os.getenv("WEATHER_API_KEY")
DB_URI = os.getenv("DB_URI")

CITIES = ["Sukabumi", "Jakarta", "Surabaya", "Semarang", "Bandung"]

def run_etl():
    print("--- MULAI PROSES ETL ---")
    data_list = []
    
    for city in CITIES:
        print(f"Mengambil data cuaca kota: {city}...")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},ID&appid={API_KEY}&units=metric"
        resp = requests.get(url)
        
        if resp.status_code == 200:
            d = resp.json()
            row = {
                "city_name": city,
                "temperature_celsius": d["main"]["temp"],
                "humidity_percent": d["main"]["humidity"],
                "weather_condition": d["weather"][0]["main"],
                "recorded_at": datetime.now(pytz.timezone('Asia/Jakarta'))
            }
            data_list.append(row)
        else:
            print(f"Gagal ambil data {city}")

    df = pd.DataFrame(data_list)
    print(f"Berhasil mengumpulkan {len(df)} baris data.")

    if not df.empty:
        try:
            print("Sedang mengirim ke Supabase...")
            engine = create_engine(DB_URI)
            df.to_sql('weather_logistics', engine, if_exists='append', index=False)
            print("SUKSES! Data tersimpan di Cloud.")
        except Exception as e:
            print(f"ERROR DATABASE: {e}")
    else:
        print("Tidak ada data untuk dikirim.")

if __name__ == "__main__":
    run_etl()