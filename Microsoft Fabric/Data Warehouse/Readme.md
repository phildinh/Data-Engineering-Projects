# 📦 Microsoft Fabric Data Warehouse Project — DP-700 Hands-On Implementation  
*A full end-to-end project demonstrating data ingestion, modeling, and security in Microsoft Fabric.*

---

## 🚀 Overview

This project is a practical, production-style implementation of two core Microsoft Fabric capabilities:

1. **Loading data into a Microsoft Fabric Data Warehouse using T-SQL**  
2. **Securing a Microsoft Fabric Data Warehouse with enterprise-grade governance**

The project transforms the Microsoft Learn DP-700 labs into a **reusable, portfolio-quality solution** showcasing how Fabric is used for:

- Data ingestion (CSV → Lakehouse → Warehouse)  
- T-SQL transformations  
- Star-schema analytics modeling  
- Data governance and security (DDM, RLS, CLS, permissions)  
- Fabric workspace roles and warehouse protection  

---

## 🧱 Architecture Summary

Raw Data (CSV)
│
▼

Staging Table (T-SQL)
│
▼
Data Warehouse (Star Schema)
├── Dimension Tables
├── Fact Tables
└── Reporting Views
│
▼
Power BI (Optional)


**Security Layer Includes**  
- Workspace roles  
- SQL GRANT/DENY permissions  
- Dynamic Data Masking  
- Row-Level Security (RLS)  
- Column-Level Security (CLS)  

---

## 📂 Repository Structure

/
├── data/
│ └── sales.csv
│
├── sql/
│ ├── 01_Create_Schema_and_Table.sql
│ ├── 02_Create_Store_Procedure_and_Load_data.sql
│ ├── 03_Analytical_queries.sql
│ ├── 04_Create_Table_and_grant_role.sql
│
├── docs/
│ ├── walkthrough.md
│ ├── architecture.md
│ └── security_model.md
│
└── README.md
