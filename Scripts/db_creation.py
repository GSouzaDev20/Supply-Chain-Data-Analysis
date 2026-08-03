import sqlite3
import pandas as pd
import os

def csv_to_sql():

    print('Reading CSV Path...')

    csv_path = '/workspaces/Data_Analysis/Supply Chain Analisys/Data/supply_chain_data_RAW.csv'
    db_path = '/workspaces/Data_Analysis/Supply Chain Analisys/DB/supply_chain.db'

    if not os.path.exists(csv_path):
        print('CSV not found')
        return
    else:
        print('CSV found, processing data...')

    df = pd.read_csv(csv_path)

    # Clean column names: remove spaces, convert to lowercase, and remove parentheses 
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower().str.replace('(', '').str.replace(')', '')

    # Data quality checks: remove negative prices and drop rows with missing SKUs
    df = df[df['price'] >= 0]
    df = df.dropna(subset=['sku'])

    # Business rules

    #Clear column Customer_demographics
    df['customer_demographics'] = ( 
        df['customer_demographics']
        .astype('string')
        .str.strip()
        .replace('', pd.NA)
        .fillna('Unknown')
    )

    # Total lead time column creation
    df['total_lead_time'] = df['lead_times'] + df['shipping_times']
    
    # Gross margin rate column creation

    df['gross_margin_rate'] = (df['revenue_generated'] - df['costs']) / df['revenue_generated']

    print('Data processed, writing to database...')

    # connect to SQLite and write the DataFrame to a table
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql('supply_chain_data', conn, if_exists='replace', index=False)
        conn.commit()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        conn.close()

    print('Data written to database successfully.')
if __name__ == '__main__':
    csv_to_sql()
