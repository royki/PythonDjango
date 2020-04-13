def get_divisors(num, possible_divisors):
	''' (int, list of int) -> list of int

	>>> get_divisors(8, [1, 2, 3])
	[1, 2]
	>>> get_divisors(4, [-2, 0, 2])
	[-2, 2]
	'''
	divisors = []
	for item in possible_divisors:
		if item !=0 and num % item == 0: 
			divisors.append(item)

	return divisors

	# Lazy evaluation 
	# if the first operand in an and expression is False, 
	# the 'and' expression evaluates to False. The second operand is not evaluated.

if __name__ == '__main__':
	import doctest
	doctest.testmod()
