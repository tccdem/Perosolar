import os
import os.path

os.mkdir('prediction_test')
os.mkdir('prediction_train')
os.mkdir('errors')
os.mkdir('models')
os.mkdir('feature-impo')
for n in range(0, 300):
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

    df = pd.read_csv("4181cubicnoF-14f.csv")
    # num_of_feature = len(df.columns) - 1
    feature_names = df.columns.values[1:]  # eliminate structure names
    X = df.iloc[:, 1:-1]
    y = df.iloc[:, -1]
    X, y = shuffle(X, y)
    ################################################
    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.8)
    X_train, y_train = X[:offset], y[:offset]
    X_test, y_test = X[offset:], y[offset:]
    # print(X,y)
    # Model
    # create and fit the best regression model
    # work2-11features params-kfold2
    params = {'learning_rate': 0.1, 'loss': 'ls', 'max_depth': 5, 'min_samples_leaf': 2, 'min_samples_split': 2,
              'n_estimators': 200, 'subsample': 0.8}
    # work2-11features params-kfold2
    # params={'learning_rate': 0.1, 'loss': 'huber', 'max_depth': 6, 'min_samples_leaf': 3, 'min_samples_split': 3,
    # 'n_estimators': 300, 'subsample': 0.8}
    # params={'learning_rate': 0.08, 'loss': 'huber', 'max_depth': 6, 'min_samples_leaf': 5, 'min_samples_split': 2,
    # 'n_estimators': 800, 'subsample': 0.85}
    best_model = ensemble.GradientBoostingRegressor(**params)
    best_model.fit(X_train, y_train)
    import os

    cwd = os.getcwd()
    save_path = cwd + r'/models'
    filename = "model_{}.sav".format(n)
    completeName = os.path.join(save_path, filename)
    pickle.dump(best_model, open(completeName, 'wb'))
    # make predictions using the model
    predictions_test = best_model.predict(X_test)
    predictions_train = best_model.predict(X_train)
    # print(dir(best_model))
    # print(best_model.get_params())
    # exit()
    # save errors for test with model name in a text file
    MSE_test = round(mean_squared_error(y_test, predictions_test), 3)
    R2_test = round(r2_score(y_test, predictions_test), 3)
    RMSD_test = round(mean_squared_error(y_test, predictions_test, squared=False), 3)
    MAD_test = round(mean_absolute_error(y_test, predictions_test), 3)
    # save errors for train with model name in a text file
    MSE_train = round(mean_squared_error(y_train, predictions_train), 3)
    R2_train = round(r2_score(y_train, predictions_train), 3)
    RMSD_train = round(mean_squared_error(y_train, predictions_train, squared=False), 3)
    MAD_train = round(mean_absolute_error(y_train, predictions_train), 3)

    # 'mkdir' creates a directory in current directory.
    save_path = cwd + r'/errors'
    file_name = "accuracies_model_{}.txt".format(n)
    completeName = os.path.join(save_path, file_name)
    file1 = open(completeName, "w")
    # file = open("accuracies_model_{}.txt".format(n),"w")
    file1.write('model_%d' % n + ':' + '\n' + 'MSE_test=' + str(MSE_test) + '\n' + 'R2_test=' + str(R2_test) + '\n'
                + 'RMSD_test=' + str(RMSD_test) + '\n' + 'MAD_test=' + str(MAD_test) + '\n' + 'MSE_train=' + str(
        MSE_train) + '\n'
                + 'R2_train=' + str(R2_train) + '\n' + 'RMSD_train=' + str(RMSD_train) + '\n' + 'MAD_train=' + str(
        MAD_train)
                )

    # save prediction an real y in separete csv file for test and train for each model
    predictions_train = list(predictions_train)
    y_train = list(y_train)
    predictions_test = list(predictions_test)
    y_test = list(y_test)
    df_test = pd.DataFrame(columns=['predictions_test'])
    df_test = pd.DataFrame(columns=['y_test'])
    df_test['predictions_test'] = predictions_test
    df_test['y_test'] = y_test
    # display(df_test)
    df_test.to_csv(os.path.join('prediction_test', "y_and_pred_test_model_{}.csv".format(n)))
    # df_test.to_csv("y_and_pred_test_model_{}.csv".format(n), index=False)
    df_train = pd.DataFrame(columns=['predictions_train'])
    df_train = pd.DataFrame(columns=['y_train'])
    df_train['predictions_train'] = predictions_train
    df_train['y_train'] = y_train
    df_train.to_csv(os.path.join('prediction_train', "y_and_pred_train_model_{}.csv".format(n)))
    # df_train.to_csv("y_and_pred_train_model_{}.csv".format(n), index=False)
    ########################################################################feature importance
    feature_importance = best_model.feature_importances_
    # make importances relative to max importance
    feature_importance = 100 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0])
    f2 = []
    for m in range(len(sorted_idx)):
        f2.append(feature_names[sorted_idx[m]])
    save_path = cwd + r'/feature-impo'
    file_name = "feature-importance_model_{}.txt".format(n)
    completeName = os.path.join(save_path, file_name)
    file2 = open(completeName, "w")
    # file = open("feature-importance_model_{}.txt".format(n),"w")
    # print(pos,f2,feature_importance[sorted_idx])
    file2.write(str(pos) + '\n' + str(f2) + '\n' + str(feature_importance[sorted_idx]))

file1.close()
file2.close()