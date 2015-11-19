def fib():
	a, b= 0, 1
	while True:
		c = a + b
		a, b = b, c
		yield c

