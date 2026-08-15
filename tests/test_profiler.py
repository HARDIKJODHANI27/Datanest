from app.utils.file_loader import load_file
from app.analytics.profiler import profile_dataframe, profile_columns


file_path = "data/raw/test.csv"

df = load_file(file_path)

print(df)

print("\nDATA PROFILE")

profile = profile_dataframe(df)

for key, value in profile.items():
    print(f"{key}: {value}")


print("\nCOLUMN PROFILE")

column_profiles = profile_columns(df)

for column in column_profiles:
    print(column)