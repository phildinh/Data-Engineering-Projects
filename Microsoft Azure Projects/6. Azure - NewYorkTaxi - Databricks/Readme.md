# New York City Taxi Analytics  
## Azure Databricks Lakehouse | Medallion Architecture | Incremental Load | SCD Type 2 | Job Orchestration | Performance Considerations | Granting Access for Data Analysts at the Gold Layer 

---

## 📌 Project Overview

This project demonstrates a **production-style Lakehouse data engineering solution** built on **Azure Databricks** using **Azure Data Lake Storage Gen2 (ADLS Gen2)** as the primary storage layer.  
It is designed to reflect **real-world enterprise data engineering practices**, including environment setup, governance, version control, batch ingestion, incremental processing, Slowly Changing Dimensions (SCD Type 2), and scheduled orchestration.

The pipeline processes **New York City Yellow Taxi trip data**, supporting:
- **Initial historical backfill**
- **Incremental monthly ingestion**
- **Bronze → Silver → Gold transformations**
- **Delta Lake ACID guarantees**
- **Data sharing to external stakeholders via a separate ADLS Gen2 location**

This repository is intentionally structured and narrated to be **portfolio-ready**, suitable for **Data Engineer / Analytics Engineer roles** using Databricks and Azure.

---

## 🧱 High-Level Architecture

- **Compute**: Azure Databricks (Serverless & Job clusters)
- **Storage**: Azure Data Lake Storage Gen2
- **Table Format**: Delta Lake
- **Governance**: Unity Catalog (Metastore, Catalogs, Schemas, Volumes)
- **Ingestion**: HTTPS pull directly from public NYC Taxi endpoints
- **Processing Pattern**: Medallion Architecture
- **Orchestration**: Databricks Jobs
- **Version Control**: GitHub + Databricks Repos
- **Collaboration Model**: Feature branches + Pull Requests
- **Granting Access**: Data Governance + Role Based access

---

## ⚡Performance Considerations
- **Partition-aware data layout** for large fact and export tables
- **Delta Lake optimization awareness** to manage file sizes as data grows
- **Join strategy design** that enables efficient Spark execution
- **Compute elasticity** using Serverless workloads for burst processing
---

## 🥉🥈🥇 Medallion Architecture Design

| Layer | Purpose | Storage Format |
|-----|-------|----------------|
| **00_landing** | Raw files pulled from external HTTP sources | Parquet (Volumes) |
| **01_bronze** | Raw structured data, schema-on-read | Delta |
| **02_silver** | Cleaned, enriched, conformed datasets | Delta |
| **03_gold** | Aggregated, analytics-ready tables | Delta |
| **04_export** | External tables for stakeholder delivery | External Delta |

All Bronze → Gold tables are stored as **managed Delta tables**, ensuring:
- ACID transactions
- Time travel
- Schema enforcement
- Scalable incremental processing

---

## 🎯 Project Objectives

- Provision a **secure Azure + Databricks environment** following best practices
- Implement a **Unity Catalog–governed Lakehouse**
- Design a **Medallion Architecture** using Delta Lake
- Perform **initial historical backfill** via HTTPS ingestion
- Implement **incremental monthly loads**
- Apply **SCD Type 2** for dimensional history tracking
- Orchestrate pipelines using **Databricks Jobs**
- Deliver curated datasets to **external stakeholder storage**

---

## 📂 Repository Structure
<img width="293" height="322" alt="image" src="https://github.com/user-attachments/assets/4071b194-3e13-41a6-a598-29da327ac6bf" />


## 📑 Table of Contents & Execution Flow

1. Create Environment  
2. Initial Load (Historical Backfill)  
3. External Stakeholder Data Export  
4. Incremental Load & Orchestration  
5. Data Validation & Quality Checks
6. Performance & Scalability Considerations
7. Granting Access for Data Analysts
---

### **Section 1 — Environment & Governance Setup**
*Foundation for a secure, scalable Lakehouse*

This section focuses on preparing the Azure + Databricks environment before any data is ingested.

