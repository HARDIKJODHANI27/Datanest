import pandas as pd

from app.analytics.data_quality import check_data_quality


df = pd.DataFrame({
    "NAME": ["Hardik", "Rahul", "Hardik", "Amit"],
    "AGE": [21, 22, 21, None],
    "COUNTRY": ["India", "India", "India", "India"],
    "EMPTY": [None, None, None, None]
})

result = check_data_quality(df)

print(result)