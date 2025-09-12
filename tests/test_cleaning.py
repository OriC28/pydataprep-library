from unittest import TestCase
import pandas as pd

from pydataprep.cleaning import handle_missing_values, remove_duplicates

df = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Pamela', 'Raúl', 'José'], 'Edad': [None, 14, 26], 'Sexo': [
    'Femenino', 'Masculino', 'Masculino'], 'Ciudad': [None, 'Punto Fijo', None]})


class TestCleaning(TestCase):
    def test_drop_rows(self):
        df_expected = pd.DataFrame({'ID': 2, 'Nombre': 'Raúl', 'Edad': 14.0,
                                    'Sexo': 'Masculino', 'Ciudad': 'Punto Fijo'}, index=[1])
        pd.testing.assert_frame_equal(
            handle_missing_values(df, 'drop_rows'), df_expected)

    def test_drop_cols(self):
        df_expected = pd.DataFrame({'ID': [1, 2, 3],
                                    'Nombre': ['Pamela', 'Raúl', 'José'],
                                    'Sexo': ['Femenino', 'Masculino', 'Masculino']})
        pd.testing.assert_frame_equal(
            handle_missing_values(df, 'drop_cols'), df_expected)
