import pandas as pd

def filter_data(df: pd.DataFrame, state: str = None, categories: list = None) -> pd.DataFrame:
    """
    Filters the DataFrame by state and/or one-hot-encoded business categories.

    Parameters:
    - df (pd.DataFrame): The full Yelp dataset.
    - state (str): Two-letter state code to filter by (e.g., 'CA').
    - categories (list of str): One or more one-hot-encoded category column names.

    Returns:
    - pd.DataFrame: Filtered DataFrame.
    """
    if state:
        df = df[df['state'] == state]

    if categories:
        # Ensure all categories are valid column names
        valid_categories = [cat for cat in categories if cat in df.columns]
        if valid_categories:
            df = df[df[valid_categories].sum(axis=1) > 0]

    return df
