def add(x):
 n = range(1, x+1)
 return sum([n[i]*n[i] if i%2 ==0 else n[i]*n[i]*(-1) for i in range(0, len(n))])
 
