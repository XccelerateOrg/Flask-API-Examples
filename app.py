from flask import Flask ,jsonify ,request

app = Flask(__name__)

@app.route("/predict",methods=["POST"])
def predict():
    print(request.form.get('test'))
    return jsonify({"abc":1234})
