import pandas as pd

def filter_data(df: pd.DataFrame, state: str = None, categories: list = None) -> pd.DataFrame:
    """
    Filters the DataFrame by state and one-hot-encoded categories. 
    Only keeps rows where ALL selected categories are present (==1).

    Parameters:
    - df (pd.DataFrame): The full Yelp dataset.
    - state (str): Two-letter state code to filter by (e.g., 'CA').
    - categories (list of str): One-hot-encoded category columns to restrict by.

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    if state:
        df = df[df['state'] == state]

    if categories:
        valid_categories = [cat for cat in categories if cat in df.columns]
        for cat in valid_categories:
            df = df[df[cat] == 1]

    return df
