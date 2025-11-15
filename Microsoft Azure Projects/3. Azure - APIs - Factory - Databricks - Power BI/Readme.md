# 🚀 Data Engineering Project 3: Pulling Data via APIs in Azure, Transforming in Databricks, and Reporting in Power BI

<img width="1612" height="1016" alt="image" src="https://github.com/user-attachments/assets/098c6fe2-62b9-41a6-aeb8-6bb1cd6077be" />

## 📌 Project Overview

This project demonstrates a modern **data engineering pipeline** on **Microsoft Azure**, where raw data is ingested via APIs, transformed through Databricks (PySpark), and delivered to Power BI for business reporting.

The architecture follows the **Bronze → Silver → Gold** layered approach:

- **Bronze**: Raw data storage in Azure Data Lake  
- **Silver**: Cleaned & transformed data using Databricks (PySpark)  
- **Gold**: Aggregated & curated data in SQL Database (Delta Lake) for analytics and reporting  

---

## 🔧 Environment Setup

- **Azure Resources**: Resource Group, Storage Account, Data Factory, Databricks Workspace  
- **Identity & Access**: Microsoft Entra ID + IAM roles for secure connections  
- **Reporting Tool**: Power BI  

---

## 🛠 Step 1: Create Resources in Microsoft Azure

To begin, we provisioned the required cloud infrastructure in Azure:

- **Resource Group** → Logical container for all services  
- **Storage Account** → Houses Azure Data Lake (Gen2) for raw and processed data  
  - Containers:  
    - `bronze` (raw data)  
    - `silver` (cleaned data)  
    - `gold` (final reporting data)  
- **Azure Data Factory (ADF)** → For orchestrating API ingestion pipelines  
- **Azure Databricks** → For scalable data processing and transformation  
- **SQL Database / Delta Lake** → For Gold layer storage and Power BI integration  

👉 Each resource is created under a **single Resource Group** for centralized management.

<img width="1912" height="605" alt="image" src="https://github.com/user-attachments/assets/84dbe20d-b737-4f8e-a34e-240298f52483" />

---

## 🛠 Step 2: Build Pipeline in Azure Data Factory

### 🔗 Create Linked Services

Configured **Linked Services** to connect ADF with:

- **HTTP API endpoint** (data source)  
- **Azure Data Lake Storage** (data destination)  

This ensures ADF can authenticate and securely move data from API → Storage.  

<img width="1915" height="530" alt="image" src="https://github.com/user-attachments/assets/300f2b9f-6155-4570-be02-730e35b9fb78" />

---

### 📥 Create Pipeline to Pull API Data

- Used **Copy Activity** in ADF pipeline:  
  - **Source**: API request (HTTP GET/POST)  
  - **Sink**: Store JSON response into **Bronze layer** (`bronze/raw_data/`) as **Parquet** files for efficient storage.  
- Scheduled pipeline with **Triggers** for automated execution (daily/hourly).  

<img width="1914" height="608" alt="image" src="https://github.com/user-attachments/assets/dae2ace1-f02b-40aa-a278-1489ae74fe90" />

---

## 🛠 Step 3: Transform Data in Azure Databricks

### 🔎 Check Bronze Layer

- Verified raw ingestion: Data is stored in **Parquet** format in the Bronze container.  
- PySpark scripts ensure schema enforcement and data validation.  

<img width="1916" height="816" alt="image" src="https://github.com/user-attachments/assets/743e5b7d-1e10-4ae5-b9c7-3f2c6d924dbf" />

---

### 🔗 Configure Access to Storage (IAM + Entra ID)

- Integrated **Databricks with Storage Account** using **Entra ID Service Principal + IAM role assignment**.  
- This enables Databricks clusters to directly access Azure Data Lake.  

<img width="1914" height="728" alt="image" src="https://github.com/user-attachments/assets/1bb98655-196c-4d62-a514-716bc7391b58" />  
<img width="1906" height="654" alt="image" src="https://github.com/user-attachments/assets/92a3b96b-0458-4228-ad6d-1552d4656e2f" />

---

### ⚙️ Databricks Compute

- Created **Databricks Cluster (Compute)** for running PySpark jobs.  
- Configured **runtime with Delta Lake support** for optimized transformations.  

<img width="1907" height="828" alt="image" src="https://github.com/user-attachments/assets/e8b6d02d-6ff8-468c-9c11-031c523d143e" />

---

### 🧹 Silver Layer Transformation

PySpark scripts clean and standardize data:

- Remove nulls / duplicates  
- Normalize column naming conventions  
- Flatten nested JSON fields  

Data saved into **Silver container** in **Delta format** for ACID transactions & versioning.

---

### 📊 Gold Layer Transformation

Business-level aggregation and modeling:

- Join multiple Silver tables  
- Apply calculations (KPIs, metrics)  
- Build fact and dimension tables  

Data stored in **Gold layer** within SQL Database / Delta Tables, ready for analytics.

---

## 🛠 Step 4: Connect Databricks / SQL to Power BI

- Configured **ODBC/JDBC connection** from Power BI to **Azure SQL Database / Databricks SQL Endpoint**.  
- Built interactive dashboards in **Power BI**:  
  - Visualizations for KPIs  
  - Drill-down by dimensions (time, region, category)  
  - Auto-refresh via scheduled refresh in Power BI Service  

---

## 📐 Project Architecture

flowchart TD:

-  API[API Source] --> ADF[Azure Data Factory<br/>(Pipelines)]
-  ADF --> Bronze[Bronze Layer<br/>(Raw Data in Parquet/JSON)]
-  Bronze --> DBX[Azure Databricks<br/>PySpark Transformations]
-  DBX --> Silver[Silver Layer<br/>(Cleaned & Standardized)]
-  Silver --> Gold[Gold Layer<br/>(Business Models & KPIs)]
-  Gold --> SQL[SQL Database / Delta Lake]
-  SQL --> PBI[Power BI Dashboards]


---

## ✅ Key Learnings & Best Practices

- **Bronze → Silver → Gold layering** enforces data quality and governance.  
- **Delta Lake format** provides reliability (ACID compliance, schema evolution, time travel).  
- **ADF Pipelines** allow automation and monitoring of ingestion workflows.  
- **Databricks + Power BI** offers an end-to-end modern analytics stack.  
- **IAM + Entra ID integration** secures access and prevents key exposure.  

---


---

