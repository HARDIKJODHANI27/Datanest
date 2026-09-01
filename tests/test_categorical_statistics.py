import pandas as pd

from app.analytics.categorical_statistics import categorical_statistics



df = pd.DataFrame({
    "CUSTOMER_TYPE": [
        "Retail",
        "Corporate",
        "Retail",
        "Retail",
        "Individual"
    ],
    "CITY": [
        "Delhi",
        "Mumbai",
        "Delhi",
        "Delhi",
        "Mumbai"
    ],
    "SALES": [100, 200, 300, 400, 500]
})


result = categorical_statistics(df)

print(result)