from pydataprep import cleaning as cl
from pydataprep import preprocessing as pr
import pandas as pd
import numpy as np

df = pd.read_excel("./data/datatest.xlsx")

# print(cl.handle_missing_values(df, 99))
# print(pr.encode_categorical(df["Grupo de clientes"], "label"))
# df = cl.handle_missing_values(df, "drop_cols")
# dfx = pr.scale_numerical(df, ["Edad"], "min_max")
# print(dfx)
# print(np.std(dfx["Edad"]))

""" print(cl.handle_missing_values(df, 'drop_cols'))
dfx = pd.DataFrame({'ID': [1, 2, 3],
                    'Nombre': ['Pamela', 'Raúl', 'José'],
                    'Sexo': ['Femenino', 'Masculino', 'Masculino']})
print(dfx.equals(cl.handle_missing_values(df, 'drop_cols')))
 """

print(cl.handle_missing_values(df, 'mean'))
