








# 🚀 Azure Databricks Job Orchestration – Process Company Data

This project demonstrates an automated **ETL workflow** in **Azure Databricks** following the **Medallion Architecture (Bronze → Silver → Gold)**.  
The pipeline reads a CSV file from **Azure Data Lake Storage (ADLS)**, processes it through three layers, and sends an **email notification** upon successful completion.

---

## 🧱 Architecture Overview  

The workflow is defined as a Databricks Job named **`process_company_data`**, containing three sequential tasks:
1. **bronze_companies** – Ingest raw data from ADLS.  
2. **silver_companies** – Clean and standardize the data.  
3. **gold_company_summary** – Aggregate metrics for analytics.

All tasks run automatically when a new file appears in the storage container.

> 🖼️ **Figure 1 – Job Architecture**  
<img width="1873" height="900" alt="image" src="https://github.com/user-attachments/assets/7ba1f70d-7d7a-4476-a108-8e58907dfe6e" />

---

## ⚙️ Job Orchestration & Data Lineage  

The workflow orchestrates three notebooks connected through dependencies.  
Databricks **Unity Catalog** automatically tracks lineage between layers for full visibility.

**Data flow:**
- **Input:** `top_tech_companies.csv` from ADLS  
- **Bronze Table:** `bronze.companies`  
- **Silver Table:** `silver.companies`  
- **Gold Table:** `gold.company_summary`

> 🖼️ **Figure 2 – Data Lineage in Job Run**  
<img width="1638" height="856" alt="image" src="https://github.com/user-attachments/assets/aac6b9b3-e1a6-4787-a8b8-560dbf921823" />

---

## ⏱️ Automated Trigger  

The job is configured with a **File Arrival Trigger** at:  
`abfss://demo@philproject1.dfs.core.windows.net/landing/companies/`  

Whenever a new file is uploaded, Databricks automatically starts the ETL process without manual intervention.

> 🖼️ **Figure 3 – Job Runs and Trigger Setup**  
<img width="1647" height="876" alt="image" src="https://github.com/user-attachments/assets/ef577208-1ab0-4716-abec-93a499924692" />

---

## 📧 Email Notification  

After each successful job run, Azure sends an automatic **success email** summarizing:
- Workspace  
- Job name and ID  
- Duration  
- Trigger type (Manual / File Arrival)  
- Run status  

> 🖼️ **Figure 4 – Success Email Notification**  
<img width="1527" height="698" alt="image" src="https://github.com/user-attachments/assets/e75ba34d-dd63-4d5a-9e75-4f2542f63113" />

---

## ✅ Project Outcome  

This project delivers a fully automated, production-style Databricks workflow that:
- Processes new data automatically via **file event triggers**  
- Tracks complete **data lineage** with Unity Catalog  
- Provides **email alerts** for monitoring  
- Follows the **Bronze → Silver → Gold** data architecture  

The final `gold.company_summary` table is now ready for integration with Power BI or Microsoft Fabric for real-time analytics.

---
