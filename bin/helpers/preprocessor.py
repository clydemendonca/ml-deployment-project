"""Helper to preprocess data."""
import pandas as pd
from sklearn.model_selection import train_test_split


class Preprocessor:
    """Class to handle preprocessing operations."""

    def __init__(self, df):
        """Set DataFrame as class variable."""
        self.df = df

    def remove_urequired_columns(self, unrequired_columns):
        """Remove columns that are not required."""
        self.df = self.df.drop(columns=unrequired_columns)

    def get_x_and_y(self, y_column):
        """Split X and y."""
        X = self.df.drop(columns=[y_column])
        y = self.df[y_column]
        return X, y
