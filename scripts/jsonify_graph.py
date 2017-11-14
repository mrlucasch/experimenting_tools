#!/usr/bin/python


import sys

import os

cwd = os.getcwd()
direct = cwd.split("/")[-1]

if direct == "scripts":
	sys.path.append(cwd + '/../python_modules/')
	import experiment

else:
	import experiment


if len(sys.argv) != 7:
	print("Usage:")
	print(sys.argv[0]+" path_to_graph experiment/filename short_description config_description path_to_data tags(comma separated")
	print("Example:")
	print("python jsonify_graph.py here congestion_graph \"Graphing showing congestion with rsync and 256mb buffers\" \"256mb 56mb buffers\" /user/lucasch/dataset \"congestion,ycsb,256mb,56mb,eurosys\"")
	exit()


graph_location = sys.argv[1]
name = sys.argv[2]
description = sys.argv[3]
config = sys.argv[4]
data =  sys.argv[5]
tags = sys.argv[6]


print("Details:")
print("graph_location: "+graph_location)
print("name: "+name)
print("description: "+description)
print("config: "+config)
print("data: "+data)
print("tags: "+tags)

tags = tags.split(",")
experiment.jsonify(graph_location,name,description,config,data,tags)