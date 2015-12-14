import sys
from parse import parse

def draw_grid(grid):

	to_join = ['\n']
	for line in grid:
		for val in line:
			if val:
				to_join.append("*")
			else:
				to_join.append("-")
		to_join.append("\n")

	return ''.join(to_join)

def get_grid(x, y, val):
	return [[val] * x for i in range(y)]

def grid_sum(grid):
	return sum([sum(line) for line in grid])

def turn_on(grid, x, y):
	grid[y][x] = True
	return grid

def turn_off(grid, x, y):
	grid[y][x] = False
	return grid
	
def toggle(grid, x, y):
	grid[y][x] = not grid[y][x]
	return grid

def change_brightness(grid, x, y, change):
	grid[y][x] += change
	grid[y][x] = max(0, grid[y][x])
	return grid

def parse_instruction(instruction):
	return parse("{:d},{:d} through {:d},{:d}", instruction).fixed

def process_grid_instruction(grid, instruction, fn, *args):
	for x in range(instruction[0], instruction[2]+1):
		for y in range(instruction[1], instruction[3]+1):
			grid = fn(grid, x, y, *args)

	return grid

def process_grid(grid, instruction):

	if instruction.startswith("turn on"):
		instruction = parse_instruction(instruction[8:])
		#grid = process_grid_instruction(grid, instruction, turn_on)
		grid = process_grid_instruction(grid, instruction, change_brightness, 1)
	elif instruction.startswith("turn off"):
		instruction = parse_instruction(instruction[9:])
		#grid = process_grid_instruction(grid, instruction, turn_off)
		grid = process_grid_instruction(grid, instruction, change_brightness, -1)

	elif instruction.startswith("toggle"):
		instruction = parse_instruction(instruction[7:])
		#grid = process_grid_instruction(grid, instruction, toggle)
		grid = process_grid_instruction(grid, instruction, change_brightness, 2)

	else:
		print("Unknown instruction {}".format(instruction))

	return grid

if __name__ == "__main__":

	grid = get_grid(1000, 1000, False)

	for instruction in sys.stdin:
		grid = process_grid(grid, instruction)
		#print( process_grid(grid, instruction) )
	
	print(grid_sum(grid))