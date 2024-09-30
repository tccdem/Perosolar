import numpy as np
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import pickle
import pandas as pd

df = pd.read_csv("ElementwiseFeas_DatasetToPredict_16288-14feas.csv")
feature_names = df.columns.values[1:]

X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

X = X.astype(np.float32)
name = df.iloc[:, 0]

filename = "ModelLAD_768.sav"
loaded_model = pickle.load(open(filename, "rb"))
# loaded_model.fit(X_train, y_train)

# make predictions using the model
predictions = loaded_model.predict(X)

data = {"names": name, "preds": predictions}
df = pd.DataFrame(data)

df.to_csv("PredictionsLAD768_16288.csv", index=False)

print("[INFO] MSE : {}".format(round(mean_squared_error(y, predictions), 7)))
print("[INFO] R2 : {}".format(round(r2_score(y, predictions), 7)))
print(
    "[INFO] RMSD : {}".format(
        round(mean_squared_error(y, predictions, squared=False), 7)
    )
)
print("[INFO] MAD : {}".format(round(mean_absolute_error(y, predictions), 7)))


# Feature importance
print("Feature Names and Importances:")
print(feature_names)
feature_importance = loaded_model.feature_importances_
# make importances relative to max importance
feature_importance = 100 * (feature_importance / feature_importance.max())
print(feature_importance)
