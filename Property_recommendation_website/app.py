from flask import Flask, render_template, request, url_for
import pandas as pd
from sklearn.metrics.pairwise import haversine_distances
from math import radians
import sqlite3

app = Flask(__name__)


connection = sqlite3.connect('proj4_grp2.sqlite')
data = pd.read_sql_query("SELECT * FROM realestate_info where state = 'AZ'", connection)

def get_similar_nearby_properties(ref_latitude, ref_longitude, ref_bedroom_number, 
                                  ref_bathroom_number, ref_price, data, max_distance_km=10,
                                  max_bedroom_number_diff=1, max_bathroom_number_diff=1, max_price_diff=50000):
    
    
    # Convert latitude and longitude from degrees to radians
    data['lat_rad'] = data['latitude'].apply(lambda x: radians(x))
    data['lon_rad'] = data['longitude'].apply(lambda x: radians(x))

    # Reference point in radians
    ref_point = [radians(ref_latitude), radians(ref_longitude)]

    # Haversine formula to calculate distances
    data['distance'] = haversine_distances(data[['lat_rad', 'lon_rad']].values, [ref_point]).reshape(-1) * 6371.0

    # Filter properties within the specified distance
    nearby_properties = data[data['distance'] <= max_distance_km]

    # Filter properties with similar number of bedrooms and price
    similar_properties = nearby_properties[
        (abs(nearby_properties['bedroom_number'] - ref_bedroom_number) <= max_bedroom_number_diff) &
        (abs(nearby_properties['bathroom_number'] - ref_bathroom_number) <= max_bathroom_number_diff) &
        (abs(nearby_properties['price'] - ref_price) <= max_price_diff)
    ]

    # Sort by distance
    similar_properties = similar_properties.sort_values(by='distance')

    return similar_properties

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    ref_latitude = float(request.form['latitude'])
    ref_longitude = float(request.form['longitude'])
    ref_bedrooms = int(request.form['bedrooms'])
    ref_bathrooms = int(request.form['bathrooms'])
    ref_price = float(request.form['price'])

    print("DEBUG", ref_latitude, ref_bedrooms)

    similar_nearby_properties = get_similar_nearby_properties(
        ref_latitude, ref_longitude, ref_bedrooms, ref_bathrooms, ref_price,
        data, max_distance_km=10, max_bedroom_number_diff=1,
        max_bathroom_number_diff=1, max_price_diff=50000,
    )

    return render_template('result.html', properties=similar_nearby_properties)

if __name__ == '__main__':
    app.run(debug=True)
