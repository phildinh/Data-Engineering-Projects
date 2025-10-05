# 🚀 Azure Project — Pull Dataset via APIs with Azure Data Factory, Store in Data Lake (Bronze/Silver/Gold), Transform with Databricks, and Visualize in Power BI

This project showcases how to build a modern data pipeline in Microsoft Azure using multiple integrated services — **Data Factory**, **Databricks**, **Synapse Analytics**, and **Power BI** — following the **Medallion architecture** (Bronze, Silver, Gold).

The pipeline pulls raw data via **APIs**, stores it in **Azure Data Lake Storage (ADLS Gen2)**, transforms it with **Databricks (PySpark)**, then loads curated data into **Synapse Analytics** for reporting through **Power BI**.

<img width="1790" height="1003" alt="image" src="https://github.com/user-attachments/assets/7a79b56b-bbb0-4dad-9a3d-099d2a93ff5c" />

---

## 🧱 Create Environment for the Project

We begin by creating all required Azure resources:
- **Resource Group**
- **Storage Account** (ADLS Gen2)
- **Azure Data Factory**
- **Azure Databricks**
- **Synapse Analytics**

Access permissions are configured using **Microsoft Entra ID** to ensure secure connections between services.  
This setup allows **Azure Factory** and **Synapse Analytics** to access the Data Lake seamlessly.

<img width="1890" height="643" alt="image" src="https://github.com/user-attachments/assets/4965f7f0-8023-4414-b42c-bec07328f01b" />

---

## 🏗️ Creating Pipeline in Data Factory to Pull Data from GitHub

The data pipeline in **Azure Data Factory** dynamically retrieves multiple CSV files from GitHub using API endpoints.

- A **JSON configuration file** is used to store all HTTP links.  
- The pipeline reads this file from the Data Lake, loops through each URL, and downloads each dataset into the **Bronze layer**.  
- This enables easy scalability and automation for handling multiple data sources.

<img width="966" height="698" alt="image" src="https://github.com/user-attachments/assets/82050fbf-da90-4599-a144-9047a4ac6247" />

The **ForEach** activity iterates through each HTTP link and copies the corresponding CSV files to the **Bronze folder** within the Data Lake.

<img width="660" height="289" alt="image" src="https://github.com/user-attachments/assets/2cb99a2c-a885-406d-8d14-6039a16160c2" />

---

## ⚙️ Using Databricks to Transform Data and Store into Silver Layer

Once raw data is stored in the Bronze layer, **Azure Databricks** is used to process and transform it.

- Create access for Databricks using **Microsoft Entra ID** (Service Principal).  
- Set up a **compute cluster** to allocate worker nodes for data transformation.  
- Use **PySpark notebooks** to clean, normalize, and enrich data, then write outputs into the **Silver layer**.

<img width="1869" height="771" alt="image" src="https://github.com/user-attachments/assets/7cae3d02-c585-49b9-8482-828efd7917a0" />

Example tasks include:
- Handling null or inconsistent values  
- Normalizing column structures  
- Enforcing schema and partitioning  
- Writing transformed datasets in **Delta format** to maintain version control and ACID compliance  

---

## 🏛️ Using Synapse Analytics for the Gold Layer and Power BI Integration

The **Gold layer** is implemented in **Synapse Analytics**, where cleaned and modeled data is made available as **SQL Views** for reporting.

- Create an **SQL Database** in Synapse Analytics.  
- Build **Views** from the Silver layer to represent key business metrics and aggregated insights.  
- These views act as the **Gold layer**, optimized for analytics and Power BI consumption.

<img width="1430" height="702" alt="image" src="https://github.com/user-attachments/assets/34828276-cb49-4325-a6ab-f9ecb7380611" />

Finally, connect **Power BI** directly to Synapse Analytics to visualize and monitor KPIs such as sales performance, product mix, and customer behavior.

<img width="1351" height="736" alt="image" src="https://github.com/user-attachments/assets/8d431e37-4eff-43da-9898-1fe5b81022c8" />

---

## ✅ Summary

This project demonstrates an end-to-end Azure data engineering solution:
- **Data ingestion** via Azure Data Factory (HTTP APIs → Bronze)
- **Data transformation** using Databricks (Bronze → Silver)
- **Data modeling and serving** via Synapse Analytics (Silver → Gold)
- **Reporting and visualization** using Power BI

Following the **Bronze → Silver → Gold** methodology ensures data quality, scalability, and reliability across the pipeline.
