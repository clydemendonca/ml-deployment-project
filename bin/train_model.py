"""Module to handle building and saving model."""
import json
import pandas as pd
from bin.helpers.preprocessor import Preprocessor
from sklearn.linear_model import LogisticRegression
import pickle


class Train:
    """Class to handle all functions which ensure building and saving model."""

    def __init__(self):
        """Get filenames for data and model files."""
        config = json.load(open('./config/config.json'))
        self.data_filename = config['app']['data']['filename']
        self.model_filename = config['app']['model']['filename']

    def build_model(self):
        """Build the model and save it in respective directory."""
        df = pd.read_csv('./data/' + self.data_filename)

        preprocessor = Preprocessor(df)
        preprocessor.remove_urequired_columns(['id'])
        X, y = preprocessor.get_x_and_y('class')

        model = LogisticRegression()
        model.fit(X, y)

        pickle.dump(model, open('./models/' + self.model_filename, 'wb'))
