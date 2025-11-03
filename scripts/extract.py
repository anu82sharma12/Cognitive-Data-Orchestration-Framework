import glob
import pandas as pd
import os

def extract_all():
    os.makedirs("data/raw", exist_ok=True)
    # Simulate 10 raw CSVs
    for i in range(10):
        df = pd.DataFrame({
            "order_id": range(i*1000, (i+1)*1000),
            "date_str": pd.date_range("2025-01-01", periods=1000).strftime("%Y/%m/%d"),
            "amount": pd.np.random.lognormal(5, 1, 1000),
            "customer": [f"CUST_{x}" for x in range(1000)]
        })
        df.to_csv(f"data/raw/sales_{i+1}.csv", index=False)
    print("Extracted 10 CSVs")
