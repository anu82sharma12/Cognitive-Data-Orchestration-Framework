def dedupe_incremental():
    import pandas as pd
    new = pd.read_parquet("data/staging/transformed.parquet")
    try:
        old = pd.read_parquet("data/processed/analytics_ready.parquet")
        combined = pd.concat([old, new]).drop_duplicates('order_id')
    except:
        combined = new
    combined.to_parquet("data/staging/deduped.parquet", index=False)
    print("Incremental dedupe complete")
