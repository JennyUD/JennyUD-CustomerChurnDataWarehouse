from __01extract_kaggle import df
from __02transform_churn import classify_schema
import os
from sqlalchemy import create_engine, text

# 1. Classify schema
schema, dimensions, facts = classify_schema(df)

# 2. Build dimension DataFrames
dimension_dfs = {
    dim_name: df[cols].drop_duplicates().reset_index(drop=True)
    for dim_name, cols in dimensions.items()
}

# 3. Secure password
password = os.getenv("PG_PASSWORD")

engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5432/churn_dw"
)

# 4. Create correct dimension tables
with engine.connect() as conn:
    for dim_name, cols in dimensions.items():

        # Drop old table if exists
        conn.execute(text(f"DROP TABLE IF EXISTS dw.{dim_name} CASCADE"))

        # Build column definitions
        col_defs = ", ".join([f'"{col}" TEXT' for col in cols])

        # Create table with surrogate key + natural key(s)
        create_sql = f"""
        CREATE TABLE dw.{dim_name} (
            {dim_name}_id SERIAL PRIMARY KEY,
            {col_defs}
        );
        """

        conn.execute(text(create_sql))
        print(f"[DDL] Created table dw.{dim_name}")

# 5. Load dimension data
for dim_name, dim_df in dimension_dfs.items():
    dim_df.to_sql(
        name=dim_name,
        con=engine,
        schema="dw",
        if_exists="append",
        index=False
    )
    print(f"[SUCCESS] Loaded {len(dim_df)} rows into dw.{dim_name}")

print("\n All dimension tables created and loaded successfully!")
