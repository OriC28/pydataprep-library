from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


def encode_categorical(df: pd.DataFrame, method: str):
    """"Applies one-hot or label-ending encoding to transform categorical variables into a numeric format"""
    if method == "one_hot":
        encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        encoded_items = encoder.fit_transform(df)
        return pd.DataFrame(encoded_items, columns=encoder.get_feature_names_out(df.columns))
    elif method == "label":
        encoder = LabelEncoder()
        encoded_data = encoder.fit_transform(df.values.ravel())
        return pd.DataFrame({"Category": encoded_data})
    else:
        return "Method not supported."


def scale_numerical(df: pd.DataFrame, columns: list, technique: str):
    """Applies the numeric feature scale to a specific set of columns"""
    pass
