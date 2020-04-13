class WorldplayStr(str):
	"""docstring for WorldplayStr"""
	
	def same_start_and_end(self):
		""" (WorldplayStr) -> bool 
		PrecondtionL len(self) != 0

		Retunrn whether self starts and ends with the same letter.

		>>> s = WorldplayStr('abracadabra')
		>>> s.same_start_and_end()
		True
		"""
		return self[0] == self[-1]


if __name__ == '__main__':
	import doctest
	doctest.testmod()

		