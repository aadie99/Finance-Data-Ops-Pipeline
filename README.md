# Finance Data Ops Pipeline

A Data Operations–oriented pipeline simulating real-world financial data ingestion, validation, and analytics workflows using SQL, with upcoming Python and AWS integration.

---

## Project Overview

This project simulates a real-world Data Operations workflow where a financial institution:

- Receives raw client credit data (CSV format)
- Loads it into a relational database (MySQL)
- Performs data quality validations
- Extracts analytical insights using SQL
- Prepares the system for automation and AWS deployment

The objective is to demonstrate practical Data Engineering and Data Operations skills aligned with modern analytics workflows.

---

## Dataset

**Dataset Used:** UCI Credit Card Default Dataset  
**Source:** https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients  

The dataset contains:
- 30,000 customer records
- 24 attributes
- Financial, demographic, and repayment history information
- Target variable indicating default behavior

---

## Tech Stack (Phase 1)

- MySQL Workbench
- SQL
- Git & GitHub
- VS Code

Upcoming:
- Python (Pandas ETL)
- AWS S3
- AWS Athena

---

# Phase 1 – SQL Ingestion & Sanity Checks

### 1. Database Setup
- Created database: `finance_pipeline`
- Imported CSV into table: `uci_credit_card_default_raw`

---

### 2. Data Sanity Checks Performed

#### Row Count Validation

```sql
SELECT COUNT(*) AS row_count
FROM uci_credit_card_default_raw;
```
`Result: Count = 30,000`
#### Null Value Checks (Key Fields)
```sql
SELECT
  SUM(CASE WHEN ID IS NULL THEN 1 ELSE 0 END) AS null_id,
  SUM(CASE WHEN LIMIT_BAL IS NULL THEN 1 ELSE 0 END) AS null_limit_bal,
  SUM(CASE WHEN AGE IS NULL THEN 1 ELSE 0 END) AS null_age
FROM uci_credit_card_default_raw;
```
`Result: No NULL values detected in critical fields`

#### Duplicate ID Detection
```sql
SELECT ID, COUNT(*) AS cnt
FROM uci_credit_card_default_raw
GROUP BY ID
HAVING cnt > 1;
```
`Result: No Duplicate IDs found`

#### Default Rate Calculation
```sql
SELECT
  AVG(`default.payment.next.month`) * 100 AS default_rate_percent
FROM uci_credit_card_default_raw;
```
`Result: Default Rate ~ 22%`

