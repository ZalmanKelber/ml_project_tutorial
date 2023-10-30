from flask import Flask, request, jsonify
import util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
@cross_origin()
def get_predict_home_price():
    bedrooms = int(request.data.get('bedrooms'))
    bathrooms = int(request.data.get('bathrooms'))
    square_feet = float(request.data.get('square_feet'))
    location = request.data.get('location')
    price = util.get_predicted_price(bedrooms, square_feet, bathrooms, location)
    response = jsonify({
        'price_prediction': price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting Flask server')
    app.run(port=8000, debug=True)