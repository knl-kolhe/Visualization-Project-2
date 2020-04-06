# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 21:29:42 2020

@author: Kunal
"""

import pandas as pd
import numpy as np

#sampling
def stratifiedSampling():
    with open('data/australian.dat','r') as input_file:
       lines = input_file.readlines()
       data = []
       for line in lines:
          newLine = line.strip().split()
          data.append( newLine )
    
    data=np.array(data,dtype=np.float32)
       
    sampledData=[]
    for i in range(len(data)):
        if data[i,-1]==0 and np.random.uniform()<0.25:
            sampledData.append(data[i])
        elif data[i,-1]==1 and np.random.uniform()<0.25:
            sampledData.append(data[i])
    
    sampledData=np.array(sampledData)
    
    yVal=sampledData[:,-1]
    sampledData=np.delete(sampledData,-1,axis=1)
    
    sampledData=pd.DataFrame(sampledData,columns=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14'])
    sampledData=sampledData.to_json()
    
    return sampledData

def randomSampling():
    with open('data/australian.dat','r') as input_file:
       lines = input_file.readlines()
       data = []
       for line in lines:
          newLine = line.strip().split()
          data.append( newLine )
    
    data=np.array(data,dtype=np.float32)
       
    sampledData=[]
    for i in range(len(data)):
        if np.random.uniform()<0.25:
            sampledData.append(data[i])
    
    sampledData=np.array(sampledData)
    
    yVal=sampledData[:,-1]
    sampledData=np.delete(sampledData,-1,axis=1)
    
    sampledData=pd.DataFrame(sampledData,columns=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14'])
    sampledData=sampledData.to_json()
    
    return sampledData


        