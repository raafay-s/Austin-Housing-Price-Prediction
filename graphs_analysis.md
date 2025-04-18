# Graph Analysis Overview
This section provides visual analyses to better understand both the distribution of house prices in the Austin housing dataset and the performance of the machine learning model. The graphs help reveal patterns in the data, challenges faced by the model, and areas where predictions are stronger or weaker.

*Note: The code used to generate these graphs can be found in the file graph_visualizations.py.*
#
## 📊 1. Distribution of House Prices in Austin Dataset
**Description**: This histogram displays the distribution of house prices in the Austin housing dataset. The x-axis represents house price ranges, while the y-axis shows the number of homes within each price range.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ca107d1c-7c29-4c80-9754-435609e9f209" alt="Distribution of House Prices" width="600" style="border:2px solid black;">
</p>

**Insights**:
* The distribution is **right-skewed**, meaning most houses are priced on the lower end.
* The majority of homes are priced between **$200,000 and $500,000**, with a peak around **$350,000–$375,000**.
* There are fewer homes in the higher price ranges above **$800,000**, but some properties go beyond **$1.4M**.
* This skew impacts model performance, as the model must predict accurately across a wide and imbalanced range.

**Finding**: The skewed distribution toward lower-priced homes indicates that the model must generalize across a highly imbalanced dataset, making predictions for luxury properties particularly challenging.
#

## 📈 2. Actual vs Predicted House Prices
**Description**: This scatter plot compares actual house prices (x-axis) with predicted prices from the ML model (y-axis). The red dashed line represents perfect predictions (where predicted = actual).

<p align="center">
  <img src="https://github.com/user-attachments/assets/c5dabece-b90d-4331-a63f-5c16f88f94ac" alt="Actual vs Predicted House Prices" width="600" style="border:2px solid black;">
</p>

**Insights**:
* Predictions are generally **well-aligned for mid-range homes**, especially between **$200,000 and $700,000**.
* **Wider variance appears at higher price points**, indicating the model struggles more with predicting luxury homes accurately.
* Many points fall **below the red line**, suggesting the model **underestimates** prices in higher ranges.
* Overall, the model captures the general trend of house prices but shows greater uncertainty in the higher price ranges.

**Finding:** The model predicts mid-range homes reasonably well but tends to underestimate prices for more expensive properties, highlighting a need for richer features to improve luxury home predictions.

#
## 🔎 Overall Conclusion
Together, the distribution histogram and the actual vs predicted scatter plot provide a deeper understanding of the challenges faced in predicting Austin housing prices.
The dataset’s right-skewed distribution means the majority of homes are clustered at lower price points, while luxury properties are rarer and more difficult to predict accurately.
The scatter plot confirms that the model performs well for mid-range homes but shows greater variability and underestimation at higher price points.

These observations highlight that while the machine learning model captures general market trends effectively, its performance could be further improved by introducing additional features that better represent luxury property characteristics, location desirability, and unique home attributes.
Overall, the graphs reinforce the need for nuanced modeling strategies in highly imbalanced and dynamic real estate markets like Austin.


