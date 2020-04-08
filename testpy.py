# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 01:25:01 2020

@author: Kunal
"""

import sampling
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

dataStrat=stratified_sampling.stratifiedSampling()
dataRandom=stratified_sampling.randomSampling()
dataStrat=pd.io.json.read_json(dataStrat)
dataRandom=pd.io.json.read_json(dataRandom)


clusters=[]
avgDistance=[]
for i in range(1,10):
    km = KMeans(n_clusters=i)
    alldistances = km.fit_transform(sampledData)
    totalDistance = np.min(alldistances, axis=1).sum()
    clusters.append(i)
    avgDistance.append(totalDistance/i)

kmeansData=pd.DataFrame({"clusters":[clusters],"avgDistance":[avgDistance]})
data=kmeansData.to_json()




dataOriginal=sampling.originalData()
dataOriginalY=dataOriginal['A15']
del dataOriginal['A15']
dataOriginal = StandardScaler().fit_transform(dataOriginal)
pca = PCA(n_components = 2)

originalPCA = pca.fit_transform(dataOriginal)
red=[]
blue=[]
for i in range(len(originalPCA)):
    if dataOriginalY[i]==0:
        red.append(originalPCA[i,:])
    else:
        blue.append(originalPCA[i,:])
red=np.array(red)
blue=np.array(blue)
plt.scatter(red[:,0],red[:,1],c='r')
plt.scatter(blue[:,0],blue[:,1],c='b')
plt.show()