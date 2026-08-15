import pyodbc


SERVER = "localhost"
DATABASE = "Datanest"
DRIVER = "ODBC Driver 18 for SQL Server"


def get_connection():
    connection_string = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)