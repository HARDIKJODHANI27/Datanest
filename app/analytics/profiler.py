import pandas as pd


def profile_dataframe(df):
    profile = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    return profile

def profile_columns(df):
    column_profiles = []

    for column in df.columns:
        column_profile = {
            "column_name": column,
            "data_type": str(df[column].dtype),
            "missing_values": int(df[column].isna().sum()),
            "unique_values": int(df[column].nunique())
        }

        column_profiles.append(column_profile)

    return column_profiles