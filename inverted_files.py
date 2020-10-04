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

inv_files=dict()
for w in dictionary:
    inv_files[w]=set()
    for i, content in enumerate(contents):
        if w in content:
            inv_files[w].add(i)

full={i for i in range(len(file_paths))}
request="'Messi' or 'Barca'"
request=request.replace('and','&').replace('or','|').replace('xor','^')
keys=re.findall(r"not '\w+'|'\w+'", request)
ops=re.findall(r'[&|^]',request)
ops.insert(0, '&')
res=full.copy()


try:
    for i in range(len(keys)):
        key=re.search(r"'(\w+)'",keys[i]).group().replace("'","")
        temp=set()
        if 'not ' in keys[i]:
            temp=full - inv_files[key]
        else:
            temp=inv_files[key]
        res=eval('res {} {}'.format(ops[i],temp))
    res=list(res)
    for i in res:
        title=re.search(r'(\w+)\.txt', file_paths[i]).group(1)
        title=title.replace('_',' ').center(2*len(title),'-')
        print(title, contents[i], sep='\n')
except:
    print('Khong co ket qua phu hop')