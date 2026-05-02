from _01extract_kaggle  import df, get_schema

def classify_schema(df):
    schema = get_schema(df)

    dimensions = {}
    facts = []

    for _, row in schema.iterrows():
        col = row["column"]
        uniq = row["unique"]

        if "id" in col.lower():
            dimensions.setdefault("dim_customer", []).append(col)

        elif uniq <= 10:
            dim_name = f"dim_{col.lower().replace(' ', '_')}"
            dimensions[dim_name] = [col]

        else:
            facts.append(col)

    print("\n=== DIMENSIONS ===")
    print(dimensions)

    print("\n=== SCHEMA ===")
    print(schema)

    print("\n=== FACTS ===")
    print(facts)

    return schema, dimensions, facts

classify_schema(df)