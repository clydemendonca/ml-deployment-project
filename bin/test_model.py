"""Module to handle all prediction-related functionality."""
import json
import pickle


class Test:
    """Class to handle all prediction-related functionality."""

    def __init__(self):
        """Set model filename as class variable."""
        config = json.load(open('./config/config.json'))
        self.model_filename = config['app']['model']['filename']

    def load_model(self):
        """Load model from pickle file."""
        self.model = pickle.load(open('./models/' + self.model_filename, 'rb'))

    def predict(self,
                clump_thickness,
                unif_cell_size,
                unif_cell_shape,
                marg_adhesion,
                single_epith_cell_size,
                bare_nuclei,
                bland_chrom,
                norm_nucleoli,
                mitoses
                ):
        """Predict cancer type for parameters."""
        return self.model.predict([[
            clump_thickness,
            unif_cell_size,
            unif_cell_shape,
            marg_adhesion,
            single_epith_cell_size,
            bare_nuclei,
            bland_chrom,
            norm_nucleoli,
            mitoses
        ]])
