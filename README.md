# 🏭 Otsuka Supply Chain Intelligence Pipeline

**Status:** ✅ Running Automatically (Serverless)

## 📖 Latar Belakang (Business Case)
Sebagai produsen minuman isotonik (Pocari Sweat), permintaan pasar sangat dipengaruhi oleh cuaca panas. Proyek ini bertujuan membantu tim Logistik memprediksi lonjakan permintaan (*Demand Forecasting*) dengan memantau suhu real-time di titik distribusi utama.

## 🛠️ Solusi Teknis
Sistem ETL otomatis yang berjalan di Cloud tanpa biaya server ($0 Cost).

* **Sumber Data:** OpenWeatherMap API (Real-time).
* **Otomatisasi:** GitHub Actions (CRON Job / Hourly).
* **Database:** Supabase PostgreSQL (Cloud Warehouse).
* **Tools:** Python 3.9, Pandas, SQLAlchemy.

## 📸 Bukti Berjalan (Proof of Concept)
**1. Otomatisasi Sukses (GitHub Actions):**
![Screenshot GitHub Actions](LINK_GAMBAR_ACTIONS_DISINI)

**2. Data Masuk ke Database (Supabase):**
![Screenshot Supabase](LINK_GAMBAR_SUPABASE_DISINI)
