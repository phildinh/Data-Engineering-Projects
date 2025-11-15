# 🚀 My First Data Engineering Project with Microsoft Azure Data Factory

This project demonstrates a **basic ETL pipeline** built in **Microsoft Azure Data Factory** using drag-and-drop components. The pipeline ingests data from multiple sources (CSV and GitHub API), transforms it based on stakeholder requirements, and stores it in a structured Data Lake environment for departmental access.  

---

## 🔄 ETL Process Overview
1. **Source**  
   - CSV files  
   - GitHub API (HTTP connection)

2. **Load**  
   - Ingest raw data into **Azure Data Lake**

3. **Transform & Process**  
   - Clean and process data inside the Data Lake  
   - Apply stakeholder-defined rules  

4. **Store**  
   - Save processed data in dedicated folders for departmental access  

5. **Automation**  
   - Configure triggers to **automate pipeline execution**  

---

## 🏗 Environment Setup in Azure
### 1. Create Resources
- **Azure Storage Account**  
- **Azure Data Lake**

### 2. Define Containers
- **Source File** → stores raw CSV datasets  
- **Destination File** → stores transformed datasets  
- **Reporting File** → stores department-specific datasets  

![Storage Setup](https://github.com/user-attachments/assets/5ed481b7-22aa-4bca-bfb9-d409aab6ef50)

---

## 🔧 Pipeline Details
### Data Flow
- Load data from **GitHub API** into the destination container  
- Transform datasets based on business requirements  

![Pipeline Structure](https://github.com/user-attachments/assets/25435f1b-43bd-4525-85d6-51b297ad38fd)

### Transformation Example
- Applied cleaning and transformation logic  
- Ensured schema consistency for downstream reporting  

![Transformation Detail](https://github.com/user-attachments/assets/3b683b30-0683-4e6b-b76c-441638da3ec4)

### Final Orchestration
- Combined all pipeline steps into a **master pipeline**  
- Configured trigger for automated runs  

![Pipeline Orchestration](https://github.com/user-attachments/assets/5056ecda-16cc-4756-bc55-119c8f1c1855)

---

## 📊 Pipeline Management
Monitor, debug, and manage pipeline execution from the **Pipeline Manager** interface.  

![Pipeline Manager](https://github.com/user-attachments/assets/518dec49-2ee0-4a39-aff7-75a87bc12eb7)

---

## ✅ Key Outcomes
- Successfully created a **working ETL pipeline** in Azure Data Factory  
- Automated **data ingestion, transformation, and storage**  
- Enabled **department-level access** to processed datasets  
- Built foundational skills in **cloud-based data engineering**  

---

📌 *This marks the beginning of my journey in Data Engineering using Azure!*
