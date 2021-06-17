from flask import Flask,jsonify,request
from main import getPrediction

app = Flask(__name__)

@app.route('/predict-digit',methods=["post"])
def predictData():
    img = request.files.get("digit")
    pred = getPrediction(img)
    return jsonify({
        "prediction" : pred,
    }),200

if __name__ == '__main__':
    app.run(debug=True)