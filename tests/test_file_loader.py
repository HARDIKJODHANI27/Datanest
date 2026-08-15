from app.utils.file_loader import load_file


file_path = "data/raw/test.csv"

df = load_file(file_path)

print(df)
print()
print("Rows:", len(df))
print("Columns:", len(df.columns))