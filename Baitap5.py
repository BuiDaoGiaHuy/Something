import re
import os
import numpy as np
import math

def files_contents_words(path):
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
    return files, contents, words

def calc_tf_idf(words, contents):       
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
    return model,idf_vector

#Norm2
def Norm2(model,words, idf_vector,query):
    content_query=query.split()
    words_query=list(set(content_query))
    vector_query=[]
    res=[]
    try:
        for i in words_query:
            tf=content_query.count(i)/len(content_query)
            idf=idf_vector[words.index(i)]
            vector_query.append(tf*idf)
        vector_query=np.array(vector_query)

        docs_set=set()
        for i in words_query:
            docs_set.update(model[i].keys())
        docs_set=list(docs_set)
        for i in docs_set:
            vt=list()
            for j in words_query:
                vt.append(model[j].setdefault(i,0))
            vt=np.array(vt)
            res.append((i,np.linalg.norm(vt-vector_query))) #
        res.sort(key=lambda x: x[1])
        return res
    except:
        return None

#Cosine
def Cosine(model,words, idf_vector,query):
    content_query=query.split()
    words_query=list(set(content_query))
    vector_query=[]
    res=[]
    try:
        for i in words_query:
            tf=content_query.count(i)/len(content_query)
            idf=idf_vector[words.index(i)]
            vector_query.append(tf*idf)
        vector_query=np.array(vector_query)

        docs_set=set()
        for i in words_query:
            docs_set.update(model[i].keys())
        docs_set=list(docs_set)
        for i in docs_set:
            vt=list()
            for j in words_query:
                vt.append(model[j].setdefault(i,0))
            vt=np.array(vt)
            cos=(vt@vector_query)/(np.linalg.norm(vt)*np.linalg.norm(vector_query))
            res.append((i,cos))
        res.sort(reverse=True,key=lambda x: x[1])
        return res
    except:
        return None

#Scalar
def Scalar(model,words, idf_vector,query):
    content_query=query.split()
    words_query=list(set(content_query))
    vector_query=[]
    res=[]
    try:
        for i in words_query:
            tf=content_query.count(i)/len(content_query)
            idf=idf_vector[words.index(i)]
            vector_query.append(tf*idf)
        vector_query=np.array(vector_query)

        docs_set=set()
        for i in words_query:
            docs_set.update(model[i].keys())
        docs_set=list(docs_set)
        for i in docs_set:
            vt=list()
            for j in words_query:
                vt.append(model[j].setdefault(i,0))
            vt=np.array(vt)
            SProduct=vt@vector_query
            res.append((i,SProduct))
        res.sort(reverse=True,key=lambda x: x[1])
        return res
    except:
        return None

path=r'C:\Users\HELLO\Desktop\data'
files, contents, words=files_contents_words(path)
model,idf_vector=calc_tf_idf(words, contents)

query='Messi Barca'
print(Scalar(model,words,idf_vector,query))
print(Norm2(model,words,idf_vector,query))
print(Cosine(model,words,idf_vector,query))


# =============================================================================
#     print(len(res),'ket qua tim kiem:')
#     for i in res:
#         print(files[i[0]], i[1])
#         print(contents[i[0]])
#         
# print('Khong tim thay ket qua')
# =============================================================================
