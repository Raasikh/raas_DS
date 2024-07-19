# -*- coding: utf-8 -*-
"""projectINTRO

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oDirxpmIvv5RceEn4dSdCOc5wHdwClCt
"""

import pandas as pd
df= pd.read_excel("/content/sample_data/Independent Houses.xlsx")
df

# Replacing infinite values with NaN in the 'Washroom' column
import numpy as np
df['Washroom'].replace([np.inf,-np.inf],np.nan,inplace=True) #(Raasikh Naveed [y979j497])
# Filling missing (NaN) values in the 'Washroom' column with 0
df['Washroom'].fillna(0,inplace=True)
df['Washroom']=df['Washroom'].astype(int)
df['Washroom'].dtype

# Replacing infinite values with NaN in the 'Sqft' column.
df['Sqft'].replace([np.inf, -np.inf], np.nan, inplace=True)
df['Sqft'].fillna(df['Sqft'].mean(), inplace=True)
# Converting the data type of the 'Sqft' column to integer.
df['Sqft'] = df['Sqft'].astype(int)
df['Sqft'].dtype  #[Priya Parajuli-E442F823]

#Filling missing values in 'Sqft' with its mean, including NaNs in the mean calculation, updating the column in-place.
mean_column1=df['Sqft'].mean()
df['Sqft']=df['Sqft'].fillna(mean_column1)
df  #(Raasikh Naveed [y979j497])

df

# Fill all the 0 values of the 'Sqft' column with its mean
df['Sqft'] = df['Sqft'].replace(0, df['Sqft'].mean())

# Nikhil Kumar Pathi (g274p387)

df

#plotting the histogram  between sqaure feet and frequency
import matplotlib.pyplot as plt
plt.hist(df['Sqft'])
plt.xlabel('Square Feet')
plt.ylabel('Frequency')
plt.title('Distribution of Square Feet')
plt.show()
# (Darshak Alapati [W353A566])

# Creating a histogram with 20 bins
plt.hist(df['Rent'], bins=20)

# Setting the title and labels for the plot
plt.title('Histogram of Rent')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.show()
# (Darshak Alapati [W353A566])

# Creating a histogram with 10 bins
plt.hist(df['Distance from Wsu'], bins=10)

# Setting the title and labels for the plot
plt.title('Histogram of Distance from Wsu')
plt.xlabel('Miles')
plt.ylabel('Frequency')

plt.show()
# (Darshak Alapati [W353A566])

# Creating a histogram with 5 bins
plt.hist(df['Bed'], bins=5)

# Setting the title and labels for the plot
plt.title('Histogram of Bed')
plt.xlabel('Bed')
plt.ylabel('Frequency')

plt.show()

# Nikhil Kumar Pathi (g274p387)

# Creating a histogram with 5 bins
plt.hist(df['Washroom'], bins=5)

# Setting the title and labels for the plot
plt.title('Histogram of Washroom')
plt.xlabel('Washroom')
plt.ylabel('Frequency')

plt.show()

#[Priya Parajuli-E442F823]

df

# scatterplot between rent and sqft

plt.scatter(df['Rent'], df['Sqft'])
plt.xlabel('Rent')
plt.ylabel('Square Feet')
plt.title('Scatterplot of Rent vs Square Feet')
plt.show()
# (Darshak Alapati [W353A566])

# scatterplot between rent and distance from wsu

plt.scatter(df['Rent'], df['Distance from Wsu'])
plt.xlabel('Rent')
plt.ylabel('Distance from Wsu')
plt.title('Scatterplot of Rent vs Distance from Wsu')
plt.show()
#(karthikeya Nerella [ F779A383])

y=df.iloc[:,5]

import statsmodels.api as sm #(Raasikh Naveed [y979j497])
X1=sm.add_constant(df.iloc[:,1:5].values)
foo=pd.DataFrame(X1)
foo.head()

# Fit the linear regression model
model1 = sm.OLS(y, X1).fit()
model1.summary(xname=['intercept','Distance from wsu', 'Bed', 'Washroon', 'Sqft']) #(Raasikh Naveed [y979j497])

df

# Hamza Khader Shaik Mohammed [M752R568]
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df[['Distance from Wsu', 'Bed', 'Sqft']], df['Rent'], test_size=0.2, random_state=42)

