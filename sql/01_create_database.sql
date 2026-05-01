-- ============================================================
-- 01_create_database.sql
-- ============================================================
DROP DATABASE IF EXISTS churn_dw;
CREATE DATABASE churn_dw WITH ENCODING = 'UTF8';
 
\connect churn_dw
 
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS dw;
 
COMMENT ON SCHEMA raw IS 'Raw ingestion layer';
COMMENT ON SCHEMA dw  IS 'Star schema data warehouse';
