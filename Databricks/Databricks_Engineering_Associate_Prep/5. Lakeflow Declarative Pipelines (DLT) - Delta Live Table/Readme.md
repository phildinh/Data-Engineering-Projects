# ⚙️ Delta Live Tables – End-to-End ETL Pipeline in Azure Databricks

### Building a Modern ETL Framework Using Auto Loader, Delta Lake, and DLT
**Focus:** Data ingestion, transformation, and aggregation across Bronze, Silver, and Gold layers.

---

## 🚀 Project Overview

This project demonstrates how to build a **fully automated ETL pipeline** using **Delta Live Tables (DLT)** within **Azure Databricks**.  
It leverages **Auto Loader**, **Delta Lake**, and **Streaming Tables** to continuously ingest and transform customer, address, and order data into a curated analytical dataset.

The pipeline follows the **Medallion Architecture (Bronze → Silver → Gold)**, ensuring data quality, traceability, and scalability — all orchestrated with **SQL, Python, and DLT expectations**.

---

## 🧩 Project Objectives

1. **Ingest raw operational data** from multiple sources (JSON, CSV) using Databricks Auto Loader.  
2. **Clean and validate data** with Delta Live Tables Expectations for quality assurance.  
3. **Implement Slowly Changing Dimensions (SCD Type 1 & 2)** for historical accuracy.  
4. **Transform nested structures** (JSON arrays) into flat, analytical formats.  
5. **Aggregate results** into a Gold layer summary for reporting and BI integration.  

---

## 🏗️ Architecture Overview

The ETL follows the classic **Medallion design pattern**, with each layer serving a specific purpose.

![Architecture Diagram 1]
<img width="1867" height="857" alt="image" src="https://github.com/user-attachments/assets/d7df2c83-9cac-4f4a-ac67-f2a5d489c620" />
![DLT Graph View]
<img width="1661" height="508" alt="image" src="https://github.com/user-attachments/assets/91a4eca2-428c-4c01-8516-636d3de582a3" />

| Layer | Purpose | Technology | Description |
|--------|----------|-------------|--------------|
| **Landing** | Raw files stored in ADLS volumes | CSV / JSON | Source data from operational systems |
| **Bronze** | Ingested raw data | Auto Loader | Stream raw data into Delta tables |
| **Silver** | Cleaned & validated data | DLT Expectations + SCD | Apply business rules, constraints, and normalization |
| **Gold** | Aggregated data | SQL (Materialized View) | Join and summarize results for reporting |

---

## 🧱 Section 1: Environment Setup  
📘 *Notebook: `01. Set-up Project Environment.ipynb`*

This notebook initializes the Databricks workspace and connects Unity Catalog with the data lake.  
Key steps include:
- Creating **catalog**, **schema**, and **external locations**.  
- Mounting **Azure Data Lake Storage** (ADLS).  
- Registering credentials for **Auto Loader** ingestion.  

*Outcome:*  
A fully configured environment ready for streaming ingestion through DLT.

---

## 🔹 Section 2: Process Customers Data  
📘 *Notebook: `02. Process Customers Data - SQL.ipynb`*

### **Bronze Layer**
- Ingest customer data (JSON) using `cloud_files` with Auto Loader.
- Capture metadata fields like file path and ingestion timestamp.
- Define a streaming table: `bronze_customers`.

### **Silver Layer**
- Clean customer attributes using constraints:
  - Remove null IDs or invalid names.
  - Validate `date_of_birth` and `email` formats.
- Store clean results as `silver_customers_clean`.
- Apply **SCD Type 1** logic via `APPLY CHANGES INTO` for latest customer state.

### **Example SQL Flow**
bronze_customers → silver_customers_clean → silver_customers


---

## 🔹 Section 3: Process Addresses Data  
📘 *Notebook: `03. Process Addresses Data - Python.ipynb`*

### **Bronze Layer**
- Use **Python + Auto Loader** to ingest CSV address files.
- Add ingestion metadata (`input_file_path`, `ingest_timestamp`).

### **Silver Layer**
- Clean address fields and cast `created_date` as date.
- Apply **SCD Type 2** logic with `dlt.apply_changes()` for versioned address tracking.

### **Flow**
bronze_addresses → silver_addresses_clean → silver_addresses (SCD2)

This ensures historical address changes per customer are fully preserved.

---

## 🔹 Section 4: Process Orders Data  
📘 *Notebook: `04. Process Orders Data - SQL.ipynb`*

### **Bronze Layer**
- Ingest order data from JSON using Auto Loader.
- Add ingestion timestamps and lineage tracking.

### **Silver Layer**
- Enforce **data quality constraints**:
  - Non-null `order_id` and `customer_id`.
  - Valid `payment_method` and `order_status` values.
- Flatten nested JSON `items` array using `EXPLODE()` to produce item-level granularity.

### **Flow**
bronze_orders → silver_orders_clean → silver_orders

---

## 🥇 Section 5: Create Customer Order Summary  
📘 *Notebook: `05. Create Customer Order Summary.ipynb`*

### **Gold Layer**
This layer aggregates data across all entities into a single, analytics-ready table.

- Joins **Silver Customers**, **Silver Addresses**, and **Silver Orders**.
- Filters for **active addresses** only (`__END_AT IS NULL`).
- Computes key business metrics:
  - Total Orders per Customer  
  - Total Items Ordered  
  - Total Order Value  

### **Materialized View**
`gold_customer_order_summary`  
continuously refreshes as upstream data changes.

### **Flow**
silver_customers + silver_addresses + silver_orders → gold_customer_order_summary

---

## 🧠 Data Flow Summary

The end-to-end pipeline automates ingestion, cleaning, and transformation with continuous data updates.

| Layer | Data Entities | Technologies Used | Type |
|--------|----------------|------------------|------|
| **Bronze** | Customers, Addresses, Orders | Auto Loader | Streaming |
| **Silver** | Customers (SCD1), Addresses (SCD2), Orders (Flattened) | DLT + Expectations | Streaming |
| **Gold** | Customer Order Summary | SQL + Materialized View | Batch/Stream Hybrid |

---

## 🔁 End-to-End DLT Graph

The Delta Live Tables flow dynamically tracks dependencies and lineage:

![DLT Graph View](<attach_your_second_image_here>)

- Green nodes = active streaming tables  
- Blue node = materialized view (Gold layer)  
- Automated lineage = ensures data consistency and refresh propagation

---

## 🧭 Tech Stack

| Component | Description |
|------------|-------------|
| **Azure Databricks** | Compute and orchestration environment |
| **Delta Live Tables (DLT)** | ETL orchestration with data quality & expectations |
| **Delta Lake** | Transactional data lake storage |
| **Auto Loader (cloudFiles)** | Incremental ingestion framework |
| **Unity Catalog** | Governance and data lineage management |
| **Python & SQL** | Transformation logic for structured and streaming data |

---

## 📊 Business Value

This pipeline enables:
- **Real-time visibility** into customer purchasing behavior  
- **Accurate historical tracking** via SCD implementation  
- **Reliable data governance** with Unity Catalog integration  
- **Seamless BI connectivity** for Power BI or Tableau dashboards  

---

## 🧩 Key Learnings

- DLT simplifies orchestration compared to traditional ETL notebooks.  
- Auto Loader provides scalability and schema evolution.  
- Expectations and constraints improve trust in data quality.  
- SCD Type 1 & 2 support ensures both accuracy and historical insight.  

---

## 👨‍💻 Author

**Phil Dinh**  


