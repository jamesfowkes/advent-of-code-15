import unittest

from d7 import Instruction, run_instructions

class d7Test(unittest.TestCase):

	def test_nullary_instruction_parser(self):
		instruction = "123 -> g"
		parsed = Instruction(instruction)
		self.assertEqual(instruction, str(parsed))

	def test_unary_instruction_parser(self):
		instruction = "NOT ad -> g"
		parsed = Instruction(instruction)
		self.assertEqual(instruction, str(parsed))

	def test_binary_instruction_parser(self):
		instruction = "ad RSHIFT rg -> bf"
		parsed = Instruction(instruction)
		self.assertEqual(instruction, str(parsed))

	def test_nullary_instruction(self):
		instruction = "123 -> g"
		result = run_instructions([instruction], "g")
		expected = 123
		self.assertEqual(expected, result)

	def test_unary_instruction(self):
		instruction = "NOT 5647 -> g"
		result = run_instructions([instruction], "g")
		expected = 59888
		self.assertEqual(expected, result)

	def test_binary_and_instruction(self):
		instruction = "61248 AND 5647 -> g"
		result = run_instructions([instruction], "g")
		expected = 1536
		self.assertEqual(expected, result)

	def test_binary_or_instruction(self):
		instruction = "25436 OR 5328 -> g"
		result = run_instructions([instruction], "g")
		expected = 30684
		self.assertEqual(expected, result)

	def test_binary_rshift_instruction(self):
		instruction = "17834 RSHIFT 3 -> g"
		result = run_instructions([instruction], "g")
		expected = 2229
		self.assertEqual(expected, result)

	def test_binary_lshift_instruction(self):
		instruction = "346 LSHIFT 4 -> g"
		result = run_instructions([instruction], "g")
		expected = 5536
		self.assertEqual(expected, result)

	def test_chained_nonary_instruction(self):
		instructions = [
			"123 -> lg",
			"lg -> a"
		]

		result = run_instructions(instructions, "a")
		expected = 123
		self.assertEqual(expected, result)

	def test_chained_unary_instruction(self):
		instructions = [
			"NOT 123 -> lg",
			"lg -> a"
		]

		result = run_instructions(instructions, "a")
		expected = 65412
		self.assertEqual(expected, result)

	def test_chained_binary_instruction(self):
		instructions = [
			"7654 AND 123 -> lg",
			"lg -> a"
		]

		result = run_instructions(instructions, "a")
		expected = 98
		self.assertEqual(expected, result)

	def test_multiply_chained_binary_instruction(self):
		instructions = [
			"432 OR 5325 -> ff",
			"ff AND 123 -> lg",
			"lg -> a"
		]

		result = run_instructions(instructions, "a")
		expected = 121
		self.assertEqual(expected, result)

if __name__ == "__main__":
	unittest.main()