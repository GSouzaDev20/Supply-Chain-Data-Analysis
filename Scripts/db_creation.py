import sqlite3
import pandas as pd
from pathlib import Path

def csv_to_sql():

    print('Reading CSV Path...')

    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR / 'Raw_Data' / 'supply_chain_data_RAW.csv'
    db_path = BASE_DIR / 'DB' / 'supply_chain.db'

    if not csv_path.exists():
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
    db_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure the DB directory exists
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
