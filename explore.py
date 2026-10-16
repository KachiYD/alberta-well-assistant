import pandas as pd

df = pd.read_excel("data/raw/production_strings.xlsx")

print(df.shape)
print(df.columns.tolist())
print(df.head())

df.to_parquet("data/wells.parquet")