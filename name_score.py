import sys
count = 3
seg = []
summarize = []	
dict = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
with open(sys.argv[1]) as f:
	for line in f:
		string = line.split(", ")
#		print string
for i in string:
	str_stripped = i.strip('"\n') 
	seg.append(str_stripped)
	seg.sort()
print seg
k = 1
for i in seg:
	sum = 0
	for j in range(0, len(i)):
		sum += dict[i[j]]
	result = sum * k
	summarize.append(result)
	k += 1
print summarize
		
