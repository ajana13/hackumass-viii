from flask import Flask, request, render_template, url_for, jsonify, redirect
import json
import api 
from tensorflow import keras
import numpy as np

app = Flask(__name__)

with open('input.json', 'r') as f:
    stats_dict = json.load(f)
print(stats_dict)

model = keras.models.load_model('model.tf')

defaultVal = {}
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', stats_dict=stats_dict)

@app.route("/predict", methods=['POST'])
def pred():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array([np.array(int_features)])
    prediction = model.predict(final_features)
    jsonOutput = {
        "data1":5
    }

        #output = round(prediction[0], 2)
    return render_template('predict.html', output=jsonOutput, prediction=prediction[0][1]*100)
    #     data1 = request.form.get("data1")
    #     jsonOutput = {
    #         "data1":data1
    #     }
    #     # TO DO
    #     # Need to preprocess the input data in the same manner as the training data
    #     df = api.json_to_df(jsonOutput)
    #     # Load the model and then predict
    #     # model = pickle.load(open("", "rb"))
    #     result = model.predict_proba(df)
    #     val = round(float(list(result)[0][0]),2)
    # return render_template('predict.html', output=jsonOutput, prediction=val)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)