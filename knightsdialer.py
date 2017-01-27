import unittest
import functools

JUMPS = {1: [6,8],
		 2: [7,9],
		 3: [4,8],
		 4: [0, 3, 9],
		 5: [],
		 6: [0, 1, 7],
		 7: [2, 6],
		 8: [1, 3],
		 9: [2, 4],
		 0: [4, 6]}

"""
For a given number of steps, find how many distinct sequences can be dialed
if the dialer starts at a given digit
@params n number of steps to take (positive integer)
		starting_digit digit on which the knight begins for this set of steps
@return number of possible permutations the knight can dial

Assume: the knight starts on the starting_digit, so with 0 steps the sequence 
has at least the starting_digit
"""
@functools.lru_cache(maxsize=1000)
def distinct_numbers(n, starting_digit):
	permutations = 0
	if n == 0 or starting_digit == 5:
		return 1
	elif n == 1:
		return len(JUMPS[starting_digit])
	else:
		for v in JUMPS[starting_digit]:
			permutations += distinct_numbers(n-1, v)

		return permutations




""" Unit tests """
class TestDistinctNumbers(unittest.TestCase):
	def test_basic(self):
		self.assertEqual(distinct_numbers(0, 1), 1)
		self.assertEqual(distinct_numbers(1, 1), 2)
		self.assertEqual(distinct_numbers(2, 1), 5)
		self.assertEqual(distinct_numbers(3, 1), 10)
		self.assertEqual(distinct_numbers(4, 1), 26)
		self.assertEqual(distinct_numbers(5, 1), 52)

		self.assertEqual(distinct_numbers(0, 5), 1)
		self.assertEqual(distinct_numbers(20, 5), 1)

	def test_big(self):
		# Full disclosure I did not actually calculate 10+ steps by hand
		self.assertEqual(distinct_numbers(10, 1), 3728)
		self.assertEqual(distinct_numbers(15, 1), 204416)
		self.assertEqual(distinct_numbers(20, 1), 14672384)
		# Here's where it broke the first time
		self.assertEqual(distinct_numbers(21, 1), 29344768)
		self.assertEqual(distinct_numbers(30, 1), 57746685952)
		self.assertEqual(distinct_numbers(31, 1), 115493371904)
		self.assertEqual(distinct_numbers(100, 1), 844717965965394256507071038618599424)
		self.assertEqual(distinct_numbers(200, 1), 753313133821826203276956718401772983484755669601920300079340912719691776)
		# Successfully reached 464 but the numbers got annoyingly long; max recursion depth reached at 465



if __name__ == '__main__':
	unittest.main()