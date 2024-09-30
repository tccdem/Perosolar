import matplotlib.pyplot as plt
import numpy as np
feature_names = ['PymatgenData mean group', 'NEWToleranceFactor', 'ToleranceFactor', 'PymatgenData std_dev mendeleev_no', 'A1-radius', 'PymatgenData std_dev block', 'PymatgenData std_dev atomic_radius', 'A2-radius', 'PymatgenData std_dev X', 'OctahedralFactor', 'PymatgenData std_dev melting_point', 'X-electro_negativity', 'B-Electro-negativity', 'B-radius']
# getting values against each value of y
feature_importance=[  2.49246105,   3.36128889,   3.38885848,   5.78294603,   6.46565476,
   7.44358696 ,  7.62265156,   9.06867937,  10.29190294,  11.48861893,
  30.25296747,  34.83118254,  78.50148219, 100.        ]
feature_importance, feature_names = zip(*sorted(zip(feature_importance, feature_names)))
print(type(feature_names), type(feature_importance))

x=np.arange(1,len(feature_names)+1)
plt.barh(x,feature_importance,alpha = 0.80, hatch = '///',align='center',color='cornflowerblue', edgecolor='royalblue')
plt.yticks(x,feature_names,fontsize=11)
plt.xticks(fontsize=13)
plt.minorticks_on()
plt.tight_layout()
plt.savefig("FeatureImportance.png",dpi=300)