# AIO Supply Chain Inventory Pipeline 🏭

Portofolio Data Engineering yang mensimulasikan pemrosesan data stok barang (Inventory Management) untuk industri FMCG. Pipeline ini diorkestrasi menggunakan **Apache Airflow**, dijalankan dalam **Docker**, dan menggunakan **Google Cloud Platform (BigQuery & GCS)**.

## 🏗 Architecture
**Flow:** Mock API (Python) -> GCS (Data Lake) -> BigQuery (Staging) -> BigQuery (Star Schema).

![Architecture Diagram](https://via.placeholder.com/800x400?text=Architecture+Diagram+Here)

## 🛠 Tech Stack
- **Language:** Python & SQL
- **Orchestration:** Apache Airflow 2.7
- **Containerization:** Docker
- **Cloud:** Google Cloud Storage & BigQuery

## 🚀 How to Run
1. Clone repo ini.
2. Letakkan Service Account Key GCP di folder `keys/gcp_credentials.json`.
3. Jalankan Docker: `docker-compose up -d`.
4. Akses Airflow UI di `localhost:8080`.
5. Setup koneksi `google_cloud_default` di Admin > Connections.