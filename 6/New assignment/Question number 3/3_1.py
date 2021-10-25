import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import *
import numpy as np
from sklearn.linear_model import LinearRegression

data=pd.read_csv('C:\hmm\courses\3rd semester\Special topics\Assignment\6\New assignment\Question number 4/ index_col=False)

col1=['Taxes']
y=data[col1]
col2=['Size']
x=data[col2]

model=LinearRegression().fit(x, y)
r_square=model.score(x, y)
print("The r2:", r_square)

r=math.sqrt(r_square)
print("The r:", round(r,2))
print('Slope:', model.coef_)
print('The y-intercept:', model.intercept_)
print("Prediction equation= ",model.intercept_,"+",model.coef_,"X")


plt.plot(x,model.coef_*x + model.intercept_)
plt.scatter(x,y)
plt.show()