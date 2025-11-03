def save_parquet():
    import pandas as pd
    df = pd.read_parquet("data/staging/transformed.parquet")
    df.to_parquet("data/processed/analytics_ready.parquet", partition_cols=['quarter'])
    print("Loaded to partitioned Parquet")
