import re
import os
import numpy as np
import math


def calc_tf_idf(path):
    files=[os.path.join(path, f) for f in os.listdir(path)]
    contents=[]
    words=set()
    for file in files:
        with open(file,encoding="utf8") as f:
            string=f.read()
            string=re.sub(r'[^-/\w\s]','',string).split()
            contents.append(string)
            words.update(string)
    words=list(words)
    model=dict()
    N=len(contents)
    idf_vector=[]
    for w in words:
        model[w]=dict()
        for i,d in enumerate(contents):
            c=d.count(w)
            # tf
            if c:
                tf=c/len(d)
                model[w][i]=tf
        #idf
        idf=1+math.log10(N/len(model[w]))
        idf_vector.append(idf)
        
    #tf-idf
    for i,w in enumerate(model.keys()):
        for d in model[w].keys():
            model[w][d]*=idf_vector[i]
    return model,files, contents

path=r'C:\Users\HELLO\Desktop\data'
model,files,contents=calc_tf_idf(path)
query='Messi Barca'
keys=query.split()
docs={i for i in range(len(contents))}
try:
    for k in keys:
        d=model[k].keys()
        docs=docs & d
    docs=list(docs)
    res=[]
    for d in docs:
        vector=[]
        for k in keys:
            vector.append(model[k][d])
        vector=np.array(vector)
        norm=np.linalg.norm(vector)
        res.append((d, norm))
    res.sort(reverse=True,key=lambda x: x[1])
    print(len(res),'ket qua tim kiem:')
    for i in res:
        print(files[i[0]], i[1])
        print(contents[i[0]])
except:
    print('Khong tim thay ket qua')

    
            
    