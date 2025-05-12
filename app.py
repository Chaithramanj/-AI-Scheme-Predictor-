from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)  # ✅ Correct usage

# Load the trained model
model = joblib.load('scheme_predictor_model.pkl')

# Dictionary of schemes and their URLs
scheme_urls = {
    "PMAY": "https://www.pfrda.org.in/myauth/admin/showimg.cshtml?ID=870",
    "PMMY": "https://www.mudra.org.in/",
    "Ayushman Bharat Scheme": "https://www.myscheme.gov.in/schemes/ab-pmjay",
    "DOTEL": "https://dot.gov.in/",
    # Add more schemes and URLs here
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    description = request.form['description']
    prediction = model.predict([description])[0]
    scheme = prediction.strip()
    url = scheme_urls.get(scheme, None)
    return jsonify({'scheme': scheme, 'url': url})

if __name__ == '__main__':  # ✅ Correct usage
    app.run(debug=True)
