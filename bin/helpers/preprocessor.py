import pandas as pd
from sklearn.model_selection import train_test_split

class Preprocessor:

    def __init__(self, df):
        self.df = df

    def remove_urequired_columns(self, unrequired_columns):
        self.df = self.df.drop(columns=unrequired_columns)

    def get_x_and_y(self, y_column):
        X = self.df.drop(columns=[y_column])
        y = self.df[y_column]
        return X, y

