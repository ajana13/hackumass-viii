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
    dict = {}
    for i in range(0, len(stats_dict['Enter the Information'])):
        dict[stats_dict['Enter the Information'][i]] = int_features[i] 
        print(stats_dict['Enter the Information'][i])
    jsonOutput = dict
    return render_template('predict.html', output=jsonOutput, prediction=prediction[0][1]*100)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)