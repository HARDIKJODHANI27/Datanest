import pandas as pd

def categorical_statistics(df):
    categorical_df = df.select_dtypes(include=["object", "category"])

    statistics = []

    for column in categorical_df.columns:

        value_counts = categorical_df[column].value_counts()
        if not value_counts.empty:
            statistics.append({
                "column": column,
                "unique_values": categorical_df[column].nunique(),
                "most_common": value_counts.index[0],
                "frequency": value_counts.iloc[0]
            })

    return statistics