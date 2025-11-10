import sqlite3
import pandas as pd

def run_query(db_path:str, query: str) -> pd.DataFrame : 
    with sqlite3.connect(db_path) as conn : 
        return pd.read_sql_query(query,conn)
