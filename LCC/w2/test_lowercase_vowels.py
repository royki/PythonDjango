import unittest
import lowercase_vowels

class TestLowerCaseVowels(unittest.TestCase):
	"""unittest of lowercase_vowels"""

	def test_zero_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('')
		expected = 0
		self.assertEqual(actual, expected)

	def test_one_char_with_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('a')
		expected = 1
		self.assertEqual(actual, expected)

	def test_one_char_without_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('b')
		expected = 0
		self.assertEqual(actual, expected)

	def test_word_zero_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('pfffft')
		expected = 0
		self.assertEqual(actual, expected)

	def test_word_some_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('bandit')
		expected = 2
		self.assertEqual(actual, expected)

	def test_word_all_vowels(self):
		actual = lowercase_vowels.count_lowercase_vowels('aeiou')
		expected = 5
		self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main(exit=False)
		