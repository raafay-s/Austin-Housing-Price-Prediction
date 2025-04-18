# Austin Housing Price Prediction Project
This project builds a machine learning model to predict residential housing prices in Austin, Texas, based on key property features such as size, lot area, number of bedrooms and bathrooms, garage spaces, and school ratings. The project includes data cleaning, feature engineering, random forest modeling, model evaluation, statistical analysis, and visualizations of results.

## Project Overview
In this project, I developed a Random Forest regression model to predict housing prices in Austin, Texas. The model leverages key property features such as living area size, lot size, number of bedrooms and bathrooms, garage spaces, number of stories, year built, average school rating, property tax rate, and home type. The dataset was carefully cleaned by removing outliers (homes priced above $1.5M or below $100k), handling missing values, and engineering new features such as the bathroom-to-bedroom ratio. The original dataset, sourced from 2024 Austin housing market data, included a diverse range of residential properties across different neighborhoods, providing a realistic mix of affordable, mid-range, and luxury homes. After preprocessing, the dataset offered a strong foundation for training a machine learning model to capture both general trends and regional pricing variations.

## Technologies and Libraries
* **Python 3**: general-purpose programming language used for data processing, machine learning, and visualization.
* **pandas**: Library for data manipulation and analysis, used to clean and structure the dataset.
* **numpy**: Library for numerical operations, supporting array handling and mathematical functions.
* **scikit-learn**: Machine learning library used to build, train, and evaluate the Random Forest regression model.
* **matplotlib**: Visualization library used to create scatter plots, histograms, and other graphical representations of the data.

## Files Included
- **austinHousingData.csv** — Cleaned dataset of Austin housing prices, used for model training and analysis.
- **main_model.py** — Main script that loads the data, trains the Random Forest regression model, evaluates performance, and prints R² results.
- **graph_visualizations.py** — Script to generate scatter plots and visual graphs comparing actual versus predicted housing prices.
- **stats_calculations.py** — Script to calculate dataset statistics including mean, median, standard deviation, quartiles, and price per square foot.
- **actual_vs_predicted_formatted.csv** — Output file showing actual prices, predicted prices, absolute error, and prediction accuracy for each home.
- **graphs_analysis.md** — Detailed analysis of the distribution histogram and actual vs predicted scatter plot insights.

## Dataset Summary
After cleaning, the dataset contained a wide range of residential properties.
Key statistics for the dataset are as follows:

* **Mean House Price:** $463,281
* **Median House Price:** $399,990
* **Standard Deviation:** $235,524
* **Minimum Price:** $102,000
* **Maximum Price:** $1,499,999
* **Price Quartiles:**
  * 25th Percentile (Q1): $305,000
  * 50th Percentile (Median): $399,990
  * 75th Percentile (Q3): $550,000
* **Mean Price per Square Foot:** $230.71

These figures highlight the diversity of the Austin housing market, with the majority of properties clustered between approximately $300,000 and $550,000. The relatively high standard deviation reflects a significant spread in house prices, indicating the challenge of modeling such a dynamic and variable market.

## Results and Analysis:
The model achieved an **R² score of 0.73**, meaning it explains approximately **73% of the variability** in housing prices. This is a strong result, especially considering that many real-world factors affecting property prices — such as renovation quality, neighborhood reputation, or unique amenities — are not captured within the available dataset. 


The scatter plot of actual versus predicted prices visually reflects this performance: 
* The **red dashed line** represents perfect predictions.
* Most homes priced between $200,000 and $700,000 are predicted fairly accurately, clustering around the perfect line.
* As home prices increase beyond $700,000, prediction errors tend to widen, indicating that the model struggles more with luxury and high-end properties.
* This behavior is typical in real estate modeling, where higher-priced homes have greater variability due to unique features not included in basic property data.

## Challenges:
Several factors limited the model's performance:
* **Missing Features**: Important drivers of home value — such as interior upgrades, views, walkability, and proximity to parks or shopping areas — were not included in the dataset.
* **Non-linearity in Expensive Homes:** Luxury properties tend to have unpredictable pricing driven by subjective factors, making them harder to model with simple structural features.
* **Limited Feature Engineering:** While basic engineered features like the bathroom-to-bedroom ratio were included, more complex features and interactions could have further improved predictive power.

## Opportunities for Improvement:
* **Add richer features:** Incorporating renovation status, proximity to desirable locations, neighborhood crime rates, and recent market trends would likely enhance model accuracy.
* **Use geospatial models:** Including latitude/longitude clustering or localized neighborhood scoring could better account for regional price differences.
* **Segment the market:** Training separate models for different price ranges (e.g., affordable vs luxury homes) could improve accuracy in price extremes.

## Conclusion:
Despite unavoidable limitations, the model successfully captures key trends and patterns in the Austin housing market. The R² score of 0.73 demonstrates that the model explains the majority of house price variability based on available structural and property features. The scatter plot visualization, combined with statistical analysis of the dataset, confirms both the strengths and the natural limitations of modeling a dynamic real estate market. This project highlights the challenges of real-world regression modeling and sets a strong foundation for future improvements by enriching datasets, engineering deeper features, and exploring more advanced modeling techniques.
