import sys
count = 3
b = [0] * count	
'''
def mysort(mylist):
	print "mylist:", mylist
	length = len(mylist)-1
	while length > 0:
		for i in range(length):
			if mylist[i] > mylist[i+1]:
				mylist[i], mylist[i+1] = mylist[i+1], mylist[i]		
		length -= 1
	return mylist
'''
def mysort(mylist):
	length = len(mylist)-1
	for i in range(length):
    		for j in range(length - i):
        		if mylist[j] > mylist[j+1]:
   	         		mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
	return mylist

with open('input.txt') as f:
	a = [int(line) for line in f]

for i in a:
	if i > b[0]:
		b[0] = i
		b = mysort(b)
print b[::-1]
	
