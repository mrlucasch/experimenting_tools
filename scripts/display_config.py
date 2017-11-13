#!/usr/bin/python


from prettytable import PrettyTable
import sys

if len(sys.argv) != 2:
	print("USAGE:")
	print(sys.argv[0]+" config_filename")
	print("NOTE: Make sure you have prettytable installed! You can install it by running: \n pip install prettytable")
	exit()


fname = sys.argv[1]
f = open(fname,"r")
lines = f.readlines()
f.close()
config = PrettyTable(['Config Variable', 'Value'])

for line in lines:
	parts = line.replace("\n","").split(",")

	config.add_row(parts)


print config
