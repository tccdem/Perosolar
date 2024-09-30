import glob
f2 = glob.glob("errors/*.txt")
all_text=""
big_dict={}
for f in f2:
    f = open(f,"r")
    lines = f.readlines()
    #print(lines)
    my_dict={}
    name=lines[0]
    name=name.strip()
    score=lines[1]
    score=score.strip()
    value=score.split('=')
    mse_test=value[0]
    mse=value[1]
    #print(name, score, type(mse))
    my_dict[name]=float(mse)
    big_dict.update(my_dict)
    min_mse = min(big_dict, key=big_dict.get)
display(big_dict)
print('minimum:',min_mse)