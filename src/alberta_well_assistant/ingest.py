from pathlib import Path
import pandas as pd

RAW = Path("data/raw/production_strings.xlsx")
OUT = Path("data/wells.parquet")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]

    for col in df.columns:
        df[col] = df[col].map(lambda v: v.strip() if isinstance(v, str) else v)

    for col in df.columns:
        if col.endswith("_date"):
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def main() -> None:
    df = clean(pd.read_excel(RAW))
    df.to_parquet(OUT)
    print(f"Saved {len(df):,} rows to {OUT}")


if __name__ == "__main__":
    main()
