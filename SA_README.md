# Real Estate Price Prediction Project
Overview
This project aims to predict real estate prices based on various features using machine learning. The dataset was obtained from Kaggle
 (https://www.kaggle.com/datasets/polartech/500000-us-homes-data-for-sale-properties)
 The project involves data cleaning, outlier removal, and utilizing a Random Forest Regressor model for price prediction and evaluated the model performance using R-squared (R2) scores and Mean Absolute Error (MAE).

## Project Steps

### 1. Data Collection:
The dataset was sourced from Kaggle, providing comprehensive real estate information.

### 2. Data Cleaning:
1. Removed null values and unnecessary columns.
2. Handled data types and converted units for consistency.
3. Dropped rows with specific criteria (e.g., null values in 'price_per_unit').

### 3. Outlier Removal:
1. Identified and handled outliers using statistical methods.

### 4. Machine Learning Model: RandomForestRegressor:

1. Developed a machine learning model using the RandomForestRegressor algorithm.
2. Chose 'Price' as the target variable and 'Bedroom number,' 'Bathroom number,' 'Living space (sqft),' and 'City' as features.
3. Split the data into training and testing sets.
4. Trained the model on the training data.

### 5. Predictions and Evaluation:

1. Made predictions using the trained model on both training and testing data.
2. Evaluated the model performance using R-squared (R2) scores and Mean Absolute Error (MAE).

## Results
#### For a sample client input:
(Python code)
client_input = pd.DataFrame({'bedroom_number': [3], 'bathroom_number': [2], 'living_space': [1500], 'city': ['Chino Valley']})

#### The model provided the following results:
Predicted Price: $320,734.04
R-squared (R2) Score on Training Data: 0.9621
R-squared (R2) Score on Testing Data: 0.7621
Mean Absolute Error on Training Data: $40,150.86
Mean Absolute Error on Testing Data: $96,945.73

## Explanation of Results
1. Predicted Price: $320,734.04 - The model predicts that a property with 3 bedrooms, 2 bathrooms, a living space of 1500 sqft, and located in Chino Valley 
will have a price of approximately $320,734.04.

2. R-squared (R2) Score on Training Data: 0.9621 - The R-squared score on the training data measures how well the model explains the variance in the target variable (Price). An R-squared score of 0.9621 indicates that the model captures a significant portion (96.21%) of the variability in the training data. 
The high R-squared on the training data suggests that the model fits the training data well, capturing the underlying patterns.

3. R-squared (R2) Score on Testing Data: 0.7621 - The R-squared score on the testing data evaluates how well the model generalizes to new, unseen data. A score of 0.7621 suggests that the model explains 76.21% of the variance in the testing data. A high R-squared on testing data is positive.

4. Mean Absolute Error on Training Data: $40,150.86 - The Mean Absolute Error (MAE) on the training data is a measure of the average absolute difference between the actual and predicted prices. An MAE of $40,150.86 indicates 'Predicted price' and actual price may vary by +- of $40,150.86 which is low and indicates the model predicted price is close to the MAE. 

5. Mean Absolute Error on Testing Data: $96,945.73 - The MAE on the testing data provides insight into how well the model generalizes to new data. 
