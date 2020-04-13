class  WordplayStr(str):
	""" A string that can report whether is has intresting properties."""

	def same_start_and_end(self):
		""" (WordplayStr) -> bool

		Precondition: len(self) != 0
		
		>>> s = WordplayStr('abracadabra')
		>>> s.same_start_and_end()
		True
		>>> s = WordplayStr('canoe')	
		>>> s.same_start_and_end()
		False
		>>> type(s)
		<class '__main__.WordplayStr'>
		"""

		return self[0] == self[-1]



if __name__ == '__main__':
	import doctest
	doctest.testmod()
