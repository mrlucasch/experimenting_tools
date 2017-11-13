#!/usr/bin/python


from prettytable import PrettyTable
import sys

import os 


if len(sys.argv) != 2:
	print("Usage:")
	print(sys.argv[0]+" experiment_name(This can be a single string or a path to a string.)")
	print("Experiment name will be used to write the output file.\n Example: If you use test1 then the file will be written as test1_readme.txt")
	print("If you use results/test1, then the readme will be written to results/test1_readme.txt")
	print("NOTE: Press enter twice to write to the file.")
	exit(0)


print("Why are you running this experiment?")

lines = []
while True:
    line = raw_input()
    if line:
        lines.append(line)
    else:
        break
descr = '\n'.join(lines)



#
fname = sys.argv[1]
outf =  open(fname+"_readme.txt","w")

outf.write("# Description of Experiment\n\n")
outf.write(descr)


outf.close()
