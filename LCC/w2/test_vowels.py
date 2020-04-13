import unittest
import vowels

class TestVowels(unittest.TestCase):
	"""unittest of vowels"""

	def test_collect_vowels(self):
		actual = vowels.collect_vowels('Happy Anniversary')
		expected = 'aAiea'
		self.assertEqual(actual, expected)

	def test_count_vowels(self):
		actual = vowels.count_vowels('xyz')
		expected = 0
		self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main(exit=False)
