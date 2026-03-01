-- DATABASE CREATION
CREATE DATABASE IF NOT EXISTS finance_pipeline;
USE finance_pipeline;

-- SANITY CHECKS 
SELECT * FROM uci_credit_card_default_raw LIMIT 5;