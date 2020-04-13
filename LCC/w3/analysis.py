def print_ints(n):
	""" (int) -> NoneType """

	for i in range(1, n+1):
		print(i)


def print_odd_ints(n):
	""" (int) -> NoneType """

	for i in range(1, n+1, 2):
		print(i)


def print_pairs(n):
	""" (int) -> NoneType """

	for i in range(1,n+1):
		for j in range(1, n+1):
			print(i, j)

def print_double_step(n):
	""" (int) -> NoneType """

	i = 1
	while i < n +1:
		print(i)
		i = i * 2