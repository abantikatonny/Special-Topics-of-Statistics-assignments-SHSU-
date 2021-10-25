import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'Crime2a.csv', skipfooter=1, engine='python')
df.head()

# split the dataframe into dependent and independent variables.
X = df[['state','violent','metro','white','hs','poverty']]
Y = df['murder']

# since the state is a string datatype column we need to encode/flatten it.
X = pd.get_dummies(X)
print(X.shape)

# Splitting dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Applying multiple linear regression on all features
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
print('Model score: ' + str(regressor.score(X_test, Y_test)))
print(X.shape)

# Predicting re results
y_pred = regressor.predict(X_test)

# Creating automated backward elimination function with p-values and adjusted r-sqaured
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)

def backwardElimination(x, SL):
    numVars = len(x[0])
    print(numVars)
    temp = np.zeros((50, 6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(Y, x).fit()
        maxVar = max(regressor_OLS.pvalues)  # .astype(float)
        adjR_before = regressor_OLS.rsquared_adj  # .astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:, j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(Y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj  # .astype(float)
                    print(tmp_regressor.summary())
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:, [0, j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print(regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    #print(regressor_OLS.summary())
    return x

# Applying the backward elimination
SL = 0.10
X_opt = X[:, [0, 1, 2, 3, 4, 5,6]]
X_opt = np.array(X_opt, dtype=float)
X_Modeled = backwardElimination(X_opt, SL)
regressor_OLS = sm.OLS(endog=Y, exog=X_Modeled).fit()
regressor_OLS.summary()

print('Parameters: ', regressor_OLS.params)
print('R2: ', regressor_OLS.rsquared)
print('exog_names= ' , regressor_OLS.model.exog_names)
print('endog_names= ',regressor_OLS.model.endog_names)