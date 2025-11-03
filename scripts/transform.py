import pandas as pd
import glob

def transform_df():
    files = glob.glob("data/raw/*.csv")
    df = pd.concat([pd.read_csv(f) for f in files])
    
    df['order_date'] = pd.to_datetime(df['date_str'], format='%Y/%m/%d', errors='coerce')
    df['revenue'] = df['amount'].round(2)
    df['quarter'] = df['order_date'].dt.to_period('Q')
    
    df = df[['order_id', 'order_date', 'customer', 'revenue', 'quarter']]
    df.to_parquet("data/staging/transformed.parquet", index=False)
    print("Transformed with pandas")
    return df
