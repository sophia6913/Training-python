import sys
with open(sys.argv[1]) as f:
	for line in f:
		string = line.split(", ")
		print string
for i in range(0, len(string)-1):
	b = sorted(string[i][1])
for i in b:
	print i 
