# Bridge Monitoring – Lakeflow Declarative Pipeline (DLT)

## 📌 Project Overview

This project demonstrates a **real-time streaming analytics pipeline** built using **Databricks Lakeflow Declarative Pipelines (DLT)**.  
It simulates IoT sensor data from multiple bridges and processes it end-to-end using a **Bronze → Silver → Gold** streaming architecture.

The solution focuses on:
- Declarative data pipelines
- Streaming ingestion and processing
- Data quality enforcement
- Event-time windowed aggregations
- Automated dependency management and orchestration

This project is designed to reflect **production-grade streaming data engineering**.

---

## 🧱 High-Level Architecture

- **Compute**: Azure Databricks (DLT Pipeline)
- **Storage**: Azure Data Lake Storage Gen2 (via Volumes)
- **Table Format**: Delta Lake
- **Governance**: Unity Catalog (Catalogs, Schemas, Volumes)
- **Ingestion Pattern**: Streaming (Delta → Delta)
- **Processing Model**: Lakeflow Declarative Pipeline
- **Architecture Pattern**: Medallion (Bronze → Silver → Gold)
- **Data Quality**: DLT Expectations
- **Orchestration**: Managed by DLT (no manual job wiring)

---

## 🗂️ Data Model & Medallion Layers
<img width="460" height="436" alt="image" src="https://github.com/user-attachments/assets/50cd5d42-e5b5-4cb8-ad61-50d1bdc7d57e" />


---

## Section 1 — Landing Layer (00_landing)

### Streaming Data Simulation

A Python-based **data generator** simulates real IoT sensors for multiple bridges:

- Temperature
- Vibration
- Tilt angle

Key characteristics:
- Multiple devices emitting events every minute
- Randomized event-time latency (out-of-order events)
- Continuous Delta writes into Unity Catalog volumes

This simulates **real-world streaming challenges** such as late-arriving data and uneven arrival times.

<img width="303" height="388" alt="image" src="https://github.com/user-attachments/assets/e91d5f12-ede3-4289-9f0e-9047ba327f20" />


---

## Section 2 — Bronze Layer (01_bronze)

### Raw Streaming Ingestion

The Bronze layer ingests raw Delta streams from the landing volumes using **Spark Structured Streaming**.

Characteristics:
- Schema-on-read
- No transformations applied
- One-to-one mapping with source streams
- Preserves original event_time for downstream processing

This layer acts as the **system of record** for streaming ingestion.

---

## Section 3 — Silver Layer (02_silver)

### Static Metadata Table

A static Silver table (`bridge_metadata`) provides contextual information for each bridge, including:
- Name
- Location
- Structural attributes
- Opening year

This table is used to enrich all streaming sensor data.

---

### Streaming Enrichment & Data Quality

Each streaming dataset (temperature, vibration, tilt) is:
- Cast to proper event-time timestamps
- Enriched via joins with bridge metadata
- Validated using **DLT expectations**, such as:
  - Non-null event_time
  - Valid value ranges per sensor type

Invalid records are automatically **dropped or flagged**, ensuring data quality is enforced declaratively.

---

## Section 4 — Gold Layer (03_gold)

### Windowed Streaming Aggregations

The Gold layer computes **10-minute windowed metrics per bridge**, including:
- Average temperature
- Maximum vibration
- Maximum tilt angle

Key streaming concepts applied:
- Event-time processing
- Watermarking to bound late data
- Stateful windowed aggregations
- Stream-to-stream joins across multiple Silver tables

The result is an analytics-ready, continuously updated metrics table suitable for dashboards, alerts, or downstream systems.

---

## Section 5 — Lakeflow Declarative Pipeline Execution

### Declarative Pipeline Benefits

This pipeline leverages Lakeflow DLT features:
- Automatic dependency resolution
- Managed execution order
- Built-in lineage visualization
- Centralized monitoring and metrics
- Simplified orchestration (no manual job wiring)

The pipeline graph clearly shows:
- Fan-in from multiple Bronze streams
- Enrichment and validation in Silver
- Aggregation and consolidation in Gold

Failures, retries, and partial refreshes are handled natively by the DLT framework.
<img width="1906" height="1027" alt="image" src="https://github.com/user-attachments/assets/554d61ae-1c4f-4b62-8f54-f9f57a7ac237" />


---

## ⚡ Performance & Streaming Considerations

- **Event-time processing** with watermarks prevents unbounded state growth
- **Small dimension tables** enable efficient broadcast joins
- **Declarative pipeline design** allows Databricks to optimize execution plans
- **Separation of concerns** across Medallion layers improves maintainability
- Streaming state is bounded and scalable by design

---

## ✅ Key Outcomes

- End-to-end **real-time Lakehouse pipeline**
- Declarative streaming ETL using Lakeflow
- Built-in data quality enforcement
- Event-time windowed analytics
- Clear lineage and operational visibility

---

## 🧠 Why This Project Matters

This project demonstrates:
- Streaming fundamentals beyond batch ETL
- Practical use of Databricks DLT in production-style pipelines
- Strong understanding of event-time processing and data quality
- Ability to design scalable, maintainable streaming architectures

It complements batch-oriented Lakehouse projects and shows versatility across **both batch and streaming data engineering**.


