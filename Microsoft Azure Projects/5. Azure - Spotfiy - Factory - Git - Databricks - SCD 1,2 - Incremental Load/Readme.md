# 🎧 Azure Data Engineering Project — Spotify Analytics Pipeline

This project demonstrates a full end-to-end **Modern Data Engineering Architecture** on Microsoft Azure.  
The solution ingests data from Azure SQL Database → processes it through Azure Data Factory → lands it into a Bronze/Silver/Gold Medallion architecture using Azure Databricks with Unity Catalog.  
The pipeline supports **incremental ingestion**, **SCD Type 2** dimension tracking, and **Spark Structured Streaming** for near-real-time gold-layer transformations.

---

## 🏗️ 1. Environment Setup & Architecture Overview

In this project, I provisioned all required Azure resources inside one resource group:

- Azure SQL Database (source system)
- Azure Data Factory (or ADF V2)
- Azure Databricks Workspace
- Access Connector for Databricks (managed identity)
- Azure Storage Account (Lakehouse storage)
- API Connection for alerts/notifications
- Logic App for optional notifications

This environment forms the basis for a **modern lakehouse pipeline** using the medallion architecture.

> 📸 **Picture 1 — Azure Resource Group Setup**  
<img width="1723" height="760" alt="image" src="https://github.com/user-attachments/assets/05bc57ad-8641-4079-a01d-a3f820ef1e78" />


---

## 🚀 2. Data Ingestion — Azure Data Factory

Azure Data Factory orchestrates ingestion from SQL Database into the Lakehouse Bronze layer.

### 2.1 Pipeline Features
- Parameterized pipelines (schema, table, cdc column, from_date)
- Lookup activity to read last CDC timestamp
- ForEach loop to process multiple tables dynamically
- Conditional “If incremental needed → run copy” logic
- Copy activity to land files into **Bronze** container
- On-success notification using Web/Logic App
- GitHub integration for storing ADF JSON templates  
  (connected to GitHub repo for CI/CD tracking)

### 2.2 Incremental Load Logic
- Reads metadata table storing last successful load time
- Applies filter on SQL table using CDC column  
  Example: `WHERE updated_at > @last_timestamp`
- Writes new files as parquet/csv into Bronze
- Updates metadata after each run

> 📸 **Picture 2 — Azure Data Factory Pipeline (Lookup → Copy → If Condition)**  
<img width="1158" height="449" alt="image" src="https://github.com/user-attachments/assets/4450044e-425f-4950-8d89-3b74df937c05" />


---

## 🪣 3. Bronze Layer — Raw Landing Zone

The Bronze layer stores:
- Raw SQL extracts  
- Incremental batches  
- CDC-based raw snapshots  

Files are stored with:
- Date-based folder structure  
- Schema-by-schema organization  
- Metadata columns (ingestion timestamp, file name)

This layer acts as the immutable source for downstream processing.

---

## 🔧 4. Azure Databricks — Silver Transformation

Databricks notebooks (Python & Spark SQL) transform raw data into clean, validated Silver tables.

### 4.1 Unity Catalog Integration
Used Unity Catalog to ensure:
- Centralized governance  
- Secure credential passthrough  
- Table lineage & auditing  
- Schema enforcement at catalog level  
- Clean separation: `catalog.schema.table`

### 4.2 Silver Layer Transformations
- Casting & normalization  
- Data quality enforcement (null checks, dedupe, schema enforcement)  
- Surrogate keys and standardized entities  
- Standard SCD Type 2 logic for dimension tables  
  (effectiveStartDate, effectiveEndDate, isCurrent flags)

### 4.3 Storage Structure
- `/catalog/bronze/...`
- `/catalog/silver/...`

Silver tables feed into the Gold layer for analytical consumption.

---

## 🟡 5. Gold Layer — Spark Structured Streaming

The Gold layer uses **Structured Streaming** in Databricks to keep analytical tables updated automatically.

### 5.1 Why Streaming?
Even though the source is batch, structured streaming allows:
- Continuous pipeline execution  
- Auto-trigger on new Bronze/Silver files  
- Metadata-driven transformations  
- Low-latency updates  
  
### 5.2 Metadata-Driven Processing
Reusable metadata tables store:
- Source table names  
- Columns  
- Primary keys for dedupe  
- Refresh mode (full, incremental, streaming)  
- SCD Type configurations  

The streaming pipeline dynamically reads these configurations and applies transformations.

### 5.3 Gold Outputs
- Fact tables (FactStream, FactTrack, FactUser…)  
- Dimensional models using SCD2  
- STAR schema optimized for BI & reporting  

> 📸 **Picture 3 — Databricks Gold Pipeline (Streaming Tables)**  
<img width="1910" height="975" alt="image" src="https://github.com/user-attachments/assets/8ea0e6e1-aa82-4fa5-993d-2318256c9602" />


---

## 🧱 6. SCD Type 2 Implementation (Gold + Silver)

Gold and Silver layers use SCD Type 2 logic to track historical changes:

- Detect changes using hash comparison  
- End previous record by setting `endDate`  
- Insert new record with `startDate`  
- Mark latest record `isCurrent = true`  

This ensures historical traceability for Spotify dimension entities like:
- Artist  
- Track  
- User  
- Date  

---

## 🔄 7. CI/CD & GitHub Integration

ADF pipelines are version-controlled via GitHub:
- Every ADF change triggers a commit  
- JSON pipeline templates stored in repo  
- Supports future deployment via Azure DevOps or GitHub Actions  

Databricks also synchronizes notebooks using:
- Repo integration  
- DBC export files  
- Managed versioning through Git

This improves reproducibility and deployability of the entire solution.

---

## 🧩 8. End-to-End Data Flow Summary
Azure SQL DB
↓ (Incremental Copy with ADF)
Bronze Layer (Raw)
↓ (Databricks ETL)
Silver Layer (Cleaned, Validated)
↓ (Streaming, SCD2, Aggregations)
Gold Layer (Business-ready)
↓
Power BI / Analytics / Reporting

---

## 🏁 9. What This Project Demonstrates

- Modern Azure lakehouse architecture  
- Parameterized, metadata-driven pipelines  
- Orchestration with ADF  
- Incremental ingestion with CDC patterns  
- Databricks transformation with Unity Catalog  
- Gold-layer streaming pipelines  
- SCD Type 2 dimensional modeling  
- CI/CD with GitHub  
- End-to-end data governance and security  

---

## 📌 10. Next Enhancements (Optional)
- Add ADF triggers (event-based for new files)  
- Add cost optimization for Databricks clusters  
- Move to Delta Live Tables (DLT) for managed pipelines  
- Add Power BI semantic model  

---




