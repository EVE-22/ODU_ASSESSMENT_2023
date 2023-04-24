
# # Visualize the relationship between numerical columns and the target variable
# sns.scatterplot(data=autos, x='powerPS', y='price')
# sns.scatterplot(data=autos, x='yearOfRegistration', y='price')
# sns.scatterplot(data=autos, x='kilometer', y='price')
# plt.show()
# # Visualize the relationship between categorical columns and the target variable
# sns.boxplot(data=autos, x='vehicleType', y='price')
# sns.boxplot(data=autos, x='gearbox', y='price')
# sns.boxplot(data=autos, x='brand', y='price')
# plt.show()
# # Check for outliers
# sns.boxplot(data=autos, x='price')
# sns.boxplot(data=autos, x='yearOfRegistration')
# sns.boxplot(data=autos, x='powerPS')
# sns.boxplot(data=autos, x='kilometer')
# plt.show()