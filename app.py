from model.features import URLFeatures
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['text']
    
    features = vectorizer.transform([data])
    prediction = model.predict(features)[0]

    result = "Phishing ⚠️" if prediction == 1 else "Safe ✅"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)