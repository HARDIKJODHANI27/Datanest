import pandas as pd
from pathlib import Path


def load_file(file):
    if isinstance(file, (str, Path)):
        file_path = Path(file)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        extension = file_path.suffix.lower()

    else:
        extension = Path(file.name).suffix.lower()

    if extension == ".csv":
        return pd.read_csv(file)

    if extension in [".xlsx", ".xls"]:
        return pd.read_excel(file)

    raise ValueError(f"Unsupported file type: {extension}")