1. **Azure Resource Provisioning**
   - Create Resource Group
   - Provision ADLS Gen2 storage
   - Deploy Azure Databricks workspace
   - Configure Databricks Access Connector for secure identity-based access
  <img width="1902" height="906" alt="01  Create resouces in azure" src="https://github.com/user-attachments/assets/9ffd739e-9193-4d78-b4bd-e47f31ad819c" />


2. **Unity Catalog & Metastore Configuration**
   - Create Databricks Metastore
   - Attach Metastore to ADLS Gen2 metadata location
   - Assign workspace to Metastore
   - Establish centralized governance for catalogs, schemas, and tables  
<img width="858" height="577" alt="02  Create metastore" src="https://github.com/user-attachments/assets/2cb73655-b51b-4c7a-a51f-3160daf78b40" />


3. **Repository & Version Control Setup**
   - Create GitHub repository as the single source of truth
   - Enable collaboration, traceability, and rollback capability  
<img width="1903" height="917" alt="03  Create repo via Github" src="https://github.com/user-attachments/assets/9b89ec35-a160-4dff-9a96-ea4197f444f6" />


4. **Databricks Repos Integration**
   - Clone GitHub repository into Databricks workspace
   - Enable direct notebook development with Git-backed version control  
<img width="1900" height="907" alt="04  Create git folder via Databricks" src="https://github.com/user-attachments/assets/778eea73-c17e-4ea9-8297-358de73f9e2f" />


5. **Branching Strategy for Development**
   - Create feature branch for Data Engineering work
   - Isolate development changes from production logic  
<img width="470" height="161" alt="05 Create branch for working" src="https://github.com/user-attachments/assets/1e2abc96-61f2-4363-bc6f-6f10145bdde2" />


6. **Pull Request & Code Review Workflow**
   - Open Pull Request from feature branch
   - Review and validate engineering changes
   - Merge approved changes into main branch  
<img width="1866" height="917" alt="06  Pull request to main branch" src="https://github.com/user-attachments/assets/5c12e77b-894b-4e68-976d-c2c748b6a86e" />
<img width="1212" height="853" alt="07  From main branch merge request" src="https://github.com/user-attachments/assets/c6c906be-e6a7-46f0-b01f-cbb1bcc109a1" />
<img width="1188" height="627" alt="08  Main branch after merging" src="https://github.com/user-attachments/assets/f468a161-ba91-4819-8866-a566abf2858c" />

---

### **Section 2 — Initial Load (Historical Backfill)**
*Building the Lakehouse from raw data to analytics-ready tables*

This section demonstrates how historical NYC Taxi data is ingested and processed end-to-end using the Medallion Architecture.

7. **Catalog, Schema, and Volume Initialization**
   - Create catalog and schemas for each Medallion layer
   - Create volumes mapped to ADLS Gen2
   - Establish governed storage paths for raw ingestion  
<img width="1635" height="700" alt="09  createschema" src="https://github.com/user-attachments/assets/c6cf2274-5c10-4d29-94d6-eab076271aae" />


8. **Raw Data Ingestion via HTTPS**
   - Pull historical NYC Taxi data directly from public endpoints
   - Store raw files by `year-month` in landing volumes
   - Volumes abstract physical ADLS paths while remaining fully governed  
<img width="1912" height="1027" alt="10  initial load" src="https://github.com/user-attachments/assets/61194097-6ace-4d38-9724-4ca855424209" />
<img width="1912" height="1027" alt="11  Data load to volumes as folder" src="https://github.com/user-attachments/assets/697a4b61-56e2-4f5b-b751-6ab4102f22b2" />



9. **Physical Storage Verification in ADLS Gen2**
   - Validate that volume-backed data is physically stored in Azure
   - Confirm separation of compute (Databricks) and storage (ADLS)  
<img width="1905" height="1023" alt="12  Managed table, store in ADLS2" src="https://github.com/user-attachments/assets/e90c0ac9-fc0e-46b6-be56-056b850113fa" />


