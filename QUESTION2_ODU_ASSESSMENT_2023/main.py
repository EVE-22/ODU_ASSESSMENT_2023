import pandas as pd
import matplotlib.pyplot as plt
# A basic python script to load and read it as dataframe. 
auto_var = pd.read_csv('autos.csv', encoding='latin-1')

# Find the average price of autos using price column of database
avg_price = auto_var['price'].mean()
print("Average price of autos:", round(avg_price, 3))

# Print the list of different possible types of VehicleType found in dataset
vehicle_type = auto_var['vehicleType'].unique()
print("Possible Vehicle Types:", vehicle_type)

#Calculate and print lowest yearOfRegistration and highest yearOfRegistration
lowest_reg_year = auto_var['yearOfRegistration'].min()
highest_reg_year = auto_var['yearOfRegistration'].max()
print("Lowest Year of Registration:", lowest_reg_year)
print("Highest Year of Registration:", highest_reg_year)

# Find and print standard deviation of column kilometer
kilometer_std_dev = auto_var['kilometer'].std()
print("Standard deviation of kilometers:", round(kilometer_std_dev, 2))

# Draw a bar graph to represent count of different type of column brand
brand_counts = auto_var['brand'].value_counts()
plt.bar(brand_counts.index, brand_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Brand')
plt.ylabel('Count')
plt.title('Count of Autos by Brand')
plt.show()

#  Find out which VehicleType is sold minimum and maximum
min_sold_vehicle_type = auto_var.groupby('vehicleType')['dateCreated'].count().idxmin()
max_sold_vehicle_type = auto_var.groupby('vehicleType')['dateCreated'].count().idxmax()
print("Vehicle Type sold the least:", min_sold_vehicle_type)
print("Vehicle Type sold the most:", max_sold_vehicle_type)

# Create a pie chart to represent different types of gearbox count
gearbox_counts = auto_var['gearbox'].value_counts()
plt.pie(gearbox_counts.values, labels=gearbox_counts.index, autopct='%1.1f%%')
plt.title('Percentage of Autos by Gearbox Type')
plt.show()
