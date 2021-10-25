import statsmodels.api as sm
import pandas as pd
from pandas import *
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv('C:/hmm/courses/3rd semester/Special topics/Assignment/6/New assignment/Question number 4/csv4.csv', index_col=False)

col1=["Mother_education"]
x=data[col1]
col2=["Num_children"]
y=data[col2]

model=LinearRegression().fit(x, y)

r_square=model.score(x, y)
print("The r2:", r_square)
r=math.sqrt(r_square)
print("The r:", round(r,2))
print('The y-intercept:', model.intercept_)
print('The slope:', model.coef_)
print("The prediction equation ŷ = ",model.intercept_,"+",model.coef_,"X")


plt.plot(x,model.coef_*x + model.intercept_)
plt.scatter(x,y)


keep = ["Mother_education", "Num_children"]
db = data[keep].dropna()
db.head()
model = sm.OLS.from_formula("Mother_education~Num_children", data=db)
result = model.fit()
plt.show()