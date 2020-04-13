#Linear Search -> Sorted and Unsorted order list 

def linear_search(L,v):
	""" (list, object) -> int 
	Int indicating the index of the object from the list if it exits otherwise -1
	>>> linear_search([2, 3, 5, 3], 2)
	0
	>>> linear_search([2, 3, 5, 3], 5)
	2
	>>> linear_search([2, 3, 5, 3], 8)
	-1
	"""
	i = 0
	length = len(L)
	
	while  i != length and v != L[i]:		
		i += 1

	if i == len(L):
		return -1
	else:
		return i

L = list(range(10000000))
print(linear_search(L, 0))

import cProfile
cProfile.run('linear_search(L, 100000000000)')

if __name__ == '__main__':
	import doctest
	doctest.testmod()

