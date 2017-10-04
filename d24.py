import sys
import unittest

from collections import namedtuple

Instruction = namedtuple("Instruction", ['ins', 'reg', 'offset'])

def parse_instruction(ins):

	parts = ins.split()

	if len(parts) == 2:
		if parts[0] in ["hlf", "tpl", "inc"]:
			return Instruction(parts[0], parts[1], 0)
		else:
			return Instruction(parts[0], "", int(parts[1]))
	elif len(parts) == 3:
		parts[1] = parts[1][:-1]
		return Instruction(parts[0], parts[1], int(parts[2]))

def run(ins, regs, pc):

	if ins.ins == "hlf":
		regs[ins.reg] = int(regs[ins.reg] / 2)
		return pc + 1
	elif ins.ins == "tpl":
		regs[ins.reg] *= 3
		return pc + 1
	elif ins.ins == "inc":
		regs[ins.reg] += 1
		return pc + 1
	elif ins.ins == "jmp":
		return pc + ins.offset
	elif ins.ins == "jie":
		return pc + ins.offset if regs[ins.reg] % 2  == 0 else pc + 1
	elif ins.ins == "jio":
		return pc + ins.offset if regs[ins.reg] % 1  == 0 else pc + 1

class D24Tests(unittest.TestCase):

	def test_instruction_parsing(self):

		expected = Instruction("hlf", "r", 0)
		actual = parse_instruction("hlf r")
		self.assertEqual(expected, actual)

		expected = Instruction("tpl", "r", 0)
		actual = parse_instruction("tpl r")
		self.assertEqual(expected, actual)

		expected = Instruction("inc", "r", 0)
		actual = parse_instruction("inc r")
		self.assertEqual(expected, actual)

		expected = Instruction("jmp", "", -3)
		actual = parse_instruction("jmp -3")
		self.assertEqual(expected, actual)

		expected = Instruction("jie", "r", 4)
		actual = parse_instruction("jie r, 4")
		self.assertEqual(expected, actual)

		expected = Instruction("jio", "r", -2)
		actual = parse_instruction("jio r, -2")
		self.assertEqual(expected, actual)

	def test_register_instructions(self):
		registers = {"r" : 4}
		instruction = Instruction("hlf", "r", 0)
		pc = run(instruction, registers, 0)
		self.assertEqual({"r":2}, registers)
		self.assertEqual(1, pc)

		registers = {"r" : 4}
		instruction = Instruction("tpl", "r", 0)
		pc = run(instruction, registers, 0)
		self.assertEqual({"r":12}, registers)
		self.assertEqual(1, pc)

		registers = {"r" : 4}
		instruction = Instruction("inc", "r", 0)
		pc = run(instruction, registers, 0)
		self.assertEqual({"r":5}, registers)
		self.assertEqual(1, pc)

	def test_jump_instructions(self):
		instruction = Instruction("jmp", "", 2)
		pc = run(instruction, {}, 0)
		self.assertEqual(2, pc)

		instruction = Instruction("jie", "r", 0)
		run(instruction, {"r": 2} 0)
		self.assertEqual({"r":5}, registers)

		registers = {"r" : 4}
		instruction = Instruction("jio", "r", 0)
		run(instruction, None)
		self.assertEqual({"r":5}, registers)
