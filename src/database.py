import sqlite3
import pandas as pd

def save_to_sqlite(df:pd.DataFrame, db_path:str, table_name:str='tips'):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn,if_exists='replace',index=False)
    conn.close()
    print(f"Données stockées dans {db_path}({table_name})")