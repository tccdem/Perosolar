import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
df = pd.read_csv('y_and_pred_test_model_56.csv')
dff = pd.read_csv('y_and_pred_train_model_56.csv')
y_train=dff['y_train']
predictions_train=dff['predictions_train']
y_test=df['y_test']
predictions_test=df['predictions_test']
z=round(max(y_test))
w=round(min(y_test))
c=round(max(y_train))
d=round(min(y_train))
Max=max(z,c)
Min=min(w,d)
#print(Max, Min)
#plt.subplot(1, 2, 1)
plt.figure(figsize=(12,10))
plt.scatter(y_test, predictions_test, linestyle="--", marker="o", alpha=0.6, color='coral', label="predictions")
plt.scatter(y_train, predictions_train, linestyle="--", marker="o", alpha=0.6, color='royalblue', label="predictions")
plt.legend(('Test set', 'Training set'),loc='upper left', shadow=True , fontsize=10)
plt.plot(y_test, y_test , color='black')
plt.ylabel('Predicted Formation Energy (eV)', fontsize=20)
plt.xlabel('Given Formation Energy(eV)' ,fontsize=20)
plt.xticks(np.arange(Min, Max, 1),size=18)
plt.yticks(np.arange(Min, Max, 1),size=18)
plt.grid(True)
plt.grid(True)
with open("accuracies_model_56.txt") as f:
    data = f.read()
    data = data.split('\n')
    MSE_test, R2_test, RMSD_test, MAD_test = data[1].split('=')[1], data[2].split('=')[1], data[3].split('=')[1], data[4].split('=')[1]
    MSE_train, R2_train, RMSD_train, MAD_train = data[5].split('=')[1], data[6].split('=')[1], data[7].split('=')[1], data[8].split('=')[1]
plt.text(5,-1,"MSE test : {}".format(round(float(MSE_test), 3)),bbox=dict(boxstyle="round",color='c') )
plt.text(5,-1.5,"R2 test: {}".format(round(float(R2_test), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-2,"RMSD test: {}".format(round(float(RMSD_test), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-2.5,"MAD test: {}".format(round(float(MAD_test), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-3,"MSE train : {}".format(round(float(MSE_train), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-3.5,"R2 train: {}".format(round(float(R2_train), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-4,"RMSD train: {}".format(round(float(RMSD_train), 3)),bbox=dict(boxstyle="round",color='c'))
plt.text(5,-4.5,"MAD train: {}".format(round(float(MAD_train), 3)),bbox=dict(boxstyle="round",color='c'))
plt.show()
#plt.savefig('error_plot')
