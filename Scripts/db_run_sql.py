import sqlite3
import os

def run_sql_query():

    sql_patch = '/workspaces/Data_Analysis/Supply Chain Analisys/SQL/dimensional_modeling.sql'
    db_path = '/workspaces/Data_Analysis/Supply Chain Analisys/DB/supply_chain.db'

    if not os.path.exists(db_path):
        print('Database not found')
        return
    else:
        print('Database found, executing query...')

    conn = sqlite3.connect(db_path)

    try:
        cursor = conn.cursor()

        with open(sql_patch, 'r') as file:
            sql_patch = file.read()

        cursor.executescript(sql_patch)
        conn.commit()

        print('Query executed successfully, tables created.')
        return
    except Exception as e:
        print(f'Error: {e}')
    finally:
        conn.close()

if __name__ == '__main__':
    run_sql_query()