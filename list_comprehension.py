def add(x):
 n = range(1, x+1)
 return sum(i*i*(-1) if i%2 ==0 else i*i for i in n)
 
