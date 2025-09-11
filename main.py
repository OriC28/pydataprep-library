from pydataprep import cleaning as cl
from pydataprep import preprocessing as pr
import pandas as pd


df = pd.read_excel("./data/data.xlsx")

# print(cl.remove_duplicates(df))
print(pr.encode_categorical(df["Grupo de clientes"], "label"))
