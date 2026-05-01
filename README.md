# Customer Churn Data Warehouse
 
End-to-end data warehouse project for analyzing customer churn using a star schema.
 
## Project Structure
```
customer-churn-data-warehouse/
â”œâ”€â”€ sql/         â†’ DDL & DML scripts (run in order 01 â†’ 06)
â”œâ”€â”€ data/        â†’ Raw CSV source files
â”œâ”€â”€ etl/         â†’ Python ETL pipeline scripts
â”œâ”€â”€ config/      â†’ Database connection config
â””â”€â”€ .gitignore
```
 
## Quick Start
 
### 1. Configure your database
Edit `config/db_config.yaml` with your PostgreSQL credentials.
 
### 2. Run the full Python ETL pipeline
```bash
pip install psycopg2-binary pandas pyyaml
python etl/run_pipeline.py
```
 
## Star Schema
- **Fact:** fact_orders
- **Dims:** dim_customer, dim_product, dim_date, dim_support
