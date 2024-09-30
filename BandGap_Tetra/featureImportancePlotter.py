import matplotlib.pyplot as plt
import numpy as np
from palettable.tableau import TableauMedium_10
from matplotlib.ticker import FormatStrFormatter


feature_names = [
    "$r_{A}$",
    "$r_{A^{\prime}}$",
    "$X_{X}$ ",
    "$r_{B}$",
    "$X_{B}$ ",
    "$\\sigma(\\kappa)$",
    "$\\sigma(MN)$",
    "$\\sigma(X)$",
    "$\\sigma(m)$",
    "$\\overline{b}$",
    "$\\sigma(T_{m})$",
    "$\mu$",
    "$t$",
    "$T$",
]

feature_importance = [
    33.75940398,
    37.21748048,
    53.47927766,
    19.57894172,
    73.21667902,
    87.14772938,
    77.24818659,
    61.37342109,
    86.81584957,
    62.76007945,
    78.85363664,
    36.87599962,
    100.0,
    62.65304652,
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
plt.savefig("FeaImp_TetraBG_LAD21.pdf", dpi=600, bbox_inches="tight")
