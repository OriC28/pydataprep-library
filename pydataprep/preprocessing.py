from sklearn.preprocessing import OneHotEncoder, LabelEncoder, MinMaxScaler, StandardScaler
import pandas as pd


def encode_categorical(df: pd.DataFrame, method: str = "one_hot") -> pd.DataFrame:
    """"Applies one-hot or label-ending encoding to transform categorical variables into a numeric format. Default method 'one_hot'

        Args:
            df (DataFrame): Dataframe object
            method (str): Encoding method

        Returns:
            New DataFrame object
    """

    if method == "one_hot":
        encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        encoded_items = encoder.fit_transform(df)
        return pd.DataFrame(encoded_items, columns=encoder.get_feature_names_out(df.columns))

    elif method == "label":
        encoder = LabelEncoder()
        encoded_data = encoder.fit_transform(df.values.ravel())
        return pd.DataFrame({"Category": encoded_data})

    raise ValueError("Method not supported.")


def scale_numerical(df: pd.DataFrame, columns: list, technique: str = "min_max") -> pd.DataFrame:
    """Applies the numeric feature scale to a specific set of columns. Default technique 'min_max'.

        Args:
            df (DataFrame): Dataframe object
            columns (list): List of columns to be scaled
            technique (str): Scaling technique

        Returns:
            DataFrame object with scaled columns
    """

    # Create object instance
    scaler = MinMaxScaler() if technique == "min_max" else StandardScaler()

    # Validate if technique is supported
    if technique not in ["min_max", "standard"]:
        raise ValueError("Technique not supported.")

    # Start scaled and transform data
    for column in columns:
        if column not in df.columns.values:
            raise ValueError(
                "Column not found. Try to set a column name that exists.")
        scaled = scaler.fit_transform(
            df[column].values.ravel().reshape(-1, 1))
        df[column] = scaled
    return df