10. **Medallion Architecture Processing**
    - Bronze: raw structured Delta tables
    - Silver: cleaned, enriched, conformed datasets
    - Gold: aggregated, analytics-ready fact tables
    - All tables stored as managed Delta tables with ACID guarantees  
<img width="481" height="471" alt="13  After running initial_load for meddalion architecture" src="https://github.com/user-attachments/assets/84540134-5e1b-4828-8fd8-3331896e2d62" />
<img width="523" height="458" alt="14  after initial load" src="https://github.com/user-attachments/assets/4a0a03f2-0e4b-4041-9243-ad2ce3e65f6d" />

---

### **Section 3 — External Stakeholder Data Delivery**
*Serving downstream consumers without exposing internal Lakehouse storage*

This section focuses on enabling **controlled data sharing** to external stakeholders.

11. **Stakeholder Resource Provisioning**
    - Create separate Azure Resource Group
    - Provision dedicated ADLS Gen2 storage for stakeholders
    - Create Databricks Access Connector for secure cross-account access  
<img width="1913" height="1025" alt="15  Cretate resources for stakeholder" src="https://github.com/user-attachments/assets/2b9b19ad-8111-487b-aac5-f8054cb496f5" />


12. **External Location & Credential Configuration**
    - Create storage credentials in Databricks
    - Register external locations mapped to stakeholder ADLS
    - Enforce governance and permission boundaries  
<img width="1903" height="1025" alt="16  Create credentials and storage location from databricks" src="https://github.com/user-attachments/assets/3d334fe1-13ed-4062-ade5-dfe6ab8233de" />


13. **Initial Export to Stakeholder Storage**
    - Write curated Gold datasets to stakeholder ADLS
    - Partition data by business-relevant dimensions (e.g. year_month)
    - Ensure append-only, analytics-ready delivery  
<img width="1910" height="1030" alt="17  Load to stakeholder data month to 9" src="https://github.com/user-attachments/assets/d6c0c9df-1e46-41e6-8358-afd8cb8464ca" />


---

### **Section 4 — Incremental Load & Orchestration**
*Operating the pipeline like a real production system*

This section demonstrates how the pipeline evolves from a one-off load into a **repeatable, scheduled, and monitored job**.

14. **Merge Incremental Logic to Main Branch**
    - Pull latest incremental logic into main branch
    - Ensure production branch reflects the latest pipeline design  
<img width="1907" height="917" alt="17 1  Merge successfully from main branch" src="https://github.com/user-attachments/assets/0fbc5e0e-7af1-49ca-bac8-a85abff827fd" />
<img width="1910" height="1028" alt="17 2 pull code for incremental load and extra task" src="https://github.com/user-attachments/assets/9119ea14-b83f-407f-b775-aeae9910f148" />



15. **Databricks Job Orchestration**
    - Create multi-task Databricks Job
    - Define task dependencies across Bronze, Silver, Gold, and Export layers
    - Execute pipeline using Serverless compute  
<img width="1910" height="1027" alt="18  pipeline fail first run" src="https://github.com/user-attachments/assets/8abd90de-c32c-4ed9-a168-c44a75977bcc" />


16. **Failure Handling & Recovery**
    - Inspect failed task in job graph
    - Identify root cause from logs
    - Fix task-level issue and re-run affected stages
    - Validate successful end-to-end execution  
<img width="1907" height="1026" alt="19  job run successfully" src="https://github.com/user-attachments/assets/c1a7149b-3656-4c5b-9ea6-fdee322b9908" />

---

### **Section 5 — Data Validation & Quality Checks**
*Ensuring correctness, completeness, and historical integrity*

17. **Post-Run Data Validation**
    - Perform EDA on Gold tables
    - Validate record counts by `year-month`
    - Confirm incremental append behavior (e.g. 2025-10 added after 2025-09)
<img width="1226" height="536" alt="21  After incremental load" src="https://github.com/user-attachments/assets/14bc9cfb-959b-4baf-93bf-606a1f32c8ed" />


