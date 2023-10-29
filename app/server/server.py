from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def get_predict_home_price():
    print('TESTING')
    print(request.form.get('bedrooms'))
    bedrooms = int(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    square_feet = float(request.form.get('square_feet'))
    location = request.form.get('location')
    response = jsonify({
        'price_prediction': util.get_predicted_price(bedrooms, square_feet, bathrooms, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting Flask server')
    app.run(port=8000, debug=True)