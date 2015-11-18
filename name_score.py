import sys
count = 3

def add(string):
	sum = 0
	for i in range(0, len(string)):
		sum += ord(string[i]) - 64
	return sum	

with open(sys.argv[1]) as f:
	for line in f:
		string = line.split(", ")

seg = [i.strip('"\n') for i in string ]
seg.sort()
print seg

summarize = [add(i) for i in seg]
result = [summarize[i] * (i+1) for i in range(0, count)]
print result	
