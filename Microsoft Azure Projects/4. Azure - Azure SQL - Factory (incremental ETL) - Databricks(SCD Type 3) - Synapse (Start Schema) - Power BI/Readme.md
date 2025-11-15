# 🚀 Azure Project — Building an Incremental ETL Pipeline from Azure SQL Database to Synapse Analytics with Data Lake and Databricks

This project demonstrates how to build a complete **ETL pipeline** within the **Microsoft Azure ecosystem**, starting from **Azure SQL Database (DBMS)** and following the **Medallion Architecture (Bronze → Silver → Gold)**.

It showcases how to implement **incremental loading**, transform data using **Databricks (PySpark)**, and store curated data in **Azure Synapse Analytics (Data Warehouse)** — ready for **Power BI visualization**.

<img width="1892" height="1069" alt="image" src="https://github.com/user-attachments/assets/cd0cb6b1-ba8d-4b97-b7ca-506d8069a330" />

---

## 🧱 Create Environment

We begin by creating all required Azure resources for the ETL workflow:

- **Resource Group**
- **Storage Account (Data Lake Gen2)**
- **Azure SQL Database (Source)**
- **Azure Data Factory (Pipeline Orchestration)**
- **Azure Databricks (Transformation Layer)**
- **Azure Synapse Analytics (Data Warehouse)**

Access permissions are configured using **Microsoft Entra ID** to ensure secure and seamless connections between services.  
This setup allows **Azure Factory**, **Databricks**, **Azure SQL Database**, and **Synapse Analytics** to interact with the **Data Lake** under a unified identity framework.

<img width="1609" height="711" alt="image" src="https://github.com/user-attachments/assets/895e147d-33a4-428a-9496-f8ab60e482c1" />

---

## 🏗️ Creating the Pipeline to Pull Data from Azure SQL Database and Load into Data Lake

The first step is to extract data from the **Azure SQL Database (DBMS)** and land it in the **Bronze layer** within **Azure Data Lake**.

- Create tables in Azure SQL Database for testing incremental loading.
- Use **timestamps or primary keys** to define change tracking for incremental extracts.
- Configure **Linked Services** for SQL Database and Data Lake.

<img width="1892" height="854" alt="image" src="https://github.com/user-attachments/assets/259f0102-33dd-454f-8b3e-2e12f5f703f9" />

### 🔁 Incremental Load Pipeline in Azure Data Factory

- Build a pipeline using **Lookup** and **Copy Data** activities.
- Configure the **source query** to fetch only new or updated records since the last run.
- Store extracted data in the **Bronze layer** of the Data Lake in **Parquet format** for efficient storage and querying.

<img width="1663" height="831" alt="image" src="https://github.com/user-attachments/assets/9475efbd-78ff-4a38-9e50-f18d83ba2f8c" />

This incremental approach ensures efficient data refreshes, minimizes pipeline runtime, and keeps the Data Lake synchronized with source system changes.

---

## ⚙️ Transforming and Processing Data with Databricks

Once raw data lands in the **Bronze layer**, it is transformed and cleaned using **Azure Databricks**.

Steps include:
- Granting Databricks access via **Microsoft Entra ID** (Service Principal).  
- Creating a **compute cluster** to process data in parallel.  
- Developing **PySpark notebooks** to transform, standardize, and validate data.  
- Writing cleaned outputs into the **Silver layer** using **Delta format** for ACID reliability.

<img width="1844" height="892" alt="image" src="https://github.com/user-attachments/assets/0690555c-5f64-42f5-bd6d-5bd9d2f3306c" />

In this step, we also begin designing a **Star Schema model**, preparing dimension and fact tables to be loaded into the Gold layer later in Synapse Analytics.

---

## 🏛️ Using Synapse Analytics for the Gold Layer and Power BI Integration

The **Gold layer** is implemented in **Azure Synapse Analytics**, where business-ready data is modeled and served for analysis.

- Create an **SQL Pool or Serverless Database** in Synapse Analytics.  
- Build **Views or external tables** on top of Silver data stored in the Data Lake.  
- Define **fact and dimension tables** to complete the **Star Schema** design.

<img width="475" height="650" alt="image" src="https://github.com/user-attachments/assets/9d3e4603-6fc1-4fe4-949c-5a281be00387" />

Finally, connect **Power BI** directly to **Synapse Analytics** to visualize business KPIs such as sales trends, performance metrics, and product mix.

<img width="608" height="724" alt="image" src="https://github.com/user-attachments/assets/fe03646d-025a-483d-9214-c6ecc532a048" />

---

## ✅ Summary

This project demonstrates a complete **end-to-end ETL pipeline** using Microsoft Azure services:
- **Azure Data Factory** for incremental ingestion  
- **Azure Data Lake (Bronze/Silver layers)** for raw and refined data storage  
- **Azure Databricks** for transformation and data quality processing  
- **Azure Synapse Analytics (Gold layer)** for analytical modeling  
- **Power BI** for visualization and business insights  

By following the **Medallion Architecture** and leveraging **incremental loading**, this pipeline efficiently processes data from source to insights — ensuring scalability, reliability, and analytical readiness.