# Model 1: Ridge Regression
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
ridge_train_pred = ridge_model.predict(X_train)
ridge_test_pred = ridge_model.predict(X_test)
ridge_train_rmse = mean_squared_error(y_train, ridge_train_pred, squared=False)
ridge_test_rmse = mean_squared_error(y_test, ridge_test_pred, squared=False)
print("Model 1: Ridge Regression")
print(f"Train RMSE: {ridge_train_rmse:.2f}")
print(f"Test RMSE: {ridge_test_rmse:.2f}")

import matplotlib.pyplot as plt

# Scatter plot for Model 1: Ridge Regression
plt.figure(figsize=(12, 6))
plt.scatter(y_train, ridge_train_pred, color='blue', label='Train')
plt.scatter(y_test, ridge_test_pred, color='red', label='Test')
plt.xlabel('Actual Rent')
plt.ylabel('Predicted Rent')
plt.title('Model 1: Ridge Regression')
plt.legend()
plt.show()

# Model 2: Lasso Regression # Hamza Khader Shaik Mohammed [M752R568]
lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train, y_train)
lasso_train_pred = lasso_model.predict(X_train)
lasso_test_pred = lasso_model.predict(X_test)
lasso_train_rmse = mean_squared_error(y_train, lasso_train_pred, squared=False)
lasso_test_rmse = mean_squared_error(y_test, lasso_test_pred, squared=False)
print("\nModel 2: Lasso Regression")
print(f"Train RMSE: {lasso_train_rmse:.2f}")
print(f"Test RMSE: {lasso_test_rmse:.2f}")

# Scatter plot for Model 2: Lasso Regression
plt.figure(figsize=(12, 6))
plt.scatter(y_train, lasso_train_pred, color='blue', label='Train')
plt.scatter(y_test, lasso_test_pred, color='red', label='Test')
plt.xlabel('Actual Rent')
plt.ylabel('Predicted Rent')
plt.title('Model 2: Lasso Regression')
plt.legend()
plt.show()

# Model 3: ElasticNet Regression ( Raasikh Ahmed y979j497)
elasticnet_model = ElasticNet(alpha=1.0, l1_ratio=0.5)
elasticnet_model.fit(X_train, y_train)
elasticnet_train_pred = elasticnet_model.predict(X_train)
elasticnet_test_pred = elasticnet_model.predict(X_test)
elasticnet_train_rmse = mean_squared_error(y_train, elasticnet_train_pred, squared=False)
elasticnet_test_rmse = mean_squared_error(y_test, elasticnet_test_pred, squared=False)
print("\nModel 3: ElasticNet Regression")
print(f"Train RMSE: {elasticnet_train_rmse:.2f}")
print(f"Test RMSE: {elasticnet_test_rmse:.2f}")

# Scatter plot for Model 3: ElasticNet Regression ( Raasikh Ahmed y979j497)
plt.figure(figsize=(12, 6))
plt.scatter(y_train, elasticnet_train_pred, color='blue', label='Train')
plt.scatter(y_test, elasticnet_test_pred, color='red', label='Test')
plt.xlabel('Actual Rent')
plt.ylabel('Predicted Rent')
plt.title('Model 3: ElasticNet Regression')
plt.legend()
plt.show()

# Hamza Khader Shaik Mohammed [M752R568]
# Plotting coefficients for each model
plt.figure(figsize=(12, 6))

# Model 1: Ridge Regression
plt.subplot(1, 3, 1)
plt.bar(['Distance from WSU', 'Bed', 'Sqft'], ridge_model.coef_)
plt.title('Model 1: Ridge Regression')
plt.xlabel('Independent Variables')
plt.ylabel('Coefficient')

# Model 2: Lasso Regression
plt.subplot(1, 3, 2)
plt.bar(['Washroom', 'Sqft', 'Distance from WSU'], lasso_model.coef_)
plt.title('Model 2: Lasso Regression')
plt.xlabel('Independent Variables')
plt.ylabel('Coefficient')

# Model 3: ElasticNet Regression
plt.subplot(1, 3, 3)
plt.bar(['Distance from WSU', 'Bed', 'Washroom'], elasticnet_model.coef_)
plt.title('Model 3: ElasticNet Regression')
plt.xlabel('Independent Variables')
plt.ylabel('Coefficient')

plt.tight_layout()
plt.show()

