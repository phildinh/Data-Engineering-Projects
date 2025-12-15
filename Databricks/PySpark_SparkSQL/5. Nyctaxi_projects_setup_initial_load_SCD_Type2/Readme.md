# NYC Taxi Lakehouse Pipeline – Databricks Portfolio Project

## 📌 Executive Summary
This project demonstrates a production-style Lakehouse data engineering pipeline built on Databricks with Azure Data Lake Storage Gen2 (ADLS2).  
It showcases how to design, govern, and operate an end-to-end analytics platform using Unity Catalog, Delta Lake, and the Medallion (Bronze–Silver–Gold) architecture.

The solution supports historical backfill and incremental ingestion, ensuring scalability, data quality, and zero duplication, while reflecting real-world Databricks enterprise best practices.

---

## 🏗️ Lakehouse Architecture & Governance

### 🔹 Platform Components
- Compute: Databricks (Apache Spark)
- Storage: Azure Data Lake Storage Gen2 (ADLS2)
- Table Format: Delta Lake
- Governance: Unity Catalog
- Orchestration: Databricks Jobs

### 🔹 Catalog & Schema Design
Catalog: nyctaxi

Schemas:
├── 00_landing        Raw external ingestion (system of record)  
├── 01_bronze         Structured raw Delta tables  
├── 02_silver         Cleaned and enriched datasets  
└── 03_gold           Business-ready aggregated datasets  

This structure enforces:
- Clear data ownership and lifecycle management
- Separation of concerns across data layers
- Consistent naming conventions and discoverability
- Enterprise-ready governance boundaries via Unity Catalog

---

## 📥 Data Ingestion Strategy

### 🔹 Source Characteristics
- Dataset: NYC Yellow Taxi trip data
- Source Type: Public HTTP endpoint
- Ingestion Mode: Batch (historical backfill + incremental loads)

### 🔹 Landing Layer Design
Raw data is ingested into the Landing Layer using a date-partitioned folder strategy:

/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/{date}

<img width="1916" height="1025" alt="image" src="https://github.com/user-attachments/assets/478461f3-aa1b-45a2-9b16-81f7bdca27b1" />


Key design principles:
- No transformations applied
- Data stored as managed Delta tables
- Full auditability and replay capability
- Physical storage backed by ADLS2

---

## 🔹 Historical Backfill
Path:
nyctaxi_project/one_off/02.Backfill_historical_yellow_trips

Responsibilities:
- Load historical datasets by date
- Establish a baseline for downstream layers
- Enforce schema consistency across time

---

## 🥉 Bronze Layer – Raw Structured Data
The Bronze Layer converts landing data into structured Delta tables while preserving full data fidelity.

### 🔹 Design Principles
- Schema-on-read ingestion
- One-to-one mapping from Landing Layer
- No business logic or filtering
- Optimized for traceability and debugging

### 🔹 Implementation
Path:
nyctaxi_project/transformations/01_bronze

This layer acts as the deterministic foundation for downstream transformations.

---

## 🥈 Silver Layer – Data Quality & Enrichment
The Silver Layer produces trusted, analytics-ready datasets by applying data quality rules and enrichment logic.

### 🔹 Transformations Applied
- Data type normalization
- Null and invalid value handling
- Timestamp standardization
- Taxi zone enrichment using reference datasets

### 🔹 Silver Outputs
- yellow_trips_cleaned  
- yellow_trips_enriched  

### 🔹 Implementation
Path:
nyctaxi_project/transformations/02_silver

This layer represents the single source of truth for analytical consumption.

---

## 🥇 Gold Layer – Analytics & Business Metrics
The Gold Layer delivers aggregated datasets optimized for BI and analytics workloads.

### 🔹 Business Metrics
- Daily trip volume
- Total fare amount
- Average trip distance

### 🔹 Implementation
Path:
nyctaxi_project/transformations/03_gold

Gold tables are:
- Partitioned for performance
- Designed for direct BI consumption
- Exposed as stable interfaces for reporting tools

---

## 🔁 Incremental Processing & Data Reliability
After the initial backfill, the pipeline transitions to incremental ingestion.

### 🔹 Incremental Load Design
Path:
nyctaxi_project/one_off/initial_load/00_landing_stage

Characteristics:
- Only new datasets are ingested
- No reprocessing of historical data
- Efficient use of compute and storage

### 🔹 Delta Lake Guarantees
- ACID transactions
- Idempotent writes
- Safe retries and reprocessing
- Strong consistency across all layers

---

## ⏰ Orchestration & Automation
The pipeline is orchestrated using Databricks Jobs with a dependency-aware DAG:

Landing → Bronze → Silver → Gold

<img width="1641" height="567" alt="image" src="https://github.com/user-attachments/assets/2da67081-2e1f-407d-93cd-6abc2bd29e18" />


### 🔹 Operational Characteristics
- Scheduled weekly execution
- Task dependencies enforced
- Failure isolation and recovery
- Designed for production-grade operations

---

## 🧠 Engineering Best Practices Demonstrated
- Unity Catalog–based governance
- Medallion (Bronze–Silver–Gold) architecture
- Managed Delta tables on ADLS Gen2
- Historical backfill + incremental ingestion
- Idempotent and fault-tolerant pipelines
- Clear separation of ingestion, transformation, and analytics layers
