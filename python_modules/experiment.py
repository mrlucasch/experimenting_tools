import pandas as pd
import json



def help():
    print("Available Functions:")
    print("read_data(fname,dropnan=False)")
    print("jsonify(graph_location,name,description,config,data,tags)")
    print("readJSON(fname)")



def read_data(fname,dropnan=False):
    df= pd.read_csv(fname,sep=",",header=0)
    if dropnan:
        df = df.dropna(axis=1, how='all')
    return df




def jsonify(graph_location,name,description,config,data,tags):
    job = {}
    job["graph"] = name
    job["location"] = graph_location
    job["desc"] = description
    job["config"] = config
    job["dataset"] = data
    job["tags"] = tags
    
    with open(name+".json", 'w') as f:
        json.dump(job, f)

def readJSON(fname):
    with open(filename, 'r') as f:
        datastore = json.load(f)
    return datastore