# 🧠 Apache Spark – Querying & Transforming Data (CSV & JSON)  
### Using Spark in Azure Databricks to Transform Data within Medallion Architecture  
**Focus:** JSON Transformation, Data Governance with Unity Catalog, and Data Processing via PySpark  

---

## 🚀 Project Overview

This project demonstrates how to **query, transform, and manage data** in **Azure Databricks** using **Apache Spark**.  
It focuses on building a **Medallion Architecture (Bronze → Silver → Gold)** with proper data governance enabled by **Unity Catalog**.

You’ll see how to extract data from multiple formats (CSV, JSON, and unstructured images), clean and enrich it using PySpark, and store transformed outputs into different layers.

<img width="1895" height="1021" alt="image" src="https://github.com/user-attachments/assets/364be432-9f2f-4c95-8a1b-15d7ab593779" />

---

## 🏗️ Big Steps Overview

1. **Environment Setup:** Configure Azure subscription, create resources, storage account, connectors, and Databricks workspace.  
2. **Data Access Configuration:** Load raw data to the storage account, define Access Control, and connect Databricks to storage using Unity Catalog (metastore, credentials, external locations).  
3. **Data Transformation & Querying:** Follow notebooks `01` → `18` to build Bronze, Silver, and Gold layers using PySpark to extract, transform, and save data in both **CSV** and **JSON** formats.

---

## 🧩 Section 1: Environment Setup

- **Goal:** Build a complete data analytics environment in Azure.
- **Steps:**
  - Create **Azure Resource Group**
  - Set up **Storage Account** (container for Bronze, Silver, Gold data)
  - Create **Azure Databricks Workspace**
  - Configure **Service Principal / Connector** for secure access  
<img width="1871" height="617" alt="image" src="https://github.com/user-attachments/assets/4449ccc2-bb89-4886-b0ab-36e138f8c376" />


---

## 🔐 Section 2: Data Access Configuration & Unity Catalog Setup

- **Goal:** Securely connect Databricks to Azure Storage and enable governance.  
- **Steps:**
  - Upload raw CSV and JSON data to **Storage Account**
  - Assign roles via **IAM** for Databricks access
  - Create **Unity Catalog Metastore** and link it to your workspace
  - Register **External Locations**, **Credentials**, and **Schemas**  
- *(Storage account upload screen)*
<img width="1583" height="726" alt="image" src="https://github.com/user-attachments/assets/cf20072a-db30-47a6-b5b7-1df6c3941efc" />

- *(Access control setup)*
<img width="1888" height="985" alt="image" src="https://github.com/user-attachments/assets/b3639e35-478e-4911-9941-823f4b18d468" />
<img width="1890" height="989" alt="image" src="https://github.com/user-attachments/assets/08caaa33-3368-44a4-908a-9cf780522525" />

---

## 💡 Section 3: Data Transformation Workflow (Notebooks 01 → 18)

Each notebook represents a stage of extraction, transformation, or analysis in the Medallion Architecture.

<img width="1906" height="967" alt="image" src="https://github.com/user-attachments/assets/3539ef43-561e-4fc6-8cb8-61de24efe0f0" />


### 🔹 01. `Set-up Project Environment.ipynb`
Initialize Spark session, configure Unity Catalog connection, and define paths for raw (bronze), processed (silver), and curated (gold) data layers.

### 🔹 02. `Extract Customer Data – JSON.ipynb`
Read structured JSON data (customer info) into a Spark DataFrame, explore schema, and perform initial validation.

### 🔹 03. `Extract Orders Data – Complex JSON as Text.ipynb`
Handle **nested JSON** structures using Spark functions like `from_json()` and `explode()` to flatten multi-level data.

### 🔹 04. `Extract Memberships Data – Images.ipynb`
Demonstrate unstructured data handling (e.g., reading image metadata) to store image-related info in the bronze layer.

### 🔹 05. `Extract Addresses Data – CSV via read_files function.ipynb`
Load CSV data using `spark.read.csv()` and custom read functions for schema inference and type enforcement.

### 🔹 06. `Extract Payments Data – CSV via External Table.ipynb`
Create external tables in Databricks referencing Azure Storage, allowing direct query access without data duplication.

### 🔹 08. `Extract Data using Python.ipynb`
Use Python and Spark APIs to extract and preview datasets, highlighting interoperability between PySpark and Python standard libraries.

### 🔹 09. `data Profiling.ipynb`
Perform **data quality checks** (nulls, duplicates, outliers) and **schema validation** before transformations.

---

### 🧪 Transformation Layer (Silver)

### 🔹 10. `Transform Customer Data.ipynb`
Clean, normalize, and standardize customer information. Handle nulls, rename columns, and enforce consistent types.

### 🔹 11. `Transform Payments Data.ipynb`
Convert transaction timestamps, calculate derived metrics (e.g., payment amount in USD), and validate unique transaction IDs.

### 🔹 12. `Transform Refunds Data.ipynb`
Aggregate refund values, detect duplicate refund records, and integrate with payment data for audit accuracy.

### 🔹 13. `Transform Memberships Data.ipynb`
Transform membership tiers, join with customer data, and generate active/inactive flags.

### 🔹 14. `Transform Addresses Data.ipynb`
Clean address data, extract country and postal codes, and merge duplicates using fuzzy matching.

### 🔹 15. `Transform Order Data – JSON.ipynb`
Parse nested JSON order data, normalize multi-line orders, and calculate order totals and item counts.

---

### 🧱 Gold Layer – Business View

### 🔹 16. `Join Customer and Address.ipynb`
Combine transformed customer and address datasets to build a **360° customer view**.

### 🔹 17. `Monthly Order Summary.ipynb`
Aggregate sales and orders by month, product, and region. This forms the **gold summary layer** for business intelligence.

### 🔹 18. `Higher Order Functions.ipynb`
Apply **Spark higher-order functions** (`transform`, `aggregate`, `filter`) for advanced array and struct manipulation on complex JSON data.

---

## 🪶 Summary

This end-to-end project showcases:
- ✅ **Azure Databricks setup** with Unity Catalog for governance  
- ✅ **Spark-based extraction** from CSV, JSON, and image formats  
- ✅ **Incremental transformation pipeline** across Bronze, Silver, and Gold layers  
- ✅ **Data quality and profiling steps** ensuring reliable transformations  
- ✅ **Business-ready outputs** (monthly summaries, 360° customer view)

---

## 🧭 Tech Stack

| Component | Description |
|------------|-------------|
| **Azure Databricks** | Data engineering and transformation platform |
| **Azure Data Lake Storage (Gen2)** | Persistent data storage for Bronze/Silver/Gold |
| **Unity Catalog** | Metadata and access governance |
| **Apache Spark (PySpark)** | Distributed data processing engine |
| **CSV / JSON / Image Data** | Input sources for structured and unstructured data |

---

## 📊 Architecture Diagram

<img width="1895" height="1021" alt="image" src="https://github.com/user-attachments/assets/3b1ba6b5-4ea4-48b0-aa54-2e7fc7d24ae5" />

---

## 🧑‍💻 Author
**Phil Dinh**  



