from ingestion import download_csv
from cleaning import clean_tips_data
from database import save_to_sqlite
from queries import run_query

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
CSV_PATH = "data/tips.csv"
DB_PATH="data/tips.db"

def main():
    df = download_csv(URL,CSV_PATH)
    df = clean_tips_data(df)
    df.to_csv("data/tips_cleaned.csv", index=False)
    save_to_sqlite(df, db_path=DB_PATH)
    query="""
    SELECT day, ROUND(AVG(total_bill),2) AS avg_bill
    FROM tips
    GROUP BY day;
"""
    result = run_query(db_path=DB_PATH, query=query)
    print(result)

if __name__ == "__main__":
    main()
    