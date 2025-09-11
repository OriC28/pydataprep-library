import pandas as pd
import numpy as np


def handle_missing_values(df: pd.DataFrame, strategy: str):
    """Handling null values ​​according to the provided strategy"""

    df_final = None
    values_rows_sum = df.isna().sum()
    types = [np.float64, np.int64]

    # Validate if values null exists
    if (sum(values_rows_sum) == 0):
        raise ValueError("No missing values.")

    # Dropping rows or columns with null values
    if strategy == "drop_rows":
        return df.dropna()

    elif strategy == "drop_cols":
        return df.dropna(axis=1)

    df_final = df.copy()

    # Statistical calculations
    match(strategy):
        case "mean":
            for column in df_final.columns:
                if df[column].dtypes in types:
                    df_final[column] = df[column].fillna(df[column].mean())
        case "median":
            for column in df_final.columns:
                if df[column].dtypes in types:
                    df_final[column] = df[column].fillna(df[column].median())
        case "mode":
            df_final = df.mode()

    return df_final


def remove_duplicates(df: pd.DataFrame):
    """Removes duplicate values ​​found"""
    pass
