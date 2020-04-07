# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 01:25:01 2020

@author: Kunal
"""

import stratified_sampling
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

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