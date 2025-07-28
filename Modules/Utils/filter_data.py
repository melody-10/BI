import pandas as pd

def filter_data(df: pd.DataFrame, state: str = None, category: str = None) -> pd.DataFrame:
    """
    Filters the DataFrame by state and/or business category.

    Parameters:
    - df (pd.DataFrame): The full Yelp dataset.
    - state (str): Two-letter state code to filter by (e.g., 'CA').
    - category (str): One-hot-encoded category column name (e.g., 'Restaurants').

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    if state:
        df = df[df['state'] == state]

    if category and category in df.columns:
        df = df[df[category] == 1]

    return df
