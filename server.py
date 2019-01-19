"""Flask App."""
import flask
import json
from flask import Flask
from flask import request
from bin.train_model import Train
from bin.test_model import Test

app = Flask(__name__)


@app.route('/train', methods=['GET'])
def train_model():
    """API to create a model in /models directory."""
    train = Train()
    train.build_model()
    return "Model is created"


@app.route('/predict', methods=['POST'])
def predict():
    """API to predict the type of cancer for given parameters."""
    body_params = dict(request.json)

    clump_thickness = body_params['clump_thickness']
    unif_cell_size = body_params['unif_cell_size']
    unif_cell_shape = body_params['unif_cell_shape']
    marg_adhesion = body_params['marg_adhesion']
    single_epith_cell_size = body_params['single_epith_cell_size']
    bare_nuclei = body_params['bare_nuclei']
    bland_chrom = body_params['bland_chrom']
    norm_nucleoli = body_params['norm_nucleoli']
    mitoses = body_params['mitoses']

    test = Test()
    test.load_model()
    prediction = test.predict(
        clump_thickness,
        unif_cell_size,
        unif_cell_shape,
        marg_adhesion,
        single_epith_cell_size,
        bare_nuclei,
        bland_chrom,
        norm_nucleoli,
        mitoses
    )

    print(prediction)
    return "Cancer is class %d" % prediction[0]


if __name__ == "__main__":
    config = json.load(open('./config/config.json'))
    app.run(host="0.0.0.0", port=config['app']['port'])
