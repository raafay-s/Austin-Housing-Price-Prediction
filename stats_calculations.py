# Mean (Average) Price
mean_price = df['latestPrice'].mean()

# Median Price
median_price = df['latestPrice'].median()

# Standard Deviation of Prices
std_dev_price = df['latestPrice'].std()

# Min and Max Prices
min_price = df['latestPrice'].min()
max_price = df['latestPrice'].max()

# Price Quartiles
quartiles = df['latestPrice'].quantile([0.25, 0.5, 0.75])

# Mean Price per Square Foot
mean_price_per_sqft = (df['latestPrice'] / df['livingAreaSqFt']).mean()

# Print everything cleanly
print(f"Mean House Price: ${mean_price:,.2f}")
print(f"Median House Price: ${median_price:,.2f}")
print(f"Standard Deviation of Prices: ${std_dev_price:,.2f}")
print(f"Minimum House Price: ${min_price:,.2f}")
print(f"Maximum House Price: ${max_price:,.2f}")
print("\nPrice Quartiles:")
print(quartiles)

print(f"\nMean Price per Square Foot: ${mean_price_per_sqft:,.2f}")