# converts maze files in json format (https://github.com/bblodget/MicromouseSim) to my format
# performs conversion on all files in directory
# Written by Matthew Tran

import sys, json, os

if len(sys.argv) != 3:
	sys.exit("Usage: convert.py <input folder> <output folder>")

def convert(s):
	n = 0
	if 'N' not in s:
		n += 8
	if 'E' not in s:
		n += 4
	if 'S' not in s:
		n += 2
	if 'W' not in s:
		n += 1
	return n

for inputfile in [i for i in os.listdir(sys.argv[1]) if ".json" in i]:
	# open json
	f = open(sys.argv[1] + "/" + inputfile, "r")
	maze = json.load(f)
	f.close()

	# convert and write to txt
	outputfile = sys.argv[2] + "/" + inputfile[0:-4] + "txt"
	f = open(outputfile, "w")
	for row in maze:
		s = ''
		for i in row:
			s += str(convert(i)) + " "
		print(s, file=f)
	f.close()