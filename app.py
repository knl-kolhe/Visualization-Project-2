from flask import Flask, render_template,request, redirect
import stratified_sampling
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('task.html')

@app.route('/about')
def about():
    return render_template('aboutData.html')


@app.route('/task1a',methods=['GET'])
def task1A():
    dataStrat=stratified_sampling.stratifiedSampling()
    dataRandom=stratified_sampling.randomSampling()
    data={"stratifiedSampling":dataStrat,"randomSampling":dataRandom}
    return render_template('task.html',taskJS="task1a",data=data)

@app.route('/task1b',methods=['GET','POST'])
def task1B():
    dataStrat=stratified_sampling.stratifiedSampling()
    dataRandom=stratified_sampling.randomSampling()
    sampledData=pd.io.json.read_json(dataStrat)
    clusters=[]
    avgDistance=[]
    dict={}
    for i in range(1,10):
        km = KMeans(n_clusters=i)
        alldistances = km.fit_transform(sampledData)
        totalDistance = np.min(alldistances, axis=1).sum()
        dict[i]=totalDistance/i;
        clusters.append(i)
        avgDistance.append(totalDistance/i)


    # kmeansData=pd.DataFrame({"clusters":[clusters],"avgDistance":[avgDistance]})
    kmeansData=pd.DataFrame(dict,index=[0])
    data=kmeansData.to_json()
    return render_template('task.html',taskJS="task1b",data=data)

if __name__== "__main__":
    app.run(debug=True)
