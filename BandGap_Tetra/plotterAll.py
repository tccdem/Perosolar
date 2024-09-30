import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

df_test = pd.read_csv("PredictionsTest_21.csv")
testReal = df_test.iloc[:, 0]
testPred = df_test.iloc[:, -1]

df_train = pd.read_csv("PredictionsTrain_21.csv")
trainReal = df_train.iloc[:, 0]
trainPred = df_train.iloc[:, -1]

plt.scatter(
    trainReal,
    trainPred,
    linestyle="-",
    marker="o",
    alpha=0.5,
    s=30,
    color="dodgerblue",
    label="predictions",
)
plt.scatter(
    testReal,
    testPred,
    linestyle="-",
    marker="o",
    alpha=0.5,
    s=30,
    color="orangered",
    label="predictions",
)
plt.legend(("Training Set", "Test Set"), loc="upper left", shadow=True, fontsize=14)
plt.plot(trainReal, trainReal, color="black")
plt.ylabel(r"Predicted $E_{gap}$ (eV)", fontsize=16)
plt.xlabel(r"Calculated $E_{gap}$ (eV)", fontsize=16)

plt.grid(True, alpha=0.2)
ax = plt.gca()
ax.set_facecolor("whitesmoke")
ratio = 1.0
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(np.fabs((xright - xleft) / (ybottom - ytop)) * ratio)
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%.1f"))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter("%.1f"))
plt.tick_params(axis="both", which="major", labelsize=13)
plt.minorticks_on()
plt.tight_layout()
plt.savefig("Tetra_BG_LAD21.pdf", dpi=600, bbox_inches="tight")
