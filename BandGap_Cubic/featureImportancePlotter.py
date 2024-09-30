import matplotlib.pyplot as plt
import numpy as np
from palettable.tableau import TableauMedium_10
from matplotlib.ticker import FormatStrFormatter


feature_names = [
    "$r_{A}$",
    "$r_{A^{\prime}}$",
    "$X_{X}$",
    "$r_{B}$",
    "$X_{B}$",
    "$\\sigma(\\kappa)$",
    "$\\sigma(MN)$",
    "$\\sigma(X)$",
    "$\\sigma(m)$",
    "$\\overline{b}$",
    "$\\sigma(T_{m})$",
    "$\mu$",
    "$t$",
    "$T$",
    "GLLBSC_SOC_BandGap",
]

feature_importance = [
    36.61626004,
    35.4714251,
    57.67803335,
    15.71250726,
    100.0,
    49.80161169,
    90.0805858,
    63.84970764,
    58.95102917,
    50.90990543,
    66.98563058,
    34.65613726,
    74.88454435,
    56.4783023,
]

divisor = 100.0
arr = np.array(feature_importance)
res = np.divide(arr, divisor)
print(res)

res, feature_names = zip(*sorted(zip(res, feature_names)))

x = np.arange(1, len(feature_names) + 1)
plt.barh(
    x,
    res,
    alpha=0.70,
    hatch="///",
    align="center",
    color="dodgerblue",
    edgecolor="mediumblue",
)
plt.yticks(x, feature_names, fontsize=17)
plt.xticks(fontsize=16)
plt.xlabel("Feature Importance", fontsize=16)
plt.grid(True, alpha=0.2)
ax = plt.gca()
ax.set_facecolor("whitesmoke")
ratio = 1.0
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(np.fabs((xright - xleft) / (ybottom - ytop)) * ratio)
plt.minorticks_on()
plt.tight_layout()
plt.savefig("FeaImp_CubicBG_LAD768.pdf", dpi=600, bbox_inches="tight")
