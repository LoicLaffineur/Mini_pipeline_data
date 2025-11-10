import pandas as pd 
from pathlib import Path

def download_csv(url: str, save_path:str) -> pd.DataFrame:
    """Downloads a CSV file from a given URL and saves it to the specified path.

    Args:
        url (str): The URL of the CSV file to download.
        save_path (str): The local path where the CSV file will be saved.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the downloaded CSV file.
    """
    df = pd.read_csv(url)
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(save_path, index=False)
    print("CSV file downloaded and saved to", save_path)
    return df