from pydataprep.cleaning import handle_missing_values
import pandas as pd

df = pd.read_excel("./data/datatest.xlsx")

# Remove all rows with at least one null value
df1 = handle_missing_values(df, 'drop_rows')

# Remove all columns with al least one null value
df2 = handle_missing_values(df, 'drop_cols')

# Fill all null values with specified value
df3 = handle_missing_values(df, 'any_value')

# Replace all null values with the column average
df_mean = handle_missing_values(df, 'mean')

# Replace all null values with the column median
df_median = handle_missing_values(df, 'median')

# Replace all null values with the column mode
df_mode = handle_missing_values(df, 'mode')
