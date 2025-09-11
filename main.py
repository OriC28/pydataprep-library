from pydataprep import cleaning as cl
from pydataprep import preprocessing as pr
import pandas as pd


df = pd.read_excel("./data/datacategories.xlsx")

# print(cl.remove_duplicates(df))
print(pr.encode_categorical(df[["Equipo"]], "one_hot"))
