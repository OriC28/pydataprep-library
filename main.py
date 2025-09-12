from pydataprep import cleaning as cl
from pydataprep import preprocessing as pr
import pandas as pd
import numpy as np

df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Nombre': ['Pamela', 'Raúl', 'José', 'Ana'], 'Edad': [np.nan, 14, 26, 14], 'Sexo': [
    'Femenino', 'Masculino', 'Masculino', 'Femenino'], 'Ciudad': [np.nan, 'Punto Fijo', np.nan, np.nan]})
