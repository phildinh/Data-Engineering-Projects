# 🧱 Datamodeling - Medallion Architecture (Bronze → Silver → Gold)  
### Incremental Load & SCD Type 1 Implementation

This project focuses on **data modeling**, one of the core concepts in **Data Engineering**, designed to ensure clean, structured, and efficient data transformation across layers.  
It demonstrates how raw data evolves into analytical-ready datasets through **Medallion Architecture** (Bronze, Silver, Gold) using **Databricks** notebooks.

---

## ⚙️ Environment Setup

The project is developed entirely within the **Databricks environment**, following a structured setup:

1. **Create Databricks Account (Workspace Environment)**  
2. **Setup Catalog** → used for data governance and organization.  
3. **Create Schema Layers** → `source`, `bronze`, `silver`, `gold`, and `scd`.  
4. **Create Folder** to hold all notebooks.  
5. **Execute notebooks** step by step to simulate the full data flow pipeline.
<img width="1800" height="910" alt="image" src="https://github.com/user-attachments/assets/3c4548ff-106f-4b19-8324-b80ea1797c84" />

---

## 📂 Project Structure

📁 Datamodeling/
├── source.py
├── bronze.py
├── silver.py
├── gold.py
├── SCD.py


---

## 🧩 Workflow Overview

### 1️⃣ Source Layer – `source.py`
- Defines **source tables** and inserts initial values.  
- Simulates **raw incoming data** before transformation.  
- Acts as the foundation for incremental loading.

---

### 2️⃣ Bronze Layer – `bronze.py`
- Creates a **view filtered by date**, following an **incremental load** pattern from the source table.  
- Inserts filtered data into the **bronze table**, maintaining history of ingestion events.

---

### 3️⃣ Silver Layer – `silver.py`
- Uses **MERGE statements** to update existing records from the bronze layer.  
- Performs **deduplication** and **data cleansing**.  
- Silver table accumulates data **incrementally**, representing the refined version of the source.

---

### 4️⃣ Gold Layer – `gold.py`
- Transforms the silver data into a **Star Schema model**.  
- Splits data into **Dimension (Dim)** and **Fact** tables for analytical purposes.  
- Supports downstream BI tools (Power BI, Tableau, etc.) with well-modeled entities.

---

### 5️⃣ Slowly Changing Dimension (SCD) – `SCD.py`
- Demonstrates **SCD Type 1 and Type 2** implementation logic using SQL and PySpark syntax.  
- Type 1 → Overwrites existing records with new data.  
- Type 2 → Keeps historical records by tracking changes with `effective_date` and `end_date` columns.

---

## 🧠 Key Concepts Demonstrated

- Databricks **Medallion Architecture**
- **Incremental Data Load**
- **Merge Logic** (Upsert using Delta Lake)
- **Star Schema Modeling**
- **SCD Type 1 & 2** with Delta Table versioning


---

## 🚀 Highlights

- Each notebook is modular, simulating a **real-world data pipeline**.  
- The project demonstrates **both technical and architectural understanding** of data engineering workflows.  
- Ideal for **portfolio showcase** or **YouTube tutorial series** to explain Databricks data modeling best practices.

---

**Author:** Phil Dinh  
**Platform:** Databricks • Delta Lake • PySpark • Medallion Architecture  
**Focus:** Data Modeling, Incremental Load, SCD Type 1 & 2
