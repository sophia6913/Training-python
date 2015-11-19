def add(x):
 return sum(i*i*(-1) if i%2 ==0 else i*i for i in range(1, x+1))
 
