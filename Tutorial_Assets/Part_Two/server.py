import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('sales_model.pkl', 'rb'))

@app.route("/")
def home_endpoint():
    return "My Deployed Model App!"

@app.route('/predict',methods=['POST'])
def predict():

    data = request.get_json(force=True)
    values = [np.array(list(data.values()))]
    prediction = model.predict(values)
    output = round(prediction[0], 2)

    return jsonify({'Prediction': output})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
    
    