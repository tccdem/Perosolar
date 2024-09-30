import re
import math
from numpy import log as ln
import pandas as pd
filename='1946classic'
with open(filename+'.csv') as fp:
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
A_radius_dict={'NH4':'170','HA':'226','HY':'220','Az':'284','FA':'277','IM':'303','DiMA':'296',
            '3-Py':'272','EA':'299','GUA':'280','TetraMA':'301','TiZ':'320','TroP':'333','MA':'238',
            'i-BuA':'360','DiEA':'385','TriMA':'304','i-PA':'307','PhA':'388','AA':'300','Py':'322','FM':'190','Cs':'167'}


B_radius_dict={'Be':'45','Mg':'72','Ca':'100','Sr':'118','Ba':'135','Mn':'83','Fe':'78','Co':'74.5','Ni':'69','Pd':'86','Pt':'80',
'Cu':'73','Zn':'74','Cd':'95','Hg':'102','Ge':'73','Sn':'115','Pb':'119','Ag':'94','Cr':'80','Ti':'86','V':'79',
'Hf':'109','Ga':'62','Te':'221','Zr':'109','W':'93','Mo':'93','In':'104'}

X_radius_dict={'F':'129','Cl':'181','Br':'196','I':'220'}

df['B-radius'] = df['B'].map(B_radius_dict).astype(float)
df['A1-radius'] = df['A1'].map(A_radius_dict).astype(float)
df['A2-radius'] = df['A2'].map(A_radius_dict).astype(float)
df['X-radius'] = df['X'].map(X_radius_dict).astype(float)
df['A-radius'] = (df['A1-radius'] + df['A2-radius'])/2
print(df['X-radius'])
a=math.sqrt(2)
nA=float(1)
df['AdivB'] =df['A-radius']/ df['B-radius']
results=[]
for i in df['AdivB']:
        result = ln(i)
        results.append(result)
#print(results)
df['ln(AdivB)'] = results
df['OctahedralFactor']= df['B-radius']/df['X-radius']
df['ToleranceFactor']= (df['A-radius']+df['X-radius'])/(a*(df['X-radius']+df['B-radius']))
df['NEWToleranceFactor']= (df['X-radius']/df['B-radius'])-(nA*(nA-(df['AdivB']/df['ln(AdivB)'])))
df.to_csv(filename+'_Tol_Oct_features'+'.csv')