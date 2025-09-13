import pandas as pd


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop_rows") -> pd.DataFrame:
    """Handling null values ​​according to the provided strategy. Default strategy 'drop_rows'.

        Args:
            df (DataFrame): Dataframe object
            strategy (str): Strategy to use

        Returns:
            New DataFrame object
    """

    if df.isna().sum().sum() == 0:
        raise ValueError("No missing values found to handle.")

    if strategy == "drop_rows":
        return df.dropna()
    elif strategy == "drop_cols":
        return df.dropna(axis=1)

    df_final = df.copy()
    numeric_types = ['float64', 'int64']

    if strategy in ['mean', 'median', 'mode']:
        for col in df_final.columns:
            if df_final[col].dtype in numeric_types and df_final[col].isnull().any():
                if not df_final[col].dropna().empty:
                    fill_value = None
                    if strategy == 'mean':
                        fill_value = df_final[col].mean()
                    elif strategy == 'median':
                        fill_value = df_final[col].median()
                    elif strategy == 'mode':
                        fill_value = df_final[col].mode().iloc[0]

                    df_final[col] = df_final[col].fillna(fill_value)
        return df_final

    return df.fillna(strategy)


def remove_duplicates(df: pd.DataFrame) -> str:
    """Removes duplicate values ​​found

       Args:
            df (DataFrame): Dataframe object

       Returns:
            str: Number of duplicates removed
    """
    df_without_duplicates = df.drop_duplicates()
    duplicates_removed = len(df) - len(df_without_duplicates)
    return f"Number of duplicates removed: {duplicates_removed}"
