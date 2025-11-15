# 🧱 Delta Lake Project – Building Reliable Data Pipelines in Azure Databricks

### Transforming Data with Delta Format, Transaction Logs, and Time Travel  
**Focus:** Data Reliability, ACID Transactions, and Performance Optimization using Delta Lake

---

## 🚀 Project Overview

This project demonstrates how to use **Delta Lake** within **Azure Databricks** to achieve data reliability and governance across the modern data pipeline.  
It explores the fundamental capabilities of Delta Lake — including transaction logs, time travel, schema enforcement, and performance tuning — that make it the foundation for scalable, production-ready data solutions.

The goal is to build a **robust Medallion Architecture** (Bronze → Silver → Gold) where every operation is fully traceable, version-controlled, and optimized for analytics.

---

## 🧩 Key Objectives

1. Understand the **Delta Lake architecture** and how it enables ACID transactions in data lakes.  
2. Learn how to **version and audit data** using time travel and history tracking.  
3. Apply **schema enforcement and evolution** to protect data integrity.  
4. Master **data ingestion, updates, and merges** for incremental processing.  
5. Optimize Delta tables for performance and scalability using compaction techniques.

---

## ⚙️ Section 1: Environment & Storage Setup

Before implementing Delta Lake, the environment is configured in **Azure Databricks** and linked to an **Azure Data Lake Storage Gen2** account.  
Unity Catalog is used to manage metadata, schema, and access permissions, ensuring full data governance.  

Storage layers are organized following the **Medallion Architecture**:
- **Bronze:** Raw ingestion layer  
- **Silver:** Cleaned and validated data  
- **Gold:** Curated and business-ready datasets  

This setup enables a structured, secure foundation for all Delta Lake operations.

---

## 📘 Project Structure (7 Notebooks)

Each notebook focuses on a specific capability of Delta Lake, gradually building from the fundamentals to advanced optimization.

| Notebook | Description |
|-----------|-------------|
| 01. Transaction log | Explore how Delta Lake maintains transactional integrity through its internal log structure. |
| 02. History and Time Travel | Learn to view table history, restore previous versions, and perform data auditing. |
| 03. Create Table – Table & Column Properties | Define Delta tables with metadata, constraints, and table-level properties. |
| 04. Create or Replace & CTAS | Understand the use of create-or-replace logic and how to generate new tables from queries. |
| 05. Insert Overwrite | Manage table updates efficiently by overwriting partitions or entire datasets. |
| 06. Copy Into and Merge Commands | Apply incremental ingestion and upsert logic to synchronize datasets. |
| 07. OPTIMIZE and ZORDER – Compaction | Improve query performance and reduce small file issues through compaction and clustering. |

<img width="1901" height="519" alt="image" src="https://github.com/user-attachments/assets/53959e31-7124-466f-8677-6d1f8c71fc7e" />

---

## 🧱 Notebook Narratives

### 🔹 01. Transaction Log
This notebook introduces the foundation of Delta Lake: the **transaction log**.  
Every change — inserts, updates, or deletes — is recorded as a JSON transaction file.  
By maintaining this log, Delta Lake ensures **ACID compliance**, providing reliability and consistency even during concurrent operations.  
It highlights how Delta tables track changes and maintain data lineage for every commit.

---

### 🔹 02. History and Time Travel
Here, Delta Lake’s **time travel feature** is demonstrated.  
The notebook explores how each Delta table maintains a **version history**, allowing users to query or restore previous states of the data.  
This is crucial for auditing, debugging, and ensuring reproducibility in analytics — enabling teams to “go back in time” and analyze data as it existed at any previous moment.

---

### 🔹 03. Create Table – Table & Column Properties
This section focuses on defining Delta tables with detailed metadata and governance settings.  
It introduces **table and column properties**, such as retention policies and descriptive attributes, helping maintain clarity and compliance across the data estate.  
This notebook emphasizes the value of explicit schema definition and proper metadata documentation in a governed data lake.

---

### 🔹 04. Create or Replace & CTAS
This notebook explains how Delta tables can be created, replaced, or generated directly from existing datasets.  
It demonstrates two critical operations:
- **Create or Replace Table:** updating an existing table structure safely.  
- **CTAS (Create Table As Select):** generating new tables based on query results.  
These methods simplify schema evolution and enable efficient re-creation of datasets in iterative development cycles.

---

### 🔹 05. Insert Overwrite
This part explores the process of **replacing data selectively** within Delta tables without deleting the entire dataset.  
It introduces the concept of **insert overwrite**, which allows updating specific partitions or the full table in a controlled, atomic way.  
This is particularly useful for handling periodic refreshes or reprocessing data while maintaining transactional safety.

---

### 🔹 06. Copy Into and Merge Commands
This notebook focuses on **incremental ingestion and upserts** — two of the most practical use cases for Delta Lake in production environments.  
The **copy into** command is used to load new data efficiently, while the **merge** logic allows existing records to be updated or inserted based on business keys.  
Together, these commands enable **slowly changing dimensions (SCD Type 1)** and maintain synchronized datasets between different systems or layers.

---

### 🔹 07. OPTIMIZE and ZORDER – Compaction
The final notebook deals with **performance optimization** in Delta Lake.  
It demonstrates how to reduce small file problems through **compaction** and improve query performance using **data clustering (ZORDER)**.  
These techniques are essential for scaling analytical workloads, reducing storage costs, and ensuring that queries remain fast even as data grows over time.

---

## 🧠 Learning Outcomes

By completing this project, you will:
- Gain a deep understanding of Delta Lake’s internal architecture and transaction management.  
- Learn how to enforce data integrity with schema control and ACID transactions.  
- Implement reproducible analytics through table history and time travel.  
- Manage incremental updates and merges in a governed, reliable environment.  
- Optimize Delta tables for faster performance and long-term scalability.  

---

## 🧭 Tech Stack

| Component | Description |
|------------|-------------|
| **Azure Databricks** | Cloud platform for Spark-based data engineering |
| **Delta Lake** | Transactional storage layer enabling ACID operations |
| **Azure Data Lake Storage (Gen2)** | Data storage for bronze, silver, and gold layers |
| **Unity Catalog** | Metadata management and data access governance |
| **PySpark** | Data transformation and orchestration engine |

---

## 📊 Architecture Overview

This project follows the **Medallion Architecture**, where data moves through three main layers:
1. **Bronze Layer** – Raw ingestion data, stored in Delta format for reliability  
2. **Silver Layer** – Cleaned and structured data with applied business logic  
3. **Gold Layer** – Curated data ready for reporting, analytics, or machine learning  

The combination of Delta Lake and Unity Catalog ensures traceability, governance, and performance at each stage.

---

## 📚 References
- Azure Databricks Documentation  
- Delta Lake Official Guide  
- Microsoft Learn: Data Engineering on Azure  
- Databricks Blog: Time Travel and Delta Optimization  

---

## 👨‍💻 Author

**Phil Dinh**  



