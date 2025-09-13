from unittest import TestCase
import pandas as pd
import numpy as np

from pydataprep.preprocessing import encode_categorical, scale_numerical


class TestPreprocessing(TestCase):
    def setUp(self):
        """Prepare a clean DataFrame for each test."""
        self.df = pd.DataFrame({'Animal': [
                               'Dog', 'Cat', 'Bird', 'Dog', 'Fish']})

        self.df_test = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['Pamela', 'Raúl', 'José', 'Ana'], 'Age': [np.nan, 14, 26, 14], 'Sex': [
            'Feminine', 'Masculine', 'Masculine', 'Feminine'], 'City': [np.nan, 'Paris', np.nan, np.nan]})

        return super().setUp()

    def test_encode_categorical_one_hot(self):
        """Tests that categorical variables are correctly encoded using one-hot encoding."""
        df_expected = pd.DataFrame({'Animal_Bird': [0.0, 0.0, 1.0, 0.0, 0.0], 'Animal_Cat': [
                                   0.0, 1.0, 0.0, 0.0, 0.0], 'Animal_Dog': [1.0, 0.0, 0.0, 1.0, 0.0], 'Animal_Fish': [0.0, 0.0, 0.0, 0.0, 1.0]})
        pd.testing.assert_frame_equal(
            encode_categorical(self.df.copy()), df_expected)

    def test_encode_categorical_label(self):
        """Tests that categorical variables are correctly encoded using label encoding."""
        def_expected = pd.DataFrame({'Category': [2, 1, 0, 2, 3]})

        pd.testing.assert_frame_equal(
            encode_categorical(self.df.copy(), 'label'), def_expected)

    def test_scale_numerical_min_max(self):
        """ Tests that numerical variables are correctly scaled using min-max normalization."""
        df_expected = self.df_test.copy()
        df_expected['Age'] = [np.nan, 0.0, 1.0, 0.0]

        pd.testing.assert_frame_equal(scale_numerical(
            self.df_test, ['Age']), df_expected)

    def test_scale_numerical_standard(self):
        """Tests that numerical variables are correctly scaled using standardization."""
        df_expected = self.df_test.copy()
        df_expected['Age'] = [np.nan, -0.707107, 1.414214, -0.707107]

        pd.testing.assert_frame_equal(scale_numerical(
            self.df_test, ['Age'], 'standard'), df_expected)

    def test_scale_numerical_not_supported_technique(self):
        """Tests that unsupported scaling techniques raise appropriate errors."""
        self.assertRaises(ValueError, scale_numerical,
                          self.df_test, ['Age'], 'robust_scaler')

    def test_scale_numerical_column_not_found(self):
        """Tests that attempting to scale a non-existent column raises an error."""
        self.assertRaises(ValueError, scale_numerical,
                          self.df_test, ['AnyColumn'], 'standard')
