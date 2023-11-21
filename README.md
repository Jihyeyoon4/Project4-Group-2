# Project-Group-2
Jihye's Part
#This Python scri, get_similar_nearby_properties, is designed to find properties that are similar to a given reference property based on geographic location, number of bedrooms, number of bathrooms, and price. It utilizes the Haversine formula for calculating distances between geographical coordinates.
The Haversine formula is applied to calculate the distances between each property and the reference property.
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html

# get data from sql 
'''
connection = sqlite3.connect('proj4_grp2.sqlite')
data = pd.read_sql_query("SELECT * FROM realestate_info where state = 'AZ'", connection)
data.head()
'''


'''
def get_similar_nearby_properties(ref_latitude, ref_longitude, ref_bedroom_number, 
                                  ref_bathroom_number, ref_price, data, max_distance_km=10,
                                max_bedroom_number_diff=1, max_bathroom_number_diff=1, max_price_diff=50000):
  # Latitude and longitude values in the data DataFrame are converted from degrees to radians
   data['lat_rad'] = data['latitude'].apply(lambda x: radians(x))
    data['lon_rad'] = data['longitude'].apply(lambda x: radians(x))
  #Reference point in radians
    ref_point = [radians(ref_latitude), radians(ref_longitude)]  #Reference point in radians
    

   #The Haversine formula is applied to calculate the distances between each property and the reference property.
    data['distance'] = haversine_distances(data[['lat_rad', 'lon_rad']].values, [ref_point]).reshape(-1) * 6371.0

  #Properties within the specified maximum distance are filtered.
    nearby_properties = data[data['distance'] <= max_distance_km]
'''

# Find and display properties similar to a reference property based on specified criteria. 
'''
reference_latitude = 35.114260 #Latitude of the reference property.
reference_longitude = -114.618385 #Longitude of the reference property.
reference_bedrooms = 2  #Number of bedrooms in the reference property.
reference_bathrooms = 1 #Number of bathrooms in the reference property
reference_price = 54900 #Price of the reference property.

similar_nearby_properties = get_similar_nearby_properties(
    reference_latitude, reference_longitude, reference_bedrooms, reference_bathrooms, reference_price,
    data, max_distance_km=10, max_bedroom_number_diff=1, max_bathroom_number_diff=1, max_price_diff=50000
)
#The function returns the DataFrame of similar properties.
print("Similar Nearby Properties:")
print(similar_nearby_properties[['property_id', 'latitude', 'longitude', 'distance', 'bedroom_number', 'bathroom_number', 'living_space', 'price']])
'''
