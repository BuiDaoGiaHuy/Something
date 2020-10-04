import os
import re
import numpy as np

path=r'C:\Users\HELLO\Desktop\data'

file_paths=[os.path.join(path,i) for i in os.listdir(path)]
contents=[]
dictionary=set()
for f_p in file_paths:
    with open(f_p, 'r',encoding = 'utf-8') as f:
        string=f.read()
        contents.append(string)
        string=re.sub('[^/\w\s-]','',string)
        words=string.split()
        dictionary.update(set(words))
dictionary=list(dictionary)
h,w=len(dictionary),len(file_paths)
t_d_matrix=np.zeros((h, w))
for i in range(h):
    for j in range(w):
        if dictionary[i] in contents[j]:
            t_d_matrix[i][j]=1
            
rq="not 'Messi' and 'Pandora'"
keys=re.findall(r"not '\w+'|'\w+'", rq)
ops=re.findall("' (\w+)",rq)
ops.insert(0,'and')
res=np.ones(w)
try:
    for i in range(len(keys)):
        key=re.search(r"'(\w+)'",keys[i]).group().replace("'","")
        idx_key=dictionary.index(key)
        temp=t_d_matrix[idx_key]
        if 'not ' in keys[i]:
            temp=np.logical_not(temp)
        if ops[i]=='and':
            res=np.logical_and(res, temp)
        elif ops[i]=='or':
            res=np.logical_or(res, temp)
        else:
            res=np.logical_xor(res, temp)
    if np.all(res==0):
        print('Khong co ket qua phu hop')
    else:
        for i in range(w):
            if res[i]:
                title=re.search(r'(\w+)\.txt', file_paths[i]).group(1)
                title=title.replace('_',' ').center(2*len(title),'-')
                print(title, contents[i], sep='\n')
except:
    print('Khong co tu khoa tim kiem')

        
    