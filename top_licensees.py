import pandas as pd

df = pd.read_parquet("data/wells.parquet")
print(df["Licensee"].value_counts().head(10))