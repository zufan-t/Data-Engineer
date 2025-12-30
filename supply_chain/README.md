**FMCG Supply Chain ELT Pipeline**
The FMCG Supply Chain ELT Pipeline is a high-volume data engineering system designed to simulate the supply chain operations of a Fast-Moving Consumer Goods (FMCG) company. It focuses on the real-time generation and ingestion of inventory transaction data for flagship products such as Pocari Sweat and Soyjoy. This project demonstrates a Direct-to-Warehouse strategy that prioritizes speed and cost-efficiency in modern data architecture.

**Project Description**
This project implements a fully automated Extract, Load, Transform (ELT) workflow. It replaces the traditional method of using intermediate cloud storage buckets with a direct ingestion path from the data source to the warehouse. The system is built using a Modern Data Stack that includes Python for data generation, Google BigQuery for storage and transformation, and Apache Airflow for orchestration. The entire environment is containerized via Docker, ensuring that the pipeline is reproducible and can be deployed across various production environments.

**Problem Statement**
FMCG companies often struggle with the following challenges in their data infrastructure.

- High Intermediate Storage Costs Traditional pipelines often require data to be stored in staging buckets like Amazon S3 or Google Cloud Storage before it is moved to a warehouse. For high-volume transaction data, these storage costs can accumulate rapidly.

- Latency in Data Availability Multi-step pipelines introduce delays between the time a transaction occurs in the warehouse and when it appears in a business report. This latency prevents supply chain managers from responding quickly to sudden stock shortages.

- Operational Complexity Managing multiple cloud services and manual scripts leads to a fragmented pipeline that is difficult to monitor and prone to failure during high-demand periods.

**Goals and Benefits**
The primary objective is to create a lean and high-performance data pipeline for supply chain monitoring.

- Direct-to-Warehouse Ingestion The system uses the ELT paradigm to move data directly into the BigQuery staging area. This eliminates the need for expensive intermediate storage layers.

- Automated Workflow Orchestration By using Apache Airflow on Docker, the pipeline manages the timing and dependency of every task, ensuring data is always up to date without manual intervention.

- Optimized Data Structure The transformation layer converts raw transaction logs into a Star Schema format. This makes the data ready for complex business intelligence queries and real-time reporting.

- Resource Reproducibility The containerized approach ensures that the entire data stack can be launched or scaled with a single command, maintaining consistency between development and production.

**Technical Results and Outputs**
The project delivers a functional and scalable supply chain data infrastructure.

**Real-Time Mock Data Generator**
The pipeline includes a specialized Python generator that creates high-velocity transaction data. This simulates a busy FMCG distribution center, producing logs for thousands of units of inventory moving through the supply chain.

**BigQuery Staging and Warehouse Layer**
The data is successfully ingested into a BigQuery Sandbox.

- Staging Layer: Holds the raw, incoming transaction data.

- Data Warehouse Layer: Contains structured Star Schema tables designed for fast analytical queries.

**SQL Merge and Upsert Logic**
The transformation phase uses advanced SQL Merge statements to handle data updates. This ensures that the warehouse maintains a single version of the truth by updating existing records and inserting new ones without creating duplicates.

**Performance Monitoring Dashboard**
The output is ready for integration with visualization tools like Looker Studio or Power BI, allowing managers to see real-time inventory levels and warehouse movement trends.

**Conclusion**
The FMCG Supply Chain ELT Pipeline proves that a Direct-to-Warehouse approach is highly effective for high-volume retail environments. By removing unnecessary storage steps and focusing on a robust ELT architecture, the system provides faster data availability while significantly reducing cloud infrastructure costs. This project serves as a scalable template for any FMCG organization looking to modernize their supply chain analytics and achieve greater operational transparency.