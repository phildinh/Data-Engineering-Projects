# dbt + Databricks Analytics Engineering Project (Bronze → Silver → Gold)

## 📌 Project Overview

This project demonstrates an **end‑to‑end analytics engineering workflow** built using **dbt (data build tool)** on top of **Databricks / Spark SQL**, following a **Medallion Architecture (Bronze → Silver → Gold)**.

The goal of the project is to showcase how raw data can be transformed into **trusted, analytics‑ready datasets** using dbt best practices such as:

* modular SQL models
* sources & lineage
* tests & data quality checks
* macros for reusable logic
* snapshots for Slowly Changing Dimensions (SCD Type 2)

This repository is designed as a **portfolio‑ready project** to demonstrate real‑world analytics engineering skills rather than just SQL transformations.

---

## 🏗️ Architecture Overview

The project follows a **Lakehouse‑style Medallion Architecture**:

```
Raw Data (Databricks Tables)
        ↓
     Bronze
  (Raw / Light Cleanup)
        ↓
     Silver
  (Cleaned, Conformed, Deduplicated)
        ↓
      Gold
  (Analytics‑ready, Business‑focused)
```

Each layer has a **clear responsibility**, enforced by dbt models, tests, and documentation.

---

## 📂 Repository Structure

```
DBT_TUTORIAL_YOUTUBE/
├── phil_dbt_youtube/
│   ├── models/
│   │   ├── bronze/
│   │   │   ├── bronze_sales.sql
│   │   │   ├── bronze_customer.sql
│   │   │   ├── bronze_product.sql
│   │   │   ├── bronze_store.sql
│   │   │   ├── bronze_date.sql
│   │   │   └── bronze_returns.sql
│   │   │
│   │   ├── silver/
│   │   │   └── silver_salesinfo.sql
│   │   │
│   │   ├── gold/
│   │   │   └── source_gold_items.sql
│   │   │
│   │   └── source/
│   │       └── sources.yml
│   │
│   ├── macros/
│   │   └── multiply.sql
│   │
│   ├── snapshots/
│   │   └── gold_items.sql
│   │
│   ├── seeds/
│   ├── tests/
│   └── dbt_project.yml
│
├── profiles.yml
├── README.md
└── pyproject.toml
```

---

## 🥉 Bronze Layer – Raw & Standardized Data

### Purpose

The **Bronze layer** represents data that is:

* sourced directly from upstream systems
* lightly cleaned and typed
* preserved close to its original structure

Bronze models intentionally **avoid business logic** and focus on:

* column selection
* basic renaming
* minimal transformations

### Example: `bronze_sales.sql`

Key responsibilities:

* select raw sales fields
* ensure consistent column naming
* prepare data for downstream joins

Bronze models may still contain:

* duplicates
* nulls
* inconsistent keys

This is expected by design.

---

## 🥈 Silver Layer – Cleaned & Conformed Data

### Purpose

The **Silver layer** is where data becomes **trustworthy and join‑ready**.

Responsibilities include:

* deduplication using window functions
* standardizing business keys
* resolving data quality issues
* applying core business logic

### Example: `silver_salesinfo.sql`

This model demonstrates:

* joining multiple Bronze tables (sales, product, customer)
* enforcing a **clear grain** (one row per sale)
* removing duplicates using `ROW_NUMBER()`
* calculating canonical metrics (e.g. gross_amount)

Silver models **never use `SELECT *`** and expose a stable schema for analytics.

---

## 🥇 Gold Layer – Analytics‑Ready Outputs

### Purpose

The **Gold layer** contains datasets designed for:

* BI dashboards
* reporting
* downstream analytics

Gold models:

* are business‑friendly
* have stable contracts
* expose only meaningful fields

In this project, the Gold layer also demonstrates **Slowly Changing Dimensions (SCD Type 2)** using dbt snapshots.

---

## 🕒 Snapshots – Slowly Changing Dimension (SCD Type 2)

### Why Snapshots?

Snapshots are used to track **historical changes** in dimension data over time.

This project implements **SCD Type 2** using dbt’s snapshot feature:

* old records are closed with `dbt_valid_to`
* new records are inserted with updated values

### Example: `gold_items.sql` snapshot

Key configuration:

* `strategy: timestamp`
* `updated_at: updateDate`
* `unique_key: id`

This allows point‑in‑time analysis and full change history tracking.

---

## 🧩 Macros – Reusable Business Logic

### Example: `multiply.sql`

The project includes a reusable macro:

```sql
{% macro multiply(col1, col2) %}
    coalesce({{ col1 }}, 0) * coalesce({{ col2 }}, 0)
{% endmacro %}
```

This demonstrates:

* abstraction of common logic
* null‑safe calculations
* reusable, testable SQL patterns

Macros are used in Silver models to ensure **consistent metric definitions**.

---

## 🔍 Sources, Tests & Lineage

### Sources

`sources.yml` defines upstream tables and establishes **data lineage** from raw sources into dbt models.

### Tests

The project uses dbt tests to enforce data quality:

* `not_null`
* `unique`
* `accepted_values`
* relationship tests between facts and dimensions

These tests ensure issues are caught **before dashboards break**.

### Lineage

All transformations are traceable through **dbt Docs**, providing:

* model‑level lineage
* column‑level documentation
* impact analysis

---

## 🛠️ Tooling & Technologies

* **dbt Core** – analytics engineering framework
* **Databricks / Spark SQL** – execution engine
* **Git & GitHub** – version control
* **VS Code** – development environment

---

## 🎯 Skills Demonstrated

This project showcases:

* Analytics Engineering best practices
* dbt model design (Bronze / Silver / Gold)
* Data quality testing & governance
* SCD Type 2 snapshot implementation
* Reusable macro development
* SQL optimization & window functions
* Production‑ready project structure

---

## 🚀 How to Run

```bash
dbt debug
dbt run
dbt test
dbt snapshot
dbt docs generate
dbt docs serve
```

---

## 📌 Final Notes

This project is intentionally designed to reflect **real‑world analytics engineering workflows**, focusing on **clarity, correctness, and maintainability** rather than one‑off SQL scripts.

It serves as a strong foundation for roles such as:

* Analytics Engineer
* Data Analyst (Advanced)
* Data Engineer (Analytics‑focused)

---

**Author:** Phil
**Focus:** dbt · Databricks · Analytics Engineering

