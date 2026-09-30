import pandas as pd
import plotly.express as px


def numeric_distribution(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' is not numeric.")

    values = df[column].dropna()

    return values


def categorical_distribution(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")

    if not pd.api.types.is_string_dtype(df[column]):
        raise ValueError(f"Column '{column}' is not categorical.")

    values = df[column].dropna()

    return values.value_counts()


def identify_visualization_columns(df):
    numerical_columns = []
    categorical_columns = []

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            numerical_columns.append(column)

        elif pd.api.types.is_string_dtype(df[column]):
            categorical_columns.append(column)

    return {
        "numerical": numerical_columns,
        "categorical": categorical_columns
    }


def get_visualization_type(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset.")

    if pd.api.types.is_numeric_dtype(df[column]):
        return "histogram"

    elif pd.api.types.is_string_dtype(df[column]):
        return "bar"

    else:
        return "unsupported"


def create_numeric_histogram(df, column):
    values = numeric_distribution(df, column)

    figure = px.histogram(
        x=values,
        title=f"Distribution of {column}",
        labels={
            "x": column,
            "count": "Frequency"
        }
    )

    return figure


def create_categorical_bar_chart(df, column):
    values = categorical_distribution(df, column)

    figure = px.bar(
        x=values.index,
        y=values.values,
        title=f"Distribution of {column}",
        labels={
            "x": column,
            "y": "Frequency"
        }
    )

    return figure