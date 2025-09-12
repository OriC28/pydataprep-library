from unittest import TestCase
import pandas as pd
import numpy as np

from pydataprep.cleaning import handle_missing_values, remove_duplicates


class TestCleaning(TestCase):

    def setUp(self):
        """Prepare a clean DataFrame for each test."""
        self.df = pd.DataFrame({'ID': [1, 2, 3, 4], 'Nombre': ['Pamela', 'Raúl', 'José', 'Ana'], 'Edad': [np.nan, 14, 26, 14], 'Sexo': [
            'Femenino', 'Masculino', 'Masculino', 'Femenino'], 'Ciudad': [np.nan, 'Punto Fijo', np.nan, np.nan]})
        return super().setUp()

    def test_drop_rows_with_nulls(self):
        """Verifies that rows with null values ​​are deleted correctly."""
        df_expected = pd.DataFrame(self.df[self.df['Nombre'] == 'Raúl'])
        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'drop_rows'), df_expected)

    def test_drop_cols_with_nulls(self):
        """Verifies that columns with null values ​​are deleted correctly."""
        df_expected = self.df.copy()
        df_expected = df_expected.drop(['Edad', 'Ciudad'], axis=1)
        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'drop_cols'), df_expected)

    def test_fill_with_custom_value(self):
        """Verify that nulls are replaced with a custom value."""
        df_expected = self.df.copy()
        df_expected = df_expected.fillna('any_value')

        pd.testing.assert_frame_equal(
            handle_missing_values(self.df, 'any_value'), df_expected)

    def test_statistical_strategies_ignores_non_numeric_cols(self):
        """Verifies that the statistical strategies do not alter non-numeric columns."""
        df_test = self.df.copy()
        df_test['Edad'] = [np.nan]*len(df_test['ID'])

        for strategy in ['mean', 'median', 'mode']:
            with self.subTest(strategy=strategy):
                pd.testing.assert_frame_equal(
                    handle_missing_values(df_test, strategy), df_test)

    def test_fill_numeric_with_statistical_strategies(self):
        """Test that nulls are filled correctly with statistical strategies (mean, median, mode)."""
        strategies_to_test = [
            ('mean', 18.0),
            ('median', 14.0),
            ('mode', 14.0)
        ]

        for strategy, expected_value in strategies_to_test:
            with self.subTest(strategy=strategy):
                df_expected = self.df.copy()
                df_expected['Edad'] = df_expected['Edad'].fillna(
                    expected_value)

                result_df = handle_missing_values(self.df, strategy)

                print(f"\nTesting strategy: '{strategy}'")
                pd.testing.assert_frame_equal(result_df, df_expected)

    def test_drop_strategy_raises_error_on_clean_df(self):
        """Verify that an error is thrown if you try to delete nulls in a clean DF."""
        df_expected = self.df.copy()
        df_expected = df_expected.fillna(0)
        self.assertRaises(ValueError, handle_missing_values, df_expected)
