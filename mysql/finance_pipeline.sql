-- FINANCE DATA OPS PIPELINE - PHASE 1 (MYSQL)
-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS finance_pipeline;
USE finance_pipeline;

-- SANITY CHECK - PREVIEW
SELECT * FROM uci_credit_card_default_raw LIMIT 5;

-- VALIDATION CHECKS - PHASE 1
-- 1. ROW COUNT
SELECT COUNT(*) AS ROW_COUNT
FROM uci_credit_card_default_raw;

-- 2. NULL CHECKS FOR KEY FIELDS	
SELECT
  SUM(CASE WHEN ID IS NULL THEN 1 ELSE 0 END) AS null_id,
  SUM(CASE WHEN LIMIT_BAL IS NULL THEN 1 ELSE 0 END) AS null_limit_bal,
  SUM(CASE WHEN AGE IS NULL THEN 1 ELSE 0 END) AS null_age,
  SUM(CASE WHEN EDUCATION IS NULL THEN 1 ELSE 0 END) AS null_education
FROM uci_credit_card_default_raw;

-- 3. DUPLICATE CHECK ON PRIMARY KEY -> ID
SELECT ID, COUNT(*) AS CNT
FROM uci_credit_card_default_raw
GROUP BY ID
HAVING CNT > 1;
-- ORDER BY CNT DESC
-- LIMIT 20;

-- 4. DEFAULT RATE %
SELECT
  AVG(`default.payment.next.month`) * 100 AS default_rate_percent
FROM uci_credit_card_default_raw;






