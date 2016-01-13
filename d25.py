import sys
import unittest

def get_next_number(n):
	return (n * 252533) % 33554393

def get_strip(n, last=0):
	if n == 1:
		return [20151125]
	
	next = get_next_number(last)
	strip = []
	for _ in range(n):
		strip.append(next)
		next = get_next_number(next)

	return strip

def get_grid(n):

	results = [get_strip(1)]

	for s in range(2, n+1):
		results.append(get_strip(s, results[s-2][-1]))

	return results

def get_diagonal(row, col):
	return row+col-1

def get_number_at_row_col(row, col):

	grid = get_grid(get_diagonal(row, col))
	return grid[-1][col-1]

if __name__ == "__main__":

	row = int(sys.argv[1])
	col = int(sys.argv[2])

	print(get_number_at_row_col(row, col))

class D25Tests(unittest.TestCase):

	def test_get_next_number(self):

		self.assertEqual(31916031, get_next_number(20151125))
		self.assertEqual(18749137, get_next_number(31916031))

	def test_get_array(self):

		expected = [[20151125]]
		actual = get_grid(1)
		self.assertEqual(expected, actual)

		expected = [[20151125], [31916031, 18749137]]
		actual = get_grid(2)
		self.assertEqual(expected, actual)

		expected = [
			[20151125],
			[31916031, 18749137],
			[16080970, 21629792, 17289845],
			[24592653, 8057251, 16929656, 30943339],
			[77061, 32451966, 1601130, 7726640, 10071777],
			[33071741, 17552253, 21345942, 7981243, 15514188, 33511524]
		]
		
		actual = get_grid(6)
		
		self.assertEqual(expected, actual)

	def test_get_diagonal(self):

		self.assertEqual(1, get_diagonal(1, 1))
		
		self.assertEqual(2, get_diagonal(2, 1))
		self.assertEqual(2, get_diagonal(1, 2))

		self.assertEqual(3, get_diagonal(3, 1))
		self.assertEqual(3, get_diagonal(2, 2))
		self.assertEqual(3, get_diagonal(1, 3))

	def test_get_number_at_row_col(self):

		self.assertEqual(20151125, get_number_at_row_col(1, 1))
		self.assertEqual(8057251, get_number_at_row_col(3, 2))
		self.assertEqual(31663883, get_number_at_row_col(5, 6))
		