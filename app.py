from flask import Flask, render_template,request, redirect
import sampling
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('task.html')

@app.route('/about')
def about():
    return render_template('aboutData.html')


@app.route('/task1a',methods=['GET'])
def task1A():
    dataStrat=sampling.stratifiedSampling()
    dataRandom=sampling.randomSampling()
    data={"stratifiedSampling":dataStrat,"randomSampling":dataRandom}
    return render_template('task.html',taskJS="task1a",data=data)

@app.route('/task1b',methods=['GET','POST'])
def task1B():
    dataOriginal=pd.io.json.read_json(sampling.originalData())
    #dataOriginal.drop(['A15'], axis=1)
    del dataOriginal['A15']

    dataRandom=pd.io.json.read_json(sampling.randomSampling())
    del dataRandom['A15']

    dataStrat=pd.io.json.read_json(sampling.stratifiedSampling())
    del dataStrat['A15']

    def kmeansElbow(data):
        dictionary={}
        for i in range(1,10):
            km = KMeans(n_clusters=i)
            #kmeans for stratified sampled data
            alldistances = km.fit(data)
            #totalDistance = np.min(alldistances, axis=1).sum()
            dictionary[i]=alldistances.inertia_#totalDistance/i;

        return dictionary

    dictOriginal=kmeansElbow(dataOriginal)
    dictRandom=kmeansElbow(dataRandom)
    dictStrat=kmeansElbow(dataStrat)



    dict=[dictOriginal,dictRandom,dictStrat]
    # kmeansData=pd.DataFrame({"clusters":[clusters],"avgDistance":[avgDistance]})
    kmeansData=pd.DataFrame(dict)
    data=kmeansData.to_json()
    return render_template('task.html',taskJS="task1b",data=data)

@app.route('/task2a',methods=['GET'])
def task2A():
    dataOriginal=pd.io.json.read_json(sampling.originalData())
    #dataOriginal.drop(['A15'], axis=1)
    del dataOriginal['A15']

    dataRandom=pd.io.json.read_json(sampling.randomSampling())
    del dataRandom['A15']

    dataStrat=pd.io.json.read_json(sampling.stratifiedSampling())
    del dataStrat['A15']


    def intrinsicDim(data):
        x = StandardScaler().fit_transform(data)
        A = np.asmatrix(x.T) * np.asmatrix(x)
        U, S, V = np.linalg.svd(A)
        eigVals = S**2 / np.sum(S**2)

        cumulative=[sum(eigVals[:i]) for i in range(1,15)]

        intrinsicDim=pd.DataFrame({"dimension":[np.arange(1,15)],"eigenValues":[eigVals],"cumulativeEigVals":[cumulative]})
        return intrinsicDim.to_json()

    #Original Data
    intrinsicDimOrg=intrinsicDim(dataOriginal)
    intrinsicDimRand=intrinsicDim(dataRandom)
    intrinsicDimStrat=intrinsicDim(dataStrat)


    data=[intrinsicDimOrg,intrinsicDimRand,intrinsicDimStrat]
    data=pd.DataFrame(data)
    data=data.to_json()
    return render_template('task.html',taskJS="task2a",data=data)

@app.route('/task3a',methods=['GET'])
def task3A():

    dataOriginal=pd.io.json.read_json(sampling.originalData())
    dataOriginalY=dataOriginal['A15']
    del dataOriginal['A15']
    dataOriginal = StandardScaler().fit_transform(dataOriginal)

    dataRandom=pd.io.json.read_json(sampling.randomSampling())
    dataRandomY=dataRandom['A15']
    del dataRandom['A15']
    dataRandom = StandardScaler().fit_transform(dataRandom)

    dataStrat=pd.io.json.read_json(sampling.stratifiedSampling())
    dataStratY=dataStrat['A15']
    del dataStrat['A15']
    dataStrat = StandardScaler().fit_transform(dataStrat)

    pca = PCA(n_components = 2)

    originalPCA = pca.fit_transform(dataOriginal)

    randomPCA = pca.fit_transform(dataRandom)

    stratPCA = pca.fit_transform(dataStrat)


    data=[originalPCA,dataOriginalY,randomPCA,dataRandomY,stratPCA,dataStratY]
    data=pd.DataFrame(data)
    data=data.to_json()
    return render_template('task.html',taskJS="task3a",data=data)

if __name__== "__main__":
    app.run(debug=True)
