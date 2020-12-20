from flask import Flask, request, render_template, url_for, jsonify, redirect
import json
import api 

app = Flask(__name__)

with open('input.json', 'r') as f:
    stats_dict = json.load(f)
print(stats_dict)

defaultVal = {}
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', stats_dict=stats_dict)

@app.route("/predict", methods=['GET','POST'])
def pred():
    if request.method == 'POST':
        data1 = request.form.get("data1")
        jsonOutput = {
            "data1":data1
        }
        # TO DO
        # Need to preprocess the input data in the same manner as the training data
        df = api.json_to_df(jsonOutput)
        # Load the model and then predict
        # model = pickle.load(open("", "rb"))
        result = model.predict_proba(df)
        val = round(float(list(result)[0][0]),2)
    return render_template('predict.html', output=jsonOutput, prediction=val)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)