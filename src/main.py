from ingestion import download_csv
from cleaning import clean_tips_data

URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
CSV_PATH = "data/tips.csv"

def main():
    df = download_csv(URL,CSV_PATH)
    df = clean_tips_data(df)
    df.to_csv("data/tips_cleaned.csv", index=False)

if __name__ == "__main__":
    main()
    