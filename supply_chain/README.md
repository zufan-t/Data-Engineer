# FMCG Supply Chain ELT Pipeline 🏭

![Python](https://img.shields.io/badge/Python-3.8-3776AB?logo=python&logoColor=white) ![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.7-017CEE?logo=apacheairflow&logoColor=white) ![Google BigQuery](https://img.shields.io/badge/Google_BigQuery-Sandbox-669DF6?logo=googlecloud&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)

## Project Overview

This project simulates a high-volume data pipeline for a Fast-Moving Consumer Goods (FMCG) company similar to PT Amerta Indah Otsuka. The system generates real-time inventory transaction data for products such as **Pocari Sweat** and **Soyjoy**, ingests it directly into a Data Warehouse, and transforms it into a business-ready format.

Unlike traditional pipelines that rely on heavy cloud storage costs, this project implements a **Direct-to-Warehouse** strategy using the **ELT (Extract, Load, Transform)** paradigm. It is fully containerized using Docker and orchestrated by Apache Airflow, ensuring the process is automated, reproducible, and scalable.

## Architecture & Workflow

The pipeline follows a modern ELT approach designed for efficiency and cost optimization:

```mermaid
graph LR
    A[Mock Data Generator] -->|Direct Ingest via Pandas| B[BigQuery Staging Area]
    B -->|SQL Merge & Upsert| C[Data Warehouse]
    
    subgraph "Google BigQuery (Sandbox)"
        B[(staging_inventory)]
        C[(Star Schema Tables)]
    end
    
    subgraph "Orchestration"
        D[Apache Airflow on Docker]
        D --> A
        D --> B
        D --> C
    end