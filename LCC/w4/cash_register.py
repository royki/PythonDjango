class CashRegister:
	"""docstring for CashRegister"""

	def __init__(self, loonies, toonies, fives, tens, twenties):
		""" (CashRegister, int, int, int, int, int) -> NoneType
		>>> register = CashRegister(5, 5, 5, 5, 5)
		>>> register.loonies 
		5
		>>> register.toonies
		5
		>>> register.fives
		5
		>>> register.tens
		5
		>>> register.twenties
		5
		"""
		# Instance variables
		self.loonies = loonies
		self.toonies = toonies
		self.fives = fives
		self.tens = tens
		self.twenties = twenties

	def __str__(self):
		"""
		>>> reg1 = CashRegister(1,2,3,4,5)
		>>> reg1.__str__()
		CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)
		"""
		return 'CashRegister: ' + \
				'${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})'.format(self.get_total(), self.loonies,
					self.toonies, self.fives, self.tens, self.twenties)
		# return 'CashRegister: $' + str(self.get_total()) + ' ($1x' + str(self.loonies) + \
		# 		', $2x' + str(self.toonies) + ', $5x' + str(self.fives) + ', $10x' + \
		# 		str(self.tens) + ', $20x' + str(self.twenties) + ')'

	def __eq__(self, other):
		""" (CashRegister, CashRegister ) -> bool
		>>> reg1 = CashRegister(2, 0, 0, 0, 0)
		>>> reg2 = CashRegister(0, 1, 0, 0, 0)
		>>> reg1 == reg2
		True
		"""
		return self.get_total() == other.get_total()

	def get_total(self):
		""" (CashRegister) -> int
		>>> register = CashRegister(5, 5, 5, 5, 5)
		>>> register.get_total()
		190
		>>> register.add(3, 'toonies')
		>>> register.remove(2, 'twenties')
		>>> register.get_total()
		156
		"""
		return self.loonies + self.toonies*2 + self.fives*5 + self.tens*10 + self.twenties*20

	def add(self, count, denom):
		""" (CashRegister, int, str) -> NoneType
		Add count items of the denom to the register.
		denom is one of loonies, toonies, fives, tens, twenties

		>>> register = CashRegister(5, 5, 5, 5, 5)
		>>> register.add(2, 'toonies')
		
		>>> register.add(1, 'tens')
		>>> register.tens
		6
		"""
		if denom == 'loonies':
			self.loonies += count
		elif denom == 'toonies':
			self.toonies += count
		elif denom == 'fives':
			self.fives += count
		elif denom == 'tens':
			self.tens += count
		elif denom == 'twenties':
			self.twenties += count

	def remove(self, count, denom):
		""" (CashRegister, int, str) -> NoneType
		Remove count items of the denom to the register.
		denom is one of loonies, toonies, fives, tens, twenties

		>>> register = CashRegister(5, 5, 5, 5, 5)
		>>> register.remove(2, 'toonies')
		
		>>> register.remove(1, 'tens')
		>>> register.tens
		4
		"""
		if denom == 'loonies':
			self.loonies -= count
		elif denom == 'toonies':
			self.toonies -= count
		elif denom == 'fives':
			self.fives -= count
		elif denom == 'tens':
			self.tens -= count
		elif denom == 'twenties':
			self.twenties -= count
	

if __name__ == '__main__':
	# A cash register with 5 loonies, 5 fives, 5 tens and 5 twenties
	# for a total of $190
	register = CashRegister(5, 5, 5, 5, 5)
	print(register.get_total())

	register.add(3, 'toonies')
	register.remove(2, 'twenties')
	print(register.get_total())

	cr1 = CashRegister(2, 0 ,0 ,0, 0)
	cr2 = CashRegister(0, 1 ,0 ,0, 0)
	cr3 = CashRegister(1, 1 ,0 ,0, 0)

	print(cr1)
	print(cr2)

	print(cr1 == cr2)
	print(cr2 == cr3)

	import doctest
	doctest.testmod()
