from pydataprep import cleaning as cl
import pandas as pd


df = pd.read_excel("./data/datatest.xlsx")
data = df.loc[1]
header = list(df.columns.values)

print(cl.remove_duplicates(df))
