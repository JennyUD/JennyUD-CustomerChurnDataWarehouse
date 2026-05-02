import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os
from __01extract_kaggle import df

password = os.getenv("PG_PASSWORD")

# psycopg2 connection
conn = psycopg2.connect(
    host="localhost",
    database="churn_dw",
    user="postgres",
    password=password
)
cur = conn.cursor()

# Get dimension tables
cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'dw'
    AND table_name LIKE 'dim_%'
""")

dim_tables = [row[0] for row in cur.fetchall()]

engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/churn_dw")

# NATURAL KEY MAP 
natural_keys = {
    "dim_customer": ["CustomerID"],
    "dim_gender": ["Gender"],
    "dim_subscription_type": ["Subscription Type"],
    "dim_contract_length": ["Contract Length"],
    "dim_churn": ["Churn"]
}

# Merge surrogate keys
for dim in dim_tables:
    print(f"Merging {dim}...")

    dim_df = pd.read_sql(f"SELECT * FROM dw.{dim}", engine)

    # natural key columns
    nk = natural_keys[dim]

      # FIX: convert both sides to string
    for col in nk:
        df[col] = df[col].astype(str)
        dim_df[col] = dim_df[col].astype(str)

    # merge on natural key(s)
    df = df.merge(dim_df, on=nk, how="left")

# Build fact DataFrame
fact_columns = [
    "dim_customer_id",
    "dim_gender_id",
    "dim_subscription_type_id",
    "dim_contract_length_id",
    "dim_churn_id",
    "age",
    "tenure",
    "usage_frequency",
    "support_calls",
    "payment_delay",
    "total_spend",
    "last_interaction"
]


df.columns = df.columns.str.lower().str.replace(" ", "_")
fact_df = df[fact_columns]

# Load fact table
fact_df.to_sql(
    name="fact_churn",
    con=engine,
    schema="dw",
    if_exists="append",
    index=False
)

print(f"Loaded {len(fact_df)} rows into dw.fact_churn")
