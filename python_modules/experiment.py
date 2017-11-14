import pandas as pd
import json
import uuid



def help():
    print("Available Functions:")
    print("read_data(fname,dropnan=False)")
    print("jsonify(graph_location,name,description,config,data,tags,loc=\"\")")
    print("readJSON(fname)")



def read_data(fname,dropnan=False):
    df= pd.read_csv(fname,sep=",",header=0)
    if dropnan:
        df = df.dropna(axis=1, how='all')
    return df




def jsonify(graph_location,name,description,config,data,tags,loc=""):
    job = {}
    job["graph"] = name
    job["location"] = graph_location
    job["desc"] = description
    job["config"] = config
    job["dataset"] = data
    job["tags"] = tags
    uid = str(uuid.uuid4())[:8]
    fname = loc+name+"_"+str(uid)+".json"
    with open(fname, 'w') as f:
        json.dump(job, f)
    print("Saved as: "+fname)

def readJSON(fname):
    with open(fname, 'r') as f:
        datastore = json.load(f)
    return datastore