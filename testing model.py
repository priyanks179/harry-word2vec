# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:11:14 2018

@author: Kartik
"""

import re
import numpy as np
from gensim import corpora, models, similarities
import nltk
from clean_text import clean_sent
import pickle

filename='word2vec.bin'
model = pickle.load(open(filename, 'rb'))
word2int = pickle.load(open('word2int', 'rb'))
model.most_similar(positive=['ron'], topn=7)

word2vec,vectors={},[]
for word,count in word2int.items():
    if word in model.wv.vocab:
        word2vec[word]=model[word].tolist()
        vectors.append(model[word].tolist())
#remove word not in word2vec
for word in list(word2int.keys()):
    if word not in list(word2vec.keys()):
       del word2int[word] 

int2word={}
for word,count in word2int.items():
    int2word[count]=word
     
        
from sklearn.manifold import TSNE
model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
vectors = model.fit_transform(np.asarray(vectors))

from sklearn import preprocessing
normalizer = preprocessing.Normalizer()
vectors =  normalizer.fit_transform(np.asarray(vectors), '2')

for i,vec in enumerate(vectors):
    vectors[i]=[vec[0],vec[1]]



import matplotlib.pyplot as plt
fig, ax = plt.subplots()
for word,_ in word2int.items():
#    print(word, vectors[word2int[word]][1])
    if word=='harry':
        ax.annotate(word, (vectors[word2int[word]][0],vectors[word2int[word]][1] ),textcoords='offset points',xycoords='data',arrowprops=dict(arrowstyle="->"))
    else:
        ax.annotate(word, (vectors[word2int[word]][0],vectors[word2int[word]][1] ))
plt.show()

