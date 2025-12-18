# Spark Structured Streaming – End-to-End Streaming Fundamentals

## 📌 Project Overview

This project demonstrates **core Spark Structured Streaming concepts** using a hands-on, file-based streaming approach.  
Instead of relying on managed frameworks (e.g. DLT), the pipeline is built using **native Spark Structured Streaming APIs**, exposing how streaming works at a lower level.

The project simulates **real-time weather sensor data**, ingested from files written continuously into an Azure Databricks **Volume**, and progressively explores streaming concepts such as:
- File-based streaming sources
- Auto Loader
- Micro-batch behavior
- Schema inference and evolution
- Event-time processing and watermarking
- Trigger intervals
- Streaming reads and writes with Delta Lake

This project is designed as a **learning-focused but production-relevant streaming walkthrough**, mirroring how engineers build intuition before adopting higher-level abstractions.

---

## 🧱 High-Level Architecture

- **Compute**: Apache Spark (Structured Streaming on Azure Databricks)
- **Storage**: Azure Data Lake Storage Gen2 (via Volumes)
- **Table Format**: Delta Lake
- **Ingestion Pattern**: File-based streaming (append-only)
- **Processing Model**: Micro-batch Structured Streaming
- **Governance**: Unity Catalog (Catalogs, Schemas, Volumes)
- **Architecture Pattern**: Streaming Bronze → Silver-style processing
- **Execution Mode**: Continuous file arrival with trigger-based execution

---

## 🗂️ Project Structure & Learning Flow

The project is organized into **progressive sections**, each introducing a new Structured Streaming concept:

01. Streaming Simulator Notebook
02. Reading Streams with Auto Loader
03. Micro-batch Size
04. Schema Inference and Evolution
05. Time-Based Aggregations and Watermarking
06. Writing Streams
07. Trigger Intervals
08. Delta Table Streaming Reads and Writes


Each section builds on the previous one, reinforcing both **theory and execution behavior**.

---

## Section 1 — Streaming Data Simulation

The pipeline begins with a **custom streaming data simulator** that continuously generates weather readings.

Key characteristics of the simulated stream:
- One weather event written every few seconds
- Each event stored as a single CSV file
- Files appended to a governed **Unity Catalog Volume**
- Events include timestamps, city, temperature, humidity, and wind speed

This approach mirrors:
- IoT devices writing files to cloud storage
- Log-based systems emitting incremental data
- External systems pushing data asynchronously

The goal is to create a **realistic file-based streaming source** for Spark to consume.

---

## Section 2 — Reading Streams with Auto Loader

Spark Structured Streaming is used to **continuously monitor the source directory** and ingest new files as they arrive.

Auto Loader concepts explored:
- Incremental file discovery
- Exactly-once processing guarantees
- Scalable ingestion without directory listing bottlenecks

This demonstrates how Spark handles **streaming file ingestion reliably**, even when files arrive out of order or at irregular intervals.

---

## Section 3 — Micro-batch Processing Behavior

This section focuses on how Spark processes streaming data in **micro-batches**.

Key learning points:
- How batch size is determined
- Relationship between file arrival rate and batch execution
- Trade-offs between latency and throughput
- Impact of small files on batch frequency

Understanding micro-batches is critical for reasoning about **streaming performance and resource usage**.

---

## Section 4 — Schema Inference and Evolution

The pipeline explores how Spark:
- Infers schema from incoming files
- Handles consistent vs changing schemas
- Reacts to new or missing columns

This section highlights:
- Why schema control matters in streaming
- Risks of uncontrolled schema evolution
- Best practices for long-running streaming jobs

---

## Section 5 — Time-Based Aggregations and Watermarking

This section introduces **event-time processing**, a core streaming concept.

Topics covered:
- Event-time vs processing-time
- Window-based aggregations (e.g. tumbling windows)
- Watermarking to handle late-arriving data
- Bounding state to prevent unbounded memory growth

This mirrors real-world use cases such as:
- Time-based metrics
- Rolling averages
- Monitoring and alerting systems

---

## Section 6 — Writing Streaming Outputs

Processed streaming data is written to downstream sinks, demonstrating:
- Append vs complete output modes
- Checkpointing for fault tolerance
- Idempotent writes using Delta Lake

This reinforces how Spark maintains **exactly-once guarantees** even across restarts.

---

## Section 7 — Trigger Intervals

This section explores **trigger configuration**, including:
- Default (as-fast-as-possible) triggers
- Fixed processing intervals
- Trade-offs between latency and cost

Understanding triggers is essential for aligning streaming jobs with **business SLAs** and infrastructure constraints.

---

## Section 8 — Delta Table Streaming Reads and Writes

The final section demonstrates:
- Streaming writes to Delta tables
- Streaming reads from Delta tables
- Using Delta as both a streaming sink and source

This closes the loop by showing how **Delta Lake enables composable streaming pipelines**, where one stream feeds another.

---

## ⚡ Performance & Design Considerations

- File-based streaming highlights the **small-file problem**
- Auto Loader reduces ingestion overhead
- Event-time + watermarking prevents unbounded state
- Trigger tuning balances freshness vs cost
- Delta Lake provides reliability and consistency

Rather than optimizing prematurely, this project focuses on **understanding behavior first**, which is essential before tuning production workloads.

---

## 🧠 Why This Project Matters

This project demonstrates:
- Strong fundamentals in Spark Structured Streaming
- Clear understanding of streaming internals
- Ability to reason about latency, state, and fault tolerance
- A solid foundation before adopting higher-level tools like DLT

It complements managed pipeline projects by showing **what happens under the hood**.

---

## ✅ Key Outcomes

- End-to-end streaming pipeline using native Spark APIs
- Realistic file-based streaming ingestion
- Hands-on exposure to event-time processing
- Clear understanding of micro-batch execution
- Practical streaming design intuition

This project forms a **core building block** for advanced streaming architectures.

