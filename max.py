import sys

with open(sys.argv[1]) as f:
	a = []
	b = [0, 0, 0]
	count = 3
	for line in f:
		integer = int(line)
		a.append(integer)

flag = 0
while not flag:
	flag = 1
	for i in range(0, len(a)-1):
		if a[i] > a[i+1]:
			flag = 0
			a[i], a[i+1] = a[i+1], a[i]

print a[::-1][:count]
	
