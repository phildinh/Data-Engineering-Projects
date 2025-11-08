# ⚡ Apache Spark Structured Streaming – Real-Time Data Ingestion in Azure Databricks  

### Building a Reliable Streaming Pipeline with Auto Loader and Delta Lake  
**Focus:** Real-Time Data Processing, Incremental Ingestion, and Fault-Tolerant Architecture

---

## 🚀 Project Overview

This project demonstrates how to implement **Spark Structured Streaming** in **Azure Databricks** to process real-time data from ingestion to storage using **Delta Lake**.  
It focuses on creating a **streaming pipeline** that reads data continuously from a source folder, applies light transformations, and writes it into Delta tables with full reliability and scalability.

By combining **Auto Loader** and **Delta Lake**, the pipeline supports incremental processing, schema evolution, and automatic file detection — key for modern data engineering in production.

---

## 🧩 Key Objectives

1. Learn how **Structured Streaming** works in Databricks with continuous data ingestion.  
2. Configure **Auto Loader** for incremental file detection and schema inference.  
3. Implement **checkpointing** and **trigger mechanisms** to ensure exactly-once delivery.  
4. Write and maintain **Delta tables** as the storage layer for streaming data.  
5. Build a foundation for real-time dashboards and near-real-time analytics.

---

## ⚙️ Section 1: Environment & Architecture Setup

Before the streaming jobs begin, the Databricks environment is configured and connected to an **Azure Data Lake Storage Gen2** container through **Unity Catalog** for secure governance.  

Data is organized across the three Medallion layers:
- **Bronze:** Raw streaming ingestion layer  
- **Silver:** Cleaned and structured streaming layer  
- **Gold:** Aggregated data for near-real-time reporting  

This layered approach supports scalability, replayability, and auditability.

*(Insert diagram showing: Streaming Source → Bronze → Silver → Gold → BI Dashboard)*

---

## 📘 Project Structure (2 Notebooks for Streaming Ingestion)

| Notebook | Description |
|-----------|-------------|
| 01. Ingest Customers Stream | Demonstrates traditional Structured Streaming ingestion using Spark APIs. |
| 02. Ingest Customers Auto Loader | Enhances the pipeline with Databricks Auto Loader for automatic file detection, schema evolution, and optimized streaming performance. |

---

## 🧱 Notebook Narratives

### 🔹 01. Ingest Customers Stream
This notebook introduces the fundamentals of **Structured Streaming** in Apache Spark.  
It begins by simulating a continuous data feed — typically JSON or CSV customer files arriving in a landing folder.  

The pipeline reads these incoming files as a stream, processes them incrementally, and writes the results into a **Delta table** for persistence.  
Key concepts demonstrated include:
- Streaming DataFrames and incremental micro-batches  
- Trigger intervals for controlling processing cadence  
- Checkpointing to ensure fault tolerance and state recovery  

The notebook provides a clear foundation for understanding real-time ingestion mechanics before introducing automation with Auto Loader.

---

### 🔹 02. Ingest Customers Auto Loader
This notebook upgrades the previous streaming pipeline by integrating **Databricks Auto Loader**, which simplifies and automates data ingestion from cloud storage.  

Instead of manually managing file arrivals, Auto Loader continuously monitors a directory for new files and loads them efficiently into Delta tables.  
It supports **schema inference, schema evolution**, and **incremental processing** out of the box.  

Auto Loader’s scalability allows ingestion of millions of files reliably while minimizing operational overhead — perfect for enterprise-grade streaming workloads.  

Key highlights include:
- Continuous file discovery using cloud notifications  
- Automatic handling of schema drift  
- Fault-tolerant checkpointing and deduplication  
- Seamless integration with the Delta format for downstream analytics  

---

## 🔁 End-to-End Data Flow

1. **Raw Data Arrival** – Customer data lands in a designated ADLS folder.  
2. **Streaming Ingestion (Structured Streaming)** – Spark continuously monitors and reads new data.  
3. **Auto Loader Enhancement** – Detects and processes new files automatically with metadata tracking.  
4. **Checkpointing & Recovery** – Maintains state between runs to guarantee no data loss.  
5. **Delta Lake Storage** – Stores curated results with full transactional consistency.  
6. **Real-Time Access** – BI tools or analytics notebooks can query up-to-date data instantly.  

---

## 🧠 Learning Outcomes

After completing this project, you will be able to:
- Build a **real-time data ingestion pipeline** using Spark Structured Streaming.  
- Implement **Databricks Auto Loader** for incremental and scalable ingestion.  
- Manage **stream state** with checkpointing and fault recovery.  
- Use **Delta Lake** as a reliable sink for streaming data.  
- Enable real-time analytics and dashboards with continuously updating data.

---

## 🧭 Tech Stack

| Component | Purpose |
|------------|----------|
| **Azure Databricks** | Streaming computation engine using Apache Spark |
| **Structured Streaming** | Framework for incremental data processing |
| **Auto Loader** | Simplified and scalable ingestion mechanism |
| **Delta Lake** | Reliable storage format ensuring ACID transactions |
| **Azure Data Lake Storage (Gen2)** | Landing and storage layer for streaming data |
| **Unity Catalog** | Centralized governance and schema management |

---

## 📊 Architecture Overview

This streaming project follows a **Medallion-based real-time architecture**:
- **Bronze:** Raw incoming data captured continuously  
- **Silver:** Processed, cleaned streaming data with transformations applied  
- **Gold:** Aggregated data ready for visualization or real-time monitoring  

By leveraging Auto Loader with Delta Lake, each layer benefits from incremental updates and guaranteed consistency, ensuring continuous insight delivery.

---

## 📚 References
- Databricks Structured Streaming Guide  
- Databricks Auto Loader Documentation  
- Delta Lake Best Practices for Streaming  
- Microsoft Learn: Real-Time Analytics on Azure Databricks  

---

## 👨‍💻 Author

**Phil Dinh**  



