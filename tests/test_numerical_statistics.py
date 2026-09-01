import pandas as pd

from app.analytics.numerical_statistics import numeric_statistics

df = pd.DataFrame({
    "NAME": ["Hardik", "Rahul", "Hardik", "Amit"],
    "AGE": [21, 22, 21, None],
    "COUNTRY": ["India", "India", "India", "India"],
    "EMPTY": [None, None, None, None]
})

result = numeric_statistics(df)

print(result)