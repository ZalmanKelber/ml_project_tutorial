import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model
    path = 'app/server/artifacts/'
    with open(path + 'bangalore_housing_columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open(path + 'bangalore_housing_predictions.pickle', 'rb') as f:
        __model = pickle.load(f)

def get_location_names():
    if __locations is None:
        load_saved_artifacts()
    return __locations

def get_predicted_price(bedrooms, square_feet, bathrooms, location):
    if __data_columns is None or __model is None:
        load_saved_artifacts()
    location = location.strip().lower()
    print('DATA')
    print(bedrooms, bathrooms, location, square_feet)
    loc_index = __data_columns.index(location) if location in __data_columns else -1
    x = np.zeros(len(__data_columns))
    x[0], x[1], x[2] = bedrooms, square_feet, bathrooms
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

if __name__ == '__main__':
    load_saved_artifacts()