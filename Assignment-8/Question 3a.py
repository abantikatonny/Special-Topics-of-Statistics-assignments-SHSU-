import statsmodels.api as sm
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('q3.csv') # load data set 
X = data.iloc[:, 1].values.reshape(-1, 1) # values converts it into a numpy array 
Y = data.iloc[:, 0].values.reshape(-1, 1) # -1 means that calculate the dimension of rows, but have 1 column 
linear_regressor = LinearRegression() # create object for the class 
linear_regressor.fit(X, Y) # perform linear regression 
Y_pred = linear_regressor.predict(X) # make predictions 
print('Intercept:', linear_regressor.intercept_) 
print('coefficient',linear_regressor.coef_) 
print('coefficient of determination:', linear_regressor.score(X,Y)) 
plt.xlabel('Age') 
plt.ylabel('Death Rate') 
plt.scatter(X, Y) 
plt.plot(X, Y_pred, color='red') 
plt.show()

keep = ['Death_Rate', 'Age'] 
db = data[keep].dropna() 
db.head() 
model = sm.OLS.from_formula("Death_Rate ~ Age", data=db) 
result = model.fit()
print(result.summary())