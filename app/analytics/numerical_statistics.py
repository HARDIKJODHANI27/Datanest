import pandas as pd

def numeric_statistics(df):
    numeric_df = df.select_dtypes(include=["number"])

    statistics = []

    for column in numeric_df.columns:
        statistics.append({
            "column": column,
            "minimum": numeric_df[column].min(),
            "maximum": numeric_df[column].max(),
            "mean": numeric_df[column].mean(),
            "median": numeric_df[column].median()
        })

    return statistics