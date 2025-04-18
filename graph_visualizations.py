# --- Actual vs Predicted Prices Scatter Plot ---
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Scatter plot
plt.figure(figsize=(10,7))
plt.scatter(y_test_actual, y_pred, alpha=0.7)

# Plot perfect prediction line
plt.plot([y_test_actual.min(), y_test_actual.max()],
         [y_test_actual.min(), y_test_actual.max()],
         'r--', label='Perfect Prediction')

# Set labels
plt.xlabel('Actual Prices ($)', fontsize=14)
plt.ylabel('Predicted Prices ($)', fontsize=14)

# Set title
plt.title('Actual vs Predicted House Prices', fontsize=16)

# Format ticks with dollar signs and commas
ax = plt.gca()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${int(x):,}'))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, _: f'${int(y):,}'))

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend()

# Show plot
plt.show()


# --- House Price Distribution Histogram ---
import matplotlib.pyplot as plt

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(df['latestPrice'], bins=50, color='skyblue', edgecolor='black')

# Set labels and title
plt.xlabel('House Price ($)', fontsize=14)
plt.ylabel('Number of Homes', fontsize=14)
plt.title('Distribution of House Prices in Austin Dataset', fontsize=16)

# Format x-axis with dollar signs and commas
ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x):,}'))

# Add grid
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()