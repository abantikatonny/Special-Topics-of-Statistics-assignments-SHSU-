import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from mlxtend.feature_selection import SequentialFeatureSelector as sfs

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r'Crime2a.csv', skipfooter=1, engine='python')
df.head()

# split the dataframe into dependent and independent variables.
X = df[['state','violent','metro','white','hs','poverty']]
Y = df['murder']

# since the state is a string datatype column we need to encode/flatten it.
X = pd.get_dummies(X)
print(X.shape)

# Splitting dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

y_train = Y_train.ravel()
y_test = Y_test.ravel()

print('Training dataset shape:', X_train.shape, y_train.shape)
print('Testing dataset shape:', X_test.shape, y_test.shape)

# Build RF classifier to use in feature selection
clf = RandomForestClassifier(n_estimators=5, n_jobs=-1)

sfs1 = sfs(clf,
           k_features=3,
           forward=True,
           floating=False,
           verbose=2,
           scoring='accuracy',
           cv=5)

# Perform SFFS
sfs1 = sfs1.fit(X_train, y_train)
feat_cols = list(sfs1.k_feature_idx_)
print('features were selected: ', feat_cols)


