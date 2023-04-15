import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("autos.csv", encoding='latin-1')

# Display the first few rows of the dataset
print(df.head())

# Get the summary statistics of the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Check for duplicate rows
print(df.duplicated().sum())

# Plot the distribution of the target variable 'price'
plt.hist(df['price'], bins=20)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Histogram of Price')
plt.show()

# Plot the scatter plot between 'price' and 'yearOfRegistration'
plt.scatter(df['yearOfRegistration'], df['price'])
plt.xlabel('Year of Registration')
plt.ylabel('Price')
plt.title('Scatter Plot of Year of Registration vs Price')
plt.show()

# Plot the boxplot of 'price' vs 'vehicleType'
sns.boxplot(x='vehicleType', y='price', data=df)
plt.title('Boxplot of Vehicle Type vs Price')
plt.show()

# Plot the boxplot of 'price' vs 'brand'
plt.figure(figsize=(15,5))
sns.boxplot(x='brand', y='price', data=df)
plt.title('Boxplot of Brand vs Price')
plt.xticks(rotation=90)
plt.show()
