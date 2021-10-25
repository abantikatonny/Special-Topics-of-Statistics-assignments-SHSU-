import pandas as pd
import matplotlib.pyplot as plt
from pandas import *
from sklearn.linear_model import LinearRegression
import numpy as np
import math

data = pd.read_csv('C:/hmm/courses/3rd semester/Special topics/Assignment/6/New assignment/Question number 1/csv2.csv', index_col=0)

#importing the columns
col1 = ['Ownership']
x = data[col1]
col2 = ['Rate']
y = data[col2]

#equations
model = LinearRegression().fit(x, y)
r_square = model.score(x, y)
rvalue = math.sqrt(r_square)
print(rvalue)

#show the graph

plt.plot(x,model.coef_*x + model.intercept_)
plt.scatter(x,y)
plt.show()