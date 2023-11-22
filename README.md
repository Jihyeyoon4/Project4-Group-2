# Project-Group-2
Housing Prediction
#Jihye's Part
#This Python script, get_similar_nearby_properties, is designed to find properties that are similar to a given reference property based on geographic location, number of bedrooms, number of bathrooms, and price. It utilizes the Haversine formula for calculating distances between geographical coordinates.

The Haversine formula is applied to calculate the distances between each property and the reference property.
[Learn more] (https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html)
Used Silhouette Score to evaluate the machine
[Learn more](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)

```python
connection = sqlite3.connect('proj4_grp2.sqlite')
data = pd.read_sql_query("SELECT * FROM realestate_info where state = 'AZ'", connection)
data.head()
```

```python
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
```

# Find and display properties similar to a reference property based on specified criteria. 
```python
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
```
# select columns for clustering
```python
numeric_dataset=data[['latitude','longitude','bedroom_number','bathroom_number','price']]
```
# Find K value
```python
inertia = []
k = list(range(1, 11))
for i in k:
    k_model = KMeans(n_clusters=i, random_state=1)
    k_model.fit(numeric_dataset)
    inertia.append(k_model.inertia_)
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)

# Review the DataFrame
df_elbow.head()
df_elbow.hvplot.line(
    x="k", 
    y="inertia", 
    title="Elbow Curve", 
    xticks=k
)
```python
#Since the data we have is High-Dimensional Data, we use PCA to reduce the dimensionality by capturing the most important variations in the data.
# Features for clustering
features_for_clustering = numeric_dataset[['latitude', 'longitude', 'bedroom_number', 'bathroom_number', 'price']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=1)
y = kmeans.fit_predict(features_for_clustering)
numeric_dataset['Cluster'] = y

# Apply PCA for dimensionality reduction to 2D
pca = PCA(n_components=2)
pca_result = pca.fit_transform(features_for_clustering)

# Create a 2D scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=numeric_dataset['Cluster'], cmap='viridis', alpha=0.8)
plt.title('KMeans Clustering - 2D Scatter Plot (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Cluster')
plt.show()
```

# Try with n_clusters=3 as well
```python
# Features for clustering
features_for_clustering = numeric_dataset[['latitude', 'longitude', 'bedroom_number', 'bathroom_number', 'price']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=1)
y = kmeans.fit_predict(features_for_clustering)
numeric_dataset['Cluster'] = y

# Apply PCA for dimensionality reduction to 2D
pca = PCA(n_components=2)
pca_result = pca.fit_transform(features_for_clustering)

# Create a 2D scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=numeric_dataset['Cluster'], cmap='viridis', alpha=0.8)
plt.title('KMeans Clustering - 2D Scatter Plot (PCA)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Cluster')
plt.show()
```
## 3 has more distict seperation and the data is grouped in clear property information segments.

# evaluate a model with Silhouette Score [-1:1]
```python
from sklearn.metrics import silhouette_score, calinski_harabasz_score
silhouette_avg = silhouette_score(features_for_clustering, numeric_dataset['Cluster'])
print(f"Silhouette Score: {silhouette_avg}")

```
Erjola's Part



