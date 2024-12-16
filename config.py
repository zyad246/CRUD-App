# config.py
import pyodbc

# Connection string for SQL Server
DATABASE_CONNECTION_STRING = (
    'DRIVER={SQL Server};'
    'SERVER=ZYAD-MOHAMED\\MSSQLSERVER01;'  # Update this with your server name
    'DATABASE=InventoryDB;'
    'Trusted_Connection=yes;'  # Use Windows Authentication
)

def get_db_connection():
    """Establish and return a database connection."""
    connection = pyodbc.connect(DATABASE_CONNECTION_STRING)
    print("DB Connected")
    return connection
