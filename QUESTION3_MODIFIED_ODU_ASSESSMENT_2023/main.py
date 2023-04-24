import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data
autos = pd.read_csv('autos.csv', encoding='latin-1')
# Check the shape of the dataset
print('Shape of the dataset:', autos.shape)

# Check the column names
print('Columns in the dataset:', list(autos.columns))
# Check the data types of the columns
print(autos.dtypes)
# Check for missing values
print(autos.isnull().sum())
# Check for unique values in categorical columns
print('Seller:', autos['seller'].unique())
print('Offer Type:', autos['offerType'].unique())
print('AB Test:', autos['abtest'].unique())
print('Vehicle Type:', autos['vehicleType'].unique())
print('Gearbox:', autos['gearbox'].unique())
print('Model:', autos['model'].unique())
print('Fuel Type:', autos['fuelType'].unique())
print('Brand:', autos['brand'].unique())
print('Not Repaired Damage:', autos['notRepairedDamage'].unique())

# Visualize the distribution of numerical columns
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs[0, 0].hist(autos['price'], bins=20, color='green')
axs[0, 0].set_xlabel('Price')
axs[0, 0].set_ylabel('Count')
axs[0, 0].set_title('Distribution of Price')

axs[0, 1].hist(autos['yearOfRegistration'], bins=20, color='blue')
axs[0, 1].set_xlabel('Year of Registration')
axs[0, 1].set_ylabel('Count')
axs[0, 1].set_title('Distribution of Year of Registration')

axs[1, 0].hist(autos['powerPS'], bins=20, color='red')
axs[1, 0].set_xlabel('Power PS')
axs[1, 0].set_ylabel('Count')
axs[1, 0].set_title('Distribution of Power PS')

axs[1, 1].hist(autos['kilometer'], bins=20, color='orange')
axs[1, 1].set_xlabel('Kilometer')
axs[1, 1].set_ylabel('Count')
axs[1, 1].set_title('Distribution of Kilometer')

plt.tight_layout()
plt.show()

# Visualize the relationship between numerical columns and the target variable
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].scatter(autos['powerPS'], autos['price'], color='purple')
axs[0].set_xlabel('Power PS')
axs[0].set_ylabel('Price')
axs[0].set_title('Power PS vs. Price')

axs[1].scatter(autos['yearOfRegistration'], autos['price'], color='pink')
axs[1].set_xlabel('Year of Registration')
axs[1].set_ylabel('Price')
axs[1].set_title('Year of Registration vs. Price')

axs[2].scatter(autos['kilometer'], autos['price'], color='grey')
axs[2].set_xlabel('Kilometer')
axs[2].set_ylabel('Price')
axs[2].set_title('Kilometer vs. Price')

plt.tight_layout()
plt.show()

# Visualize the relationship between categorical columns and the target variable
fig, axs = plt.subplots(ncols=3, figsize=(20,5))

axs[0].boxplot(x=autos['price'], notch=True, vert=False)
axs[0].set_title('Price')

axs[1].boxplot(x=autos['yearOfRegistration'], notch=True, vert=False)
axs[1].set_title('Year of Registration')

axs[2].boxplot(x=autos['powerPS'], notch=True, vert=False)
axs[2].set_title('Power PS')

plt.show()

# Check for outliers
fig, axs = plt.subplots(ncols=4, figsize=(20,5))

axs[0].boxplot(x=autos['price'], notch=True, vert=False)
axs[0].set_title('Price')

axs[1].boxplot(x=autos['yearOfRegistration'], notch=True, vert=False)
axs[1].set_title('Year of Registration')

axs[2].boxplot(x=autos['powerPS'], notch=True, vert=False)
axs[2].set_title('Power PS')

axs[3].boxplot(x=autos['kilometer'], notch=True, vert=False)
axs[3].set_title('Kilometer')

plt.show()