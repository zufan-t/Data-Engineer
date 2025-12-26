# UNNES Smart Drink Sales Predictor 🥤🌤️

![Python](https://img.shields.io/badge/Python-3.8-3776AB?logo=python&logoColor=white) ![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.7-017CEE?logo=apacheairflow&logoColor=white) ![dbt](https://img.shields.io/badge/dbt-Core-FF694B?logo=dbt&logoColor=white) ![BigQuery](https://img.shields.io/badge/Google_BigQuery-Sandbox-669DF6?logo=googlecloud&logoColor=white)

## Executive Summary

This project represents the convergence of Data Engineering and Entrepreneurship. Developed as a strategic tool for a university business assignment at **Universitas Negeri Semarang (UNNES)**, the system aims to optimize the daily inventory of a beverage business by leveraging real-time weather data.

By analyzing current weather conditions and forecasts around the campus area, the system predicts customer demand patterns—specifically shifting preferences between cold refreshments and warm beverages. This data-driven approach minimizes inventory waste (perishable goods like ice cubes) and maximizes sales opportunities during specific weather events.

## Technical Architecture

The solution implements a **Modern Data Stack** architecture that prioritizes automation and cost-efficiency. It operates on a fully containerized environment orchestrated by Apache Airflow.

```mermaid
graph LR
    A[OpenWeatherMap API] -->|Python Extraction| B[BigQuery Raw Layer]
    B -->|dbt Transformation| C[BigQuery Sales Mart]
    C -->|Visualization| D[Looker Studio Dashboard]
    
    subgraph "Orchestration (Docker)"
        E[Apache Airflow]
        E --> A
        E --> C
    end