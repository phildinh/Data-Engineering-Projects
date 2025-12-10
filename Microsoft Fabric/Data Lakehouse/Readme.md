
# 🏗️ Microsoft Fabric Lakehouse Project  
## End-to-End Medallion Architecture with Apache Spark, Delta Lake, and Power BI Direct Lake  
### *A professional data engineering implementation using Microsoft Fabric*

---

## 📌 Project Overview

This project demonstrates a complete, production-style **data lakehouse architecture** built on **Microsoft Fabric**, following best practices used by enterprise data engineering teams.

The solution implements a full **Medallion Architecture (Bronze → Silver → Gold)** using:

- Microsoft Fabric **Lakehouse**  
- **Apache Spark** notebooks  
- **Delta Lake** table storage  
- Semantic modeling for **Power BI Direct Lake**  
- A clean, reusable workflow designed for scalability  

All transformations, optimizations, and table creation steps are orchestrated through **Fabric Notebooks**, enabling efficient and governed data engineering within the Fabric ecosystem.

---

## 📂 Lakehouse Structure & Raw Data (Bronze)

<img width="1916" height="1026" alt="image" src="https://github.com/user-attachments/assets/779fa8ef-f753-4d1c-b9f4-1c72650503de" />

The **Bronze layer** holds the raw, unmodified data exactly as received.  
In this project, three yearly sales extracts (`2019.csv`, `2020.csv`, `2021.csv`) were uploaded to:


This layer acts as the immutable data source, supporting reproducibility and auditability.

---

## ⚙️ Data Processing with Spark Notebooks (Silver)

This stage performs the core data engineering work. A dedicated **Spark notebook** (included in this repository) handles:

- Loading raw CSV files from the Bronze layer  
- Normalizing and validating field types  
- Cleaning missing or inconsistent values  
- Standardizing schema across years  
- Writing curated Delta tables into the **Silver layer**

The Silver layer represents **clean, structured, analytics-ready datasets** that preserve fidelity but eliminate raw-data irregularities.

> *(Insert screenshot of the transformed Silver Delta tables here)*  
> **IMAGE PLACEHOLDER**

The Jupyter notebook in this repository documents each step in detail, ensuring full transparency of the transformation logic.

---

## 🥇 Business-Ready Gold Layer (Dimensional Model)

The **Gold layer** refines Silver tables into a fully optimized **dimensional star schema**, ready for semantic modeling and BI consumption.

The Gold model includes:

### ⭐ Dimension Tables  
- `dimcustomer_gold`  
- `dimproduct_gold`  
- `dimdate_gold`  

### ⭐ Fact Table  
- `factsales_gold`  

Key characteristics of the Gold layer:

- Conforms to Kimball dimensional modeling principles  
- Supports high-performance BI queries  
- Enables rich time intelligence and analytical reporting  
- Stored as **Delta tables** for reliability and ACID capabilities  

<img width="1912" height="1030" alt="image" src="https://github.com/user-attachments/assets/cdd56afe-df87-4f53-a567-a22e44e832d7" />

This structure reflects real-world enterprise modeling patterns used by data engineering teams to support scalable and governed analytics.

---

## 🔗 Power BI Semantic Model (Direct Lake)

The Gold tables are surfaced directly to Power BI using **Direct Lake**, providing:

- Sub-second query performance  
- No import refresh required  
- Automatic reflection of Lakehouse changes  
- Simplified governance and reuse  

The resulting semantic model forms a clean, intuitive star schema:

<img width="1915" height="992" alt="image" src="https://github.com/user-attachments/assets/ba526f72-1d2f-4c0d-b81b-7d69fbc3416d" />

This schema supports analysis along customer, product, and date dimensions, making the dataset immediately usable for downstream analytics.

---

## 🧱 End-to-End Architecture Summary

Bronze → Raw files stored in Lakehouse (CSV)
Silver → Cleaned, typed, structured Delta tables (Spark)
Gold → Dimensional business model (Delta)
Power BI → Direct Lake semantic model for analytics


This implementation adheres to modern lakehouse engineering standards, leveraging Fabric-native capabilities to deliver a unified analytics experience.

---

## 🎯 Project Goals

This project demonstrates practical expertise in:

- Designing and implementing Medallion Architecture  
- Building Spark-based data pipelines in Fabric  
- Structuring data using Delta Lake  
- Applying dimensional modeling techniques  
- Delivering analytics-ready datasets through Direct Lake  
- Operating within Microsoft Fabric’s unified data engineering ecosystem  

It serves as both a **portfolio project** and a **reusable learning asset** for professionals preparing for advanced Fabric engineering roles or certifications such as **DP-700**.

---

## 📁 Included Artifacts

- Full **Spark notebook** for Bronze → Silver → Gold transformations  
- Documentation for each transformation stage  
- Relationship diagrams and model screenshots  
- Clean repo structure following engineering best practices  

---

## 🚀 Future Enhancements (Optional)

Potential extensions include:

- Incremental ingestion using merge logic  
- Data quality checks and expectations frameworks  
- Additional fact/ dimension modeling  
- Databricks-style optimization techniques (Z-Order, partitioning)  
- Pipeline automation via Fabric Data Factory  
- Security implementation (RLS, masking, permissions)  

---

## ✔️ Summary

This project demonstrates the full lifecycle of building a modern, enterprise-grade data lakehouse in **Microsoft Fabric**, applying Spark, Delta, and Power BI in a cohesive and scalable architecture.

It mirrors the workflows used by professional data engineers and showcases practical experience with the Fabric platform.

```markdown
<<< END OF FILE >>>
