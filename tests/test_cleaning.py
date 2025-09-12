from unittest import TestCase
import pandas as pd

from pydataprep.cleaning import handle_missing_values, remove_duplicates


class TestCleaning(TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Pamela', 'Raúl', 'José'], 'Edad': [None, 14, 26], 'Sexo': [
            'Femenino', 'Masculino', 'Masculino'], 'Ciudad': [None, 'Punto Fijo', None]})
        return super().setUp()

    def test_drop_rows(self):
        df_expected = pd.DataFrame({'ID': 2, 'Nombre': 'Raúl', 'Edad': 14.0,
                                    'Sexo': 'Masculino', 'Ciudad': 'Punto Fijo'}, index=[1])
        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'drop_rows'), df_expected)

    def test_drop_cols(self):
        df_expected = pd.DataFrame({'ID': [1, 2, 3],
                                    'Nombre': ['Pamela', 'Raúl', 'José'],
                                    'Sexo': ['Femenino', 'Masculino', 'Masculino']})
        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'drop_cols'), df_expected)

    def test_fill_null_values(self):
        df_expected = pd.DataFrame({'ID': [1, 2, 3], 'Nombre': ['Pamela', 'Raúl', 'José'], 'Edad': ['any_value', 14.0, 26.0], 'Sexo': [
                                   'Femenino', 'Masculino', 'Masculino'], 'Ciudad': ['any_value', 'Punto Fijo', 'any_value']})

        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'any_value'), df_expected)

    def test_fill_null_values_mean(self):
        df_expected = self.df.copy()
        df_expected['Edad'] = df_expected['Edad'].fillna(20.0)

        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'mean'), df_expected)
