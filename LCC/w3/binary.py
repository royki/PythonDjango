#Binary Search -> Only Sorted order list

def binary_search(L, v) :
	""" (list, object) -> int 
	>>> binary_search([2, 3, 5, 6], 2)
	0
	>>> binary_search([2, 3, 5, 6], 5)
	2
	>>> binary_search([2, 3, 5, 6], 8)
	-1
	"""

	b = 0
	e = len(L) - 1

	while b <= e:
		m = (b + e) // 2
		if L[m] < v:
			b = m + 1
		else:
			e = m - 1

	if b == len(L) or L[b] != v:
		return -1
	else:
		return b


L = list(range(10000000))
print(binary_search(L, 0))

import cProfile
cProfile.run('binary_search(L, 100000000000)')

if __name__ == '__main__':
	import doctest
	doctest.testmod()

