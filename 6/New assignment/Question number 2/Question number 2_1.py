import pandas as pd
from pandas import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.linear_model import LinearRegression

data = pd.read_csv('C:/hmm/courses/3rd semester/Special topics/Assignment/6/New assignment/Question number 2/Crime2.csv', index_col=0)

col1 = ['Poverty']
x = data[col1]
col2 = ['Violent']
y = data[col2]
model = LinearRegression().fit(x, y)

r_square = model.score(x, y)
print("The coefficient of determination:", r_square)

r = math.sqrt(r_square)
print("r:", round(r,2))
print("The prediction equation:",model.intercept_,"+",model.coef_,"X")


plt.plot(x,model.coef_*x + model.intercept_,)
plt.scatter(x,y)
plt.show()