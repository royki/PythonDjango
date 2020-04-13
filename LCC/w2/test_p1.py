import unittest
import p1

class Test_p1(unittest.TestCase):
	"""test is_palindrom_v1"""

	def test_empty_string(self):
		actual = p1.is_palindrom_v1('')
		expected = True
		self.assertEqual(actual, expected)

	def test_single_char(self):
		actual = p1.is_palindrom_v1('a')
		expected = True
		self.assertEqual(actual, expected)

	def test_2_char_yes(self):
		actual = p1.is_palindrom_v1('aa')
		expected = True
		self.assertEqual(actual, expected)

	def test_2_char_non(self):
		actual = p1.is_palindrom_v1('ab')
		expected = False
		self.assertEqual(actual, expected)

	def test_3_char_yes(self):
		actual = p1.is_palindrom_v1('aba')
		expected = True
		self.assertEqual(actual, expected)

	def test_3_char_non(self):
		actual = p1.is_palindrom_v1('abc')
		expected = False
		self.assertEqual(actual, expected)

	def test_word_even_length(self):
		actual = p1.is_palindrom_v1('redder')
		expected = True
		self.assertEqual(actual, expected)

	def test_word_even_length_non(self):
		actual = p1.is_palindrom_v1('renter')
		expected = False
		self.assertEqual(actual, expected)

	def test_word_odd_length(self):
		actual = p1.is_palindrom_v1('racecar')
		expected = True
		self.assertEqual(actual, expected)

	def test_word_odd_length_non(self):
		actual = p1.is_palindrom_v1('banana')
		expected = False
		self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main(exit=False)

