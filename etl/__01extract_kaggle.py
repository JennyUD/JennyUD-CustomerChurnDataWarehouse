import pandas as pd

path = r"data\processed\clean_churn.csv"
df = pd.read_csv(path)
print(f"Number of rows in df: {len(df)}")

def get_schema(df):
    schema = pd.DataFrame({
        "column": df.columns,
        "dtype": df.dtypes.astype(str),
        "unique": df.nunique()
    })
    print("\n=== SCHEMA ===")
    print(schema)
    return schema
  
#get_schema(df)


