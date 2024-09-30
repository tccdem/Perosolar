# Classic Features
"""
Created on Tue Apr  5 14:58:16 2022

@author: Fati_JMLI
"""
A_radius_dict={'NH4':'170','HA':'226','HY':'220','Az':'284','FA':'277','IM':'303','DiMA':'296',
            '3-Py':'272','EA':'299','GUA':'280','TetraMA':'301','TiZ':'320','TroP':'333','MA':'238', 
            'i-BuA':'360','DiEA':'385','TriMA':'304','i-PA':'307','PhA':'388','AA':'300','Py':'322','FM':'190','Cs':'167'}

B_electro_dict={'Be':'1.57','Mg':'1.31','Ca':'1','Sr':'0.95','Ba':'0.89','Mn':'1.55','Fe':'1.83','Co':'1.88','Ni':'1.91',
            'Pd':'2.2','Pt':'2.28','Cu':'1.9','Zn':'1.65','Cd':'1.69','Hg':'2','Ge':'2.01','Sn':'1.96','Pb':'2.33','Ag':'1.93',
            'Cr':'1.66','Ti':'1.54','V':'1.63','Hf':'1.3','Ga':'1.81','Te':'2.1','Zr':'1.33','W':'2.36','Mo':'2.16','In':'1.78'}

B_radius_dict={'Be':'45','Mg':'72','Ca':'100','Sr':'118','Ba':'135','Mn':'83','Fe':'78','Co':'74.5','Ni':'69','Pd':'86','Pt':'80',
'Cu':'73','Zn':'74','Cd':'95','Hg':'102','Ge':'73','Sn':'115','Pb':'119','Ag':'94','Cr':'80','Ti':'86','V':'79',
'Hf':'109','Ga':'62','Te':'221','Zr':'109','W':'93','Mo':'93','In':'104'}

X_radius_dict={'F':'3.98','Cl':'3.16','Br':'2.96','I':'2.66'}

import re
import pandas as pd
with open('Sorted1946_OrthoGLLBSC_SOC_NegElim1713.csv') as fp:
    a=next(fp)
    #print(a)
    df = pd.DataFrame(columns=['A1','A2','B','X'])
    for line in fp:
        A1A2BX3=line.split(",")[0]
        #print(A1A2BX3)
        A1,A2,BX3=A1A2BX3.split("_")
        B,X=re.sub( r"([A-Z])", r" \1", BX3).split()
        r = re.compile("([a-zA-Z]+)([0-9]+)")
        m = r.match(X) 
        X=m.group(1)
        #print(A1,A2,B,X)
        df = df.append({'A1':A1 , 'A2':A2,'B':B,'X':X}, ignore_index=True)
    #display(df)
df['X-electro_negativity'] = df['X'].map(X_radius_dict)
df['B-radius'] = df['B'].map(B_radius_dict)
df['B-Electro-negativity'] = df['B'].map(B_electro_dict)
df['A1-radius'] = df['A1'].map(A_radius_dict)
df['A2-radius'] = df['A2'].map(A_radius_dict)
df.to_csv("1946classicfeatures.csv")