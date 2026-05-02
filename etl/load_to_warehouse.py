from extract_kaggle import df
from transform_churn import classify_schema
import os

schema, dimensions, facts = classify_schema(df)

OUTPUT_PATH = 'sql/02_create_tables.sql'

def generate_dimensional_sql(dim_name, cols):
    sql = f"CREATE TABLE dw.{dim_name} (\n"
    sql += f"  {dim_name}_id SERIAL PRIMARY KEY,\n"
    for col in cols:
        col_clean = col.lower().replace(" ", "_")
        sql += f"  {col_clean} VARCHAR(255),\n"
    sql = sql.rstrip(",\n") + "\n);\n\n"
    return sql

def generate_fact_sql(fact_name, fact_cols, dimensions):
    sql = f"CREATE TABLE dw.{fact_name} (\n"
    sql += "  fact_id SERIAL PRIMARY KEY,\n"

    for dim in dimensions:
        sql += f"  {dim}_id INT REFERENCES dw.{dim}({dim}_id),\n"

    for col in fact_cols:
        col_clean = col.lower().replace(" ", "_")
        sql += f"  {col_clean} NUMERIC,\n"

    sql = sql.rstrip(",\n") + "\n);\n\n"
    return sql

def write_sql_file():
    os.makedirs("sql", exist_ok=True)

    with open(OUTPUT_PATH, "w") as f:
        f.write("-- 02_create_tables.sql (Auto-generated)\n\n")
        f.write("-- Run this file with:\n")
        f.write("-- psql -U postgres -d churn_dw -f sql/02_create_tables.sql\n\n")
        f.write(f"CREATE SCHEMA IF NOT EXISTS dw;\n\n")


        for dim_name, cols in dimensions.items():
            f.write(generate_dimensional_sql(dim_name, cols))

        f.write(generate_fact_sql("fact_churn", facts, dimensions))

    print(f"SQL DDL written to {OUTPUT_PATH}")

if __name__ == "__main__":
    write_sql_file()
