def is_perfect(num):
	a = []
	sum = 0
	for i in range(1, (num//2)+1):
		if num % i == 0:
			sum += i
	if sum == num:
		return 'True'
	else:
		return 'False'


is_perfect(28)
