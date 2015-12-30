import sys
import copy

def get_blank_grid(rows, cols):
	return [[0 for _x in range(cols)] for _y in range(rows)] 

def get_initial_grid(rows, cols):

	grid = get_blank_grid(rows, cols)
	for r, line in enumerate(sys.stdin):
		line = line.strip()
		for c, on_off in enumerate(line):
			grid[r][c] = on_off == '#'

	return grid

def count_if_on(row, col, grid):

	try:
		return 1 if grid[row-1][col-1] else 0
	except:
		return 0

def count_neighbours(row, col, grid):

	n = 0

	n += count_if_on(row-1, col-1, grid)
	n += count_if_on(row-1, col, grid)
	n += count_if_on(row-1, col+1, grid)

	n += count_if_on(row, col-1, grid)
	n += count_if_on(row, col+1, grid)

	n += count_if_on(row+1, col-1, grid)
	n += count_if_on(row+1, col, grid)
	n += count_if_on(row+1, col+1, grid)

	return n

def run_grid(grid, rows, cols):
	new_grid = copy.deepcopy(grid)

	for row in range(rows):
		for col in range(cols):
			neighbours = count_neighbours(row, col, grid)

			if grid[row][col] and (neighbours < 2 or neighbours > 3):
				new_grid[row][col] = False

			if not grid[row][col] and (neighbours == 3):
				new_grid[row][col] = True

	return new_grid

def print_row(row):
	row = ['#' if c else '.' for c in row]
	print(''.join(row))

def print_grid(grid):

	for row in grid:
		print_row(row)
	
if __name__ == "__main__":

	grid = get_initial_grid(6, 6)

	steps = int(sys.argv[1])

	for s in range(steps):
		grid = run_grid(grid, 6, 6)

	print_grid(grid)