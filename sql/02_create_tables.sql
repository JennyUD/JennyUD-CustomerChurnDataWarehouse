-- 02_create_tables.sql (Auto-generated)

CREATE SCHEMA IF NOT EXISTS dw;

CREATE TABLE dw.dim_customer (
  dim_customer_id SERIAL PRIMARY KEY,
  customerid VARCHAR(255)
);

CREATE TABLE dw.dim_gender (
  dim_gender_id SERIAL PRIMARY KEY,
  gender VARCHAR(255)
);

CREATE TABLE dw.dim_subscription_type (
  dim_subscription_type_id SERIAL PRIMARY KEY,
  subscription_type VARCHAR(255)
);

CREATE TABLE dw.dim_contract_length (
  dim_contract_length_id SERIAL PRIMARY KEY,
  contract_length VARCHAR(255)
);

CREATE TABLE dw.dim_churn (
  dim_churn_id SERIAL PRIMARY KEY,
  churn VARCHAR(255)
);

CREATE TABLE dw.fact_churn (
  fact_id SERIAL PRIMARY KEY,
  dim_customer_id INT REFERENCES dw.dim_customer(dim_customer_id),
  dim_gender_id INT REFERENCES dw.dim_gender(dim_gender_id),
  dim_subscription_type_id INT REFERENCES dw.dim_subscription_type(dim_subscription_type_id),
  dim_contract_length_id INT REFERENCES dw.dim_contract_length(dim_contract_length_id),
  dim_churn_id INT REFERENCES dw.dim_churn(dim_churn_id),
  age NUMERIC,
  tenure NUMERIC,
  usage_frequency NUMERIC,
  support_calls NUMERIC,
  payment_delay NUMERIC,
  total_spend NUMERIC,
  last_interaction NUMERIC
);

