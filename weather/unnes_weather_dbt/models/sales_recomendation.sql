{{ config(materialized='table') }}

WITH raw_data AS (
    SELECT 
        CAST(dt_txt AS TIMESTAMP) as waktu_prediksi,
        temp as suhu_celcius,
        humidity as kelembaban,
        weather_main as kondisi_utama
    FROM `{{ target.project }}.raw_data_layer.unnes_weather_forecast`
)

SELECT
    waktu_prediksi,
    suhu_celcius,
    kondisi_utama,
    CASE 
        WHEN kondisi_utama IN ('Rain', 'Drizzle') THEN 'Wedang Jahe/Kopi'
        WHEN suhu_celcius >= 30 THEN 'Es Jumbo (Extra Ice)'
        ELSE 'Es Teh/Jeruk Biasa'
    END AS rekomendasi_jualan
FROM raw_data
WHERE waktu_prediksi >= CURRENT_TIMESTAMP()
ORDER BY waktu_prediksi ASC