18. **SCD Type 2 Verification**
    - Validate dimension tables retain historical records
    - Confirm correct `start_date`, `end_date`, and current flags
    - Ensure no data loss during incremental updates
<img width="1221" height="587" alt="22  SCD type 2" src="https://github.com/user-attachments/assets/8d7838f7-aef4-49ec-87c4-24407864cd82" />


19. **Stakeholder Delivery Validation**
    - Confirm new month data is appended in stakeholder ADLS
    - Validate folder structure and partitioning consistency
<img width="1907" height="1025" alt="20  append one month to stakeholder file location" src="https://github.com/user-attachments/assets/caa75750-12d8-4843-a5fe-57c8f0e599c2" />

---

### **Section 6 — Performance & Scalability Considerations**

*This project is designed with **performance and scalability in mind**, while intentionally avoiding premature optimization.  
The focus is on **data layout, execution patterns, and architectural decisions** that scale naturally as data volume and usage increase.*

#### 6.1 Partition-Aware Data Layout

Large fact and export tables are organized using **time-based partitions** (e.g. `year_month` or `vendor`), enabling:

- Efficient incremental processing
- Query pruning for time-filtered analytics
- Predictable performance as historical data grows
- Simplified downstream data consumption for stakeholders

Partitioning decisions are aligned with **actual access patterns**, rather than arbitrary schema design.

<img width="1640" height="394" alt="image" src="https://github.com/user-attachments/assets/597e9397-89f5-42cd-8b45-15256339f3f5" />
<img width="1617" height="593" alt="image" src="https://github.com/user-attachments/assets/27aefaed-e246-4a78-a948-1a8e3b02b74f" />


#### 6.2 Delta Lake Optimization Strategy

All Bronze, Silver, and Gold datasets are stored using **Delta Lake**, providing:

- ACID transaction guarantees
- Schema enforcement and evolution
- Support for scalable file layout management

As data volume increases, **Delta Lake optimization techniques** (such as file compaction and layout optimization) are considered to reduce small-file overhead and improve scan efficiency.  
These optimizations are applied **based on workload behavior**, not blindly during early development.


#### 6.3 Efficient Join Design

Dimension enrichment in the Silver layer is designed with **join efficiency** in mind:

- Small, static lookup tables (e.g. taxi zone reference data) are kept intentionally lightweight
- This allows Spark to automatically apply **broadcast join optimizations** during execution
- Reduces shuffle cost and improves pipeline stability

Join strategies are driven by **data characteristics**, not manual forcing of execution plans.

#### 6.4 Compute & Execution Strategy

The pipeline leverages **Databricks Serverless compute** for batch and incremental workloads, providing:

- Elastic scaling based on job demand
- Reduced operational overhead
- Faster iteration during development and troubleshooting

Compute selection is aligned with the **batch-oriented nature** of the pipeline, with the ability to evolve toward more specialized clusters if workload patterns change.

#### 6.5 Deferred Optimization Philosophy

Performance tuning is treated as an **iterative process**, guided by:

- Job execution metrics
- Query access patterns
- Data growth trends
- Stakeholder usage behavior

This approach ensures that optimization efforts are **justified, measurable, and sustainable**, mirroring how performance engineering is handled in real production environments.
<img width="819" height="103" alt="image" src="https://github.com/user-attachments/assets/3603cc74-a089-4503-b726-1ac0969cb08a" />

---

### 🔐 Section 7 — Granting Access for Data Analysts at the Gold Layer

This section demonstrates how **fine-grained data access** is implemented using **Azure IAM + Databricks Unity Catalog**, ensuring that business users (Data Analysts) can **query curated Gold data** without exposure to raw or intermediate datasets.

The goal is to follow the **principle of least privilege**, a standard practice in enterprise data platforms.

---

#### 7.1 Azure-Level Access (Platform Entry Point)

Before granting any data access, the test Data Analyst account is granted access at the **Azure resource group level**.

This step ensures:
- The user can authenticate into the Databricks workspace
- Platform access is controlled separately from data access
- Cloud-level governance remains centralized in Azure

<img width="1918" height="905" alt="grant access from microsoft" src="https://github.com/user-attachments/assets/3a1d1625-a619-4c3b-9351-29bb04be555e" />

---

#### 7.2 Admin Workspace: Full Catalog Visibility

From the **admin Databricks workspace**, the `nyctaxi` catalog contains all schemas representing the Medallion architecture:

- `00_landing`
- `01_bronze`
- `02_silver`
- `03_gold`

At this stage:
- Only platform admins and data engineers have full visibility
- No permissions have been granted to the test Data Analyst

<img width="1918" height="910" alt="admin workspace" src="https://github.com/user-attachments/assets/8d6f405b-fbfa-4bb9-ad8a-e6719fd9a135" />

---

#### 7.3 Test User: No Catalog Visibility by Default

When logging in as the **test Data Analyst**, the `nyctaxi` catalog is **not visible**.

This confirms:
- Unity Catalog does **not expose data by default**
- Catalog-level access must be explicitly granted
- There is no accidental data leakage across users

<img width="1917" height="906" alt="test user workspace" src="https://github.com/user-attachments/assets/158970f2-c8dc-4661-82a5-f6640d74d3a5" />

---

#### 7.4 Granting Gold-Only Access (Unity Catalog)

Access is then granted to the test user with the following scope:

- **USE CATALOG** on `nyctaxi`
- **USE SCHEMA** on `nyctaxi.03_gold`
- **SELECT** on tables within `nyctaxi.03_gold`

No permissions are granted for:
- `00_landing`
- `01_bronze`
- `02_silver`

This ensures the Data Analyst:
- Can only work with **curated, business-ready data**
- Cannot access raw or intermediate layers
- Cannot modify schemas or tables

<img width="1908" height="902" alt="grant access for data analyst at gold layer" src="https://github.com/user-attachments/assets/83fe81b2-ed77-4a4a-b3da-b445ef150adf" />

---

#### 7.5 Scoped Visibility for the Data Analyst

After permissions are applied, the test user can now:

- See the `nyctaxi` catalog
- See **only the `03_gold` schema**
- Cannot see Bronze or Silver schemas at all

This confirms that **schema-level isolation** is working as intended.

<img width="1907" height="902" alt="from test workspace can only see gold layer" src="https://github.com/user-attachments/assets/75769878-8968-4ead-bfab-00f01321248a" />

---

#### 7.6 Querying Gold Data as a Data Analyst

Finally, the test user successfully queries a Gold table (e.g. `daily_trip_summary`) using the SQL Editor.

This validates:
- Read-only access is correctly configured
- Gold data is consumable by analytics workloads
- The Medallion architecture is enforced through permissions, not convention

<img width="1906" height="906" alt="test user can query gold layer at select" src="https://github.com/user-attachments/assets/67cc95f1-13d1-4bc4-86cb-545b082c9318" />

---

#### 7.7 Why This Matters (Enterprise Perspective)

This access model reflects real production environments where:

- Data Engineers own **pipeline logic and transformations**
- Data Analysts consume **trusted, curated outputs**
- Governance is enforced centrally via Unity Catalog
- Security rules scale across teams and projects

By restricting access to the Gold layer only, the platform:
- Reduces risk of misinterpretation of raw data
- Prevents accidental modification of upstream tables
- Supports compliance and audit requirements

#### ✅ Key Takeaways

- Azure IAM controls **who can enter the platform**
- Unity Catalog controls **what data users can see**
- Schema-level grants enable **clean separation of responsibilities**
- Gold-layer-only access is a best practice for analytics users

This setup demonstrates **production-ready data governance**, not just data processing.

---

## ✅ Outcome

By the end of this project:
- A fully governed **Databricks Lakehouse** is in place
- Historical and incremental pipelines run reliably
- Data is delivered to internal analytics and external stakeholders
- The system mirrors **real enterprise Data Engineering workflows**, not toy examples


