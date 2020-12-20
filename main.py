from flask import Flask, request, render_template, url_for, jsonify, redirect
import json
import api 
from tensorflow import keras
import numpy as np

app = Flask(__name__)

# stats_dict - the top 15 selected features/stats 
with open('input.json', 'r') as f:
    stats_dict = json.load(f)

# load the saved model
model = keras.models.load_model('model.tf')

# default page or Home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', stats_dict=stats_dict)

# prediction page
@app.route("/predict", methods=['POST'])
def pred():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array([np.array(int_features)])
    prediction = model.predict(final_features)
    dict = {}
    # Make a dictionary object with the keys as the data heading of the top 15 features
    for i in range(0, len(stats_dict['Enter the Information'])):
        dict[stats_dict['Enter the Information'][i]] = int_features[i] 
    jsonOutput = dict
    # render the prediction as a percentage
    out = round(prediction[0][1]*100,5)
    return render_template('predict.html', output=jsonOutput, prediction=out)

# about page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)