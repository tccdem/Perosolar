import numpy as np
import matplotlib.pyplot as plt
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.utils import shuffle
import sys
import os
import pickle
import pandas as pd

df = pd.read_csv("17830-14f-noF.csv")
#num_of_feature = len(df.columns) - 1
feature_names = df.columns.values[1:] #eliminate structure names
#display(df)
X = df.iloc[:,1:]
#y = df.iloc[:,-1]
#print(y)
#print(X.index[np.isinf(X).any(1)])

X = X.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
X = X.astype(np.float32)

filename = 'model_70.sav'
loaded_model = pickle.load(open(filename, 'rb'))
#loaded_model.fit(X_train, y_train)

# make predictions using the model
predictions = loaded_model.predict(X)

#print("[INFO] MSE : {}".format(round(mean_squared_error(y, predictions), 7)))
#print("MSE", mean_squared_error(y, predictions)/119)
#result = loaded_model.score(X_test, y_test)
#result = loaded_model.score(X,y)
#print(result)
prediction = pd.DataFrame(predictions, columns=['predictions']).to_csv('prediction.csv')
#print(y,predictions)
