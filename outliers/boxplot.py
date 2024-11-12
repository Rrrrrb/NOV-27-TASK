import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Value': [10, 12, 12, 13, 12, 11, 12, 300, 13, 12, 11, 12]}
df = pd.DataFrame(data)

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)

# Calculate the Interquartile Range (IQR)
IQR = Q3 - Q1

# Define the bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
df['Outlier'] = df['Value'].apply(lambda x: 'Yes' if x < lower_bound or x > upper_bound else 'No')

# Display the DataFrame with outlier labels
print(df)

# Plot box plot to visualize outliers
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Value'])
plt.title("Boxplot of Values with Outliers")
plt.show()
