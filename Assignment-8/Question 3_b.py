import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd 
import numpy as np 
from statsmodels.formula.api import glm
import warnings 
warnings.filterwarnings("ignore")

data = pd.read_csv('q3.csv') # load data set 

formula = 'Death_Rate ~ Age'

model = smf.glm(formula = formula, data=data, family=sm.families.Poisson(sm.families.links.log))

result = model.fit() 

print(result.summary()) 

print("Coefficeients")

print(result.params) 
print() 
print("p-Values") 
print(result.pvalues) 
print() 
print("Dependent variables") 
print(result.model.endog_names)