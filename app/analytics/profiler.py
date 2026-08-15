import pandas as pd


def profile_dataframe(df):
    profile = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    return profile