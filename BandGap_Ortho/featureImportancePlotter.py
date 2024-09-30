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
    33.41170842,
    26.90518469,
    69.36840731,
    16.28981737,
    100.0,
    96.46422943,
    87.38015812,
    58.98843489,
    84.97035051,
    64.78497733,
    78.10649295,
    44.77707901,
    84.16374866,
    69.40344075,
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
plt.savefig("FeaImp_OrthoBG_LAD2178.pdf", dpi=600, bbox_inches="tight")
