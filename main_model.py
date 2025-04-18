# --- Main Model Script ---
# Imports
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load dataset
file_path = 'C:/Users/raafa/Downloads/austinHousingData.csv'  # Update if needed
df = pd.read_csv(file_path)

# Remove outliers
df = df[(df['latestPrice'] < 1500000) & (df['latestPrice'] > 100000)]  # keep homes $100k-$1.5M
df = df[df['livingAreaSqFt'] > 500]  # remove tiny houses

# Drop rows with missing important values
df = df.dropna(subset=[
    'latestPrice', 'livingAreaSqFt', 'lotSizeSqFt', 'zipcode', 
    'garageSpaces', 'yearBuilt', 'numOfBathrooms', 'numOfBedrooms', 
    'numOfStories', 'avgSchoolRating', 'propertyTaxRate', 'homeType'
])

# Feature Engineering: create bathroom-to-bedroom ratio
df['bath_bed_ratio'] = df['numOfBathrooms'] / df['numOfBedrooms']
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

# Select features (X) and target (y)
X = df[['livingAreaSqFt', 'lotSizeSqFt', 'zipcode', 'garageSpaces', 
        'yearBuilt', 'numOfBathrooms', 'numOfBedrooms', 'numOfStories', 
        'avgSchoolRating', 'propertyTaxRate', 'homeType',
        'bath_bed_ratio']]  # <--- No price_per_sqft

y = np.log1p(df['latestPrice'])  # Log-transform target

# CUSTOM TRAIN/TEST SPLIT
np.random.seed(42)
mask = np.random.rand(len(df)) < 0.8  # 80% train, 20% test
X_train = X[mask]
X_test = X[~mask]
y_train = y[mask]
y_test = y[~mask]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['homeType', 'zipcode'])
    ],
    remainder='passthrough'
)

# Build Random Forest model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=5,
        random_state=42
    ))
])

# Train the model
model.fit(X_train, y_train)

# Predict and reverse log
y_pred_log = model.predict(X_test)
y_pred = np.expm1(y_pred_log)
y_test_actual = np.expm1(y_test)

# Evaluate
r2 = r2_score(y_test_actual, y_pred)

# Print R² Score
print(f"R² Score: {r2:.2f}")


# --- Save Actual vs Predicted Prices to CSV ---
# Create a DataFrame with Actual, Predicted, and Accuracy
results_df = pd.DataFrame({
    'Actual Price ($)': y_test_actual,
    'Predicted Price ($)': y_pred
})

# Round Actual and Predicted to nearest dollar
results_df = results_df.round(0)

# Add Absolute Error (difference between actual and predicted)
results_df['Absolute Error ($)'] = (results_df['Actual Price ($)'] - results_df['Predicted Price ($)']).abs()

# Add Accuracy (%) = 1 - (error / actual price)
results_df['Accuracy (%)'] = (1 - results_df['Absolute Error ($)'] / results_df['Actual Price ($)']) * 100
results_df['Accuracy (%)'] = results_df['Accuracy (%)'].round(2)  # Round to 2 decimals

# Format Actual Price, Predicted Price, and Error with commas and dollar signs
results_df['Actual Price ($)'] = results_df['Actual Price ($)'].apply(lambda x: f"${int(x):,}")
results_df['Predicted Price ($)'] = results_df['Predicted Price ($)'].apply(lambda x: f"${int(x):,}")
results_df['Absolute Error ($)'] = results_df['Absolute Error ($)'].apply(lambda x: f"${int(x):,}")

# Save to CSV
results_df.to_csv('actual_vs_predicted_formatted.csv', index=False)

print("Formatted CSV 'actual_vs_predicted_formatted.csv' created successfully!")
