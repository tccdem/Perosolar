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


numOfRuns = 3000
for k in range(numOfRuns):
    df = pd.read_csv("SortedTetra_1642_14feas.csv")
    feature_names = df.columns.values[1:]
    Xold = df.iloc[:, 1:-1]
    yold = df.iloc[:, -1]
    indicesToRemove = []
    Xold, yold = shuffle(Xold, yold, random_state=None)
    # filter the data
    for i in range(len(yold)):
        if yold[i] > 9.0 or yold[i] < 0.001:
            indicesToRemove.append(i)
    X = Xold.drop(indicesToRemove)
    y = yold.drop(indicesToRemove)
    # ###############################################

    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.75)
    X_train, y_train = X[:offset], y[:offset]
    X_test, y_test = X[offset:], y[offset:]

    # ###############################################
    # Model
    # create and fit the best regression model
    params = {
        "n_estimators": 800,
        "max_depth": 5,
        "min_samples_split": 4,
        "learning_rate": 0.085,
        "loss": "lad",
    }
    best_model = ensemble.GradientBoostingRegressor(**params)

    best_model.fit(X_train, y_train)
    filename = "ModelLAD_" + str(k) + ".sav"
    print(filename)
    pickle.dump(best_model, open(filename, "wb"))
    # make predictions using the model
    predictions = best_model.predict(X_test)
    predictions_train = best_model.predict(X_train)

    print("Errors with different metrics for TEST")
    print("[INFO] MSE : {}".format(round(mean_squared_error(y_test, predictions), 7)))
    print("[INFO] R2 : {}".format(round(r2_score(y_test, predictions), 7)))
    print(
        "[INFO] RMSD : {}".format(
            round(mean_squared_error(y_test, predictions, squared=False), 7)
        )
    )
    print("[INFO] MAD : {}".format(round(mean_absolute_error(y_test, predictions), 7)))

    print("Errors with different metrics for TRAIN")
    print(
        "[INFO] MSE : {}".format(
            round(mean_squared_error(y_train, predictions_train), 7)
        )
    )
    print("[INFO] R2 : {}".format(round(r2_score(y_train, predictions_train), 7)))
    print(
        "[INFO] RMSD : {}".format(
            round(mean_squared_error(y_train, predictions_train, squared=False), 7)
        )
    )
    print(
        "[INFO] MAD : {}".format(
            round(mean_absolute_error(y_train, predictions_train), 7)
        )
    )

    # Feature importance
    print("feature_ names and importances:")
    print(feature_names)
    feature_importance = best_model.feature_importances_
    # make importances relative to max importance
    feature_importance = 100 * (feature_importance / feature_importance.max())
    print(feature_importance)

    # Save predictions for train and test
    saveDictTest = {"yTest": y_test, "yTestPreds": predictions}
    df = pd.DataFrame(saveDictTest)
    df.to_csv("PredictionsTest_" + str(k) + ".csv", index=False)
    saveDictTrain = {"yTrain": y_train, "yTrainPreds": predictions_train}
    df = pd.DataFrame(saveDictTrain)
    df.to_csv("PredictionsTrain_" + str(k) + ".csv", index=False)
