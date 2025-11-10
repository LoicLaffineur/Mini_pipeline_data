import pandas as pd 

def clean_tips_data(df: pd.DataFrame) -> pd.DataFrame : 
    df = df.dropna()  # Remove rows with missing values
    df = df[df['total_bill'] > 0]  # Keep only rows with positive total_bill
    df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100  # Add tip percentage column
    return df
