import pandas as pd

from app.analytics.visualization import (
    numeric_distribution,
    categorical_distribution,
    identify_visualization_columns,
    get_visualization_type,
    create_numeric_histogram,
    create_categorical_bar_chart
)


df = pd.DataFrame({
    "SALES": [100, 150, 200, 300, 450],
    "CITY": [
        "Delhi",
        "Kolkata",
        "Delhi",
        "Mumbai",
        "Delhi"
    ]
})


print("Numeric Distribution:")

print(
    numeric_distribution(df, "SALES")
)


print("\nCategorical Distribution:")

print(
    categorical_distribution(df, "CITY")
)


print("\nVisualization Columns:")

columns = identify_visualization_columns(df)

print(
    "Numerical:",
    columns["numerical"]
)

print(
    "Categorical:",
    columns["categorical"]
)


print("\nVisualization Types:")

print(
    "SALES:",
    get_visualization_type(df, "SALES")
)

print(
    "CITY:",
    get_visualization_type(df, "CITY")
)


figure = create_numeric_histogram(df, "SALES")

print("\nHistogram:")

print(type(figure))


figure = create_categorical_bar_chart(df, "CITY")

print("\nCategorical Bar Chart:")

print(type(figure))