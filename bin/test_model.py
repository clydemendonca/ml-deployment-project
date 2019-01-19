import json
import pickle

class Test:

    def __init__(self):
        config = json.load(open('./config/config.json'))
        self.model_filename = config['app']['model']['filename']

    def load_model(self):
        self.model = pickle.load(open('./models/' + self.model_filename, 'rb'))

    def predict(self, clump_thickness, unif_cell_size, unif_cell_shape,	marg_adhesion, single_epith_cell_size, bare_nuclei, bland_chrom, norm_nucleoli, mitoses):
        return self.model.predict([[clump_thickness, unif_cell_size	, unif_cell_shape, marg_adhesion,
                            single_epith_cell_size,	bare_nuclei, bland_chrom, norm_nucleoli, mitoses]])
