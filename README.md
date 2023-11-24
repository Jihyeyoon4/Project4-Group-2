# Project-4-Group-2

## Overview 
This project focuses on the development of machine learning models for real estate applications, including price prediction, recommendation systems, and market analysis. Leveraging a dataset sourced from Kaggle, the objective is to create robust predictive models that can assist home buyers, sellers and real estate professionals in making informed decisions.

# Requirements
Sklearn, Python, SQLite, Matplotlib, Numpy

## Project Division

### Price Prediction

This section aims to predict real estate prices based on various features using machine learning. The project involves data cleaning, outlier removal, and utilizing a Random Forest Regressor model for price prediction and evaluated the model performance using R-squared (R2) scores and Mean Absolute Error (MAE).

1. Data Collection:
The dataset was sourced from Kaggle, providing comprehensive real estate information.

2. Data Cleaning:
Removed null values and unnecessary columns.
Handled data types and converted units for consistency.
Dropped rows with specific criteria (e.g., null values in 'price_per_unit').

3. Outlier Removal:
Identified and handled outliers using statistical methods.

4. Machine Learning Model: RandomForestRegressor:
Developed a machine learning model using the RandomForestRegressor algorithm.
Chose 'Price' as the target variable and 'Bedroom number,' 'Bathroom number,' 'Living space (sqft),' and 'City' as features.
Split the data into training and testing sets.
Trained the model on the training data.

5. Predictions and Evaluation:
Made predictions using the trained model on both training and testing data.
Evaluated the model performance using R-squared (R2) scores and Mean Absolute Error (MAE).

6. Results
- For a sample client input:
(Python code) client_input = pd.DataFrame({'bedroom_number': [3], 'bathroom_number': [2], 'living_space': [1500], 'city': ['Chino Valley']})

- The model provided the following results:
Predicted Price: $320,734.04 R-squared (R2) Score on Training Data: 0.9621 R-squared (R2) Score on Testing Data: 0.7621 Mean Absolute Error on Training Data: $40,150.86 Mean Absolute Error on Testing Data: $96,945.73

 - Price Prediction
This supervised learning task aims to understand the relationship between independent variables such as "city," "state," "latitude," "longitude," "price," "bedroom_number," "bathroom_number," "price_per_unit," "living_space," "land_space," "property_type," and the dependent variable, which is the price of the house. The objective is to predict the final price of each home using the following regression models: Linear Regression, Random Forest and Lasso Regression.

### Recommendation Systems

This model is designed to identify properties similar to a given reference property based on geographic location, number of bedrooms, number of bathrooms, and price. [https://github.com/Jihyeyoon4/Project4-Group-2/assets/135631517/cf1b539f-9114-46ec-8e69-7c2918d42066]


### Usage
```
1. def get_similar_nearby_properties(ref_latitude, ref_longitude, ref_bedroom_number, 
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

```
The Haversine formula is employed to compute the distances between each property and the reference property. Once properties located within the specified maximum distance are filtered, discover and showcase properties similar to a reference property based on the specified criteria(Bedroom, Bathroom, and Price)

4.Result

You can now get the list of properties’ information ('property_id', 'latitude', 'longitude', 'distance', 'bedroom_number','bathroom_number','living_space','price’.) by using print().
 

5.Validate a model

 Used Kmean(k=3) and since the data we have is multiple features data, I used PCA to reduce the dimensionality by capturing the most important variations in the data. And then, I clustered the feature to see the result. The data is grouped in clear property information segments.

6.Evaluation

Unsupervised learning models, which include clustering algorithms, don't have a clear notion of accuracy in the same way as supervised learning models do. However, we used ‘ Silhouette Score’ that measures how similar an object is to its own cluster compared to other clusters (separation). Higher Silhouette Scores generally indicate better-defined clusters. 
 
[https://github.com/Jihyeyoon4/Project4-Group-2/assets/135631517/70e200f5-5f6e-4ae4-a669-7ab40156e623]

### Market Analysis
This section of the project employs unsupervised machine learning techniques, specifically K-Means clustering, to identify trends, hotspots, and investment opportunities within the four states in the U.S.: Texas, California, Arizona, and Illinois. These states were selected due to being the states with the biggest amount of properties in the dataset.

1. Preprocessing
To enhance model performance and convergence speed, the data underwent normalization using StandardScaler.

2. K-Means Model and Elbow Method
The dataset was segmented into distinct clusters using the K-Means algorithm, which groups data points based on similarities. In the context of real estate, this segmentation helps categorize properties based on various features such as location, size, amenities, and price. The Elbow Method was employed to determine the optimal number of clusters for the data.

3. Results
Visualizations were created in the form of scatter plots for each state, showcasing the relationship between Living Space/Price and Bedroom Number/Price. The analysis of Living Space indicated that California and Texas predominantly have larger properties. Meanwhile, the Bedroom Number analysis revealed that most states typically feature properties with a standard number of bedrooms, typically ranging between 0 and 2.

### Investment Opportunities 

This section of the project aims to help investors to identify the best areas for investing in real state. For this, we used the Fred Economic Data to draw Line Charts and analyse key features from 2016 and 2022. 
Considering the feature of House Price, all four states appeared to have increase in the prices. In this case, we move to the feature of income to visualize the possible investment points. The states of Illinois and Arizona both decreases in income in the last two years. 
The population feature can also be considered in the analysis, once the increase of population can impact in the house prices. Considering that California had a decrease in population in the past two years, we can conclude that Texas would be the best investment spot in the areas analysed. 

### Visualizing and Analyzing Data

We used Tableau to create different charts, graphs, maps, dashboards, and stories for visualizing and analyzing data to help home buyers in making decisions. Two datasets were used to compare and analyse the following questions: 

1. Relationship between Location and Price
2. Property count and Property Types
3. Minimum and Maximum Price of Property 
4. Features Affecting selling Prices like number of bedrooms and bathrooms, living space, postal code and address

- Link for Tableau Visualization         https://public.tableau.com/app/profile/sughra.shadab/vizzes

## Licence 
The dataset utilized in this project originates from Kaggle ["https://www.kaggle.com/datasets/polartech/500000-us-homes-data-for-sale-properties"] and Fred Economic Data ["https://fred.stlouisfed.org/"] and is made available under its respective licensing terms.

Please refer to the Kaggle dataset's licensing information for specific details regarding permitted usage, redistribution, and any restrictions imposed by the dataset provider.
