import pandas as pd

df = pd.read_parquet("data/wells.parquet")
print(df["licensee"].value_counts().head(10))