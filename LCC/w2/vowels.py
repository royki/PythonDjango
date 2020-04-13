def collect_vowels(s):
	''' (str) -> str

	>>> collect_vowels('Happy Anniversary!')
	'aAiea'
	>>> collect_vowels('xyz')
	''
	'''
	vowels = ''

	for char in s:
		if char in 'aeiouAEIOU':
			vowels = vowels + char
	return vowels

def count_vowels(s):
	''' (str) -> str
	>>> count_vowels('Happy Anniversary!')
	5
	>>> count_vowels('xyz')
	0
	'''

	num_vowels = 0

	for char in s:
		if char in 'aeiouAEIOU':
			num_vowels = num_vowels + 1
	return num_vowels

if __name__ == '__main__':
	import doctest
	doctest.testmod()