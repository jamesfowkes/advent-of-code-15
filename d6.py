import sys
from parse import parse

def turn_on(grid, instruction):
	pass

def turn_off(grid, instruction):
	pass

def toggle(grid, instruction):
	pass

def parse_instruction(instruction):
	return parse(instruction, "{:d},{:d} through {:d},{:d}")

def process_grid(grid, instruction):

	if instruction.startswith("turn on"):
		instruction = parse_instruction(instruction[8:])
		grid = turn_on(grid, instruction)
	elif instruction.startswith("turn off"):
		instruction = parse_instruction(instruction[9:])
		grid = turn_off(grid, instruction)
	elif instruction.startswith("toggle"):
		instruction = parse_instruction(instruction[7:])
		grid = toggle(grid, instruction)

	return instruction

if __name__ == "__main__":

	grid = [[False] * 1000] * 1000

	for instruction in sys.stdin:
		#grid = process_grid(grid, instruction)
		print( process_grid(grid, instruction) )
		