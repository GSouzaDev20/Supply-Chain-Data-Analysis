# End-to-End Supply Chain Data Pipeline

A Data Engineering and Analytics project focused on building an automated ETL pipeline to ingest, clean, transform, model, and analyze global supply chain logistics data.

The project simulates a real-world analytics workflow by transforming raw operational data into structured datasets ready for business intelligence and decision-making.

---

# 📌 Project Overview

Supply chain operations generate large volumes of data involving suppliers, products, transportation, carriers, costs, and delivery performance.

Poor data quality, inefficient transportation processes, and long lead times can negatively impact operational efficiency and profitability.

The objective of this project is to develop an end-to-end data pipeline capable of:

- Extracting raw supply chain data
- Performing data cleaning and validation
- Applying business rules and feature engineering
- Storing processed data in a relational database
- Creating an analytical data model using dimensional modeling
- Preparing data for business intelligence analysis

---

# 🏗️ Pipeline Architecture


Raw Supply Chain CSV Data
|
↓
Python ETL Pipeline
(Pandas + Data Cleaning)
|
↓
SQLite Database
|
↓
SQL Dimensional Modeling
(Star Schema)
|
↓
Power BI Dashboard


---

# 🛠️ Tech Stack

## Programming Language

- Python

## Data Processing

- Pandas
- NumPy

## Database

- SQLite

## Data Modeling

- Dimensional Modeling
- Star Schema

## Business Intelligence

- Power BI

## Development Tools

- Git
- GitHub
- VS Code

---

# 🔄 Data Pipeline Workflow

## 1. Data Ingestion

The pipeline starts by loading raw supply chain data from CSV files.

The ingestion process is automated using Python scripts, creating a repeatable workflow.

---

## 2. Data Cleaning and Transformation

The ETL process performs several data quality improvements:

- Standardization of column names
- Removal of invalid records
- Treatment of missing values
- Data validation rules
- Feature engineering

Examples of created metrics:

### Total Lead Time

Calculation combining:

- Production lead time
- Shipping time

### Gross Margin Rate

Calculation based on:

- Revenue generated
- Operational costs

---

## 3. Database Loading

After processing, the transformed dataset is loaded into a SQLite relational database.

Main analytical table:


supply_chain_data


The database provides structured storage for further SQL analysis.

---

## 4. Data Modeling

The project applies dimensional modeling concepts to improve analytical performance.

The final model follows a Star Schema architecture containing:

### Fact Tables

Store measurable business events:

- Shipments
- Costs
- Revenue
- Delivery performance

### Dimension Tables

Store descriptive information:

- Products
- Suppliers
- Logistics
- Customers

---

# 📂 Project Structure


Supply-Chain-Data-Analysis/

│
├── Data/
│ └── supply_chain_data_RAW.csv
│
├── DB/
│ └── supply_chain.db
│
├── SQL/
│ └── dimensional_modeling.sql
│
├── Scripts/
│ ├── db_creation.py
│ └── db_run_sql.py
│
├── Pipeline.py
│
├── requirements.txt
│
└── README.md


---

# 📊 Business Questions

This project aims to answer important supply chain questions:

- Which carriers have the best delivery performance?
- Which suppliers present higher operational risks?
- Which products generate higher profitability?
- What factors influence transportation delays?
- How can lead times be reduced?
- Where are the main operational bottlenecks?

---

# 🚀 Pipeline Execution

Install project dependencies:

```bash
pip install -r requirements.txt

