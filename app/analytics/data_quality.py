import pandas as pd


def check_data_quality(df):
    quality = {}

    quality["missing_values"] = int(df.isna().sum().sum())
    quality["duplicate_rows"] = int(df.duplicated().sum())

    quality["empty_columns"] = [
        column
        for column in df.columns
        if df[column].isna().all()
    ]

    quality["missing_columns"] = {
        column: int(df[column].isna().sum())
        for column in df.columns
        if df[column].isna().sum() > 0
    }

    quality["constant_columns"] = [
        column
        for column in df.columns
        if df[column].nunique() == 1
    ]

    return quality

