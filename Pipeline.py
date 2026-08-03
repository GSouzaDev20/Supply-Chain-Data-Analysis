from Scripts.db_creation import csv_to_sql
from Scripts.db_run_sql import run_sql_query

print("Starting the data pipeline...")
print("Creating the database and populating it with data from CSV...")

csv_to_sql()

print("Database created and populated successfully.")
print("Running SQL queries on the database...")
run_sql_query()

print("SQL queries executed successfully. Data pipeline completed.")