import sys
import copy
from collections import namedtuple

Grid = namedtuple('Grid', ['grid', 'rows', 'cols'])

def get_blank_grid(rows, cols):
	grid = [[0 for _x in range(cols)] for _y in range(rows)] 
	return Grid(grid, rows, cols)

def get_initial_grid():

	lines = [l.strip() for l in sys.stdin]

	rows = len(lines)
	cols = len(lines[0])

	grid = get_blank_grid(rows, cols)

	for r, line in enumerate(lines):
		for c, on_off in enumerate(line):
			grid.grid[r][c] = on_off == '#'

	return grid

def count_if_on(row, col, grid, _print=False):

	if row < 0 or col < 0:
		return 0

	try:
		return 1 if grid[row][col] else 0
	except:
		return 0

def count_neighbours(row, col, grid):

	n = 0

	n += count_if_on(row-1, col-1, grid, row==0 and col == 0)
	n += count_if_on(row-1, col, grid)
	n += count_if_on(row-1, col+1, grid)

	n += count_if_on(row, col-1, grid)
	n += count_if_on(row, col+1, grid)

	n += count_if_on(row+1, col-1, grid)
	n += count_if_on(row+1, col, grid)
	n += count_if_on(row+1, col+1, grid)

	return n

def run_grid(grid):
	new_grid = copy.deepcopy(grid.grid)

	for row in range(grid.rows):
		for col in range(grid.cols):
			neighbours = count_neighbours(row, col, grid.grid)

			if grid.grid[row][col] and (neighbours < 2 or neighbours > 3):
				new_grid[row][col] = False

			if not grid.grid[row][col] and (neighbours == 3):
				new_grid[row][col] = True

	return Grid(new_grid, grid.rows, grid.cols)

def set_on(grid, r, c):
	new_grid = copy.deepcopy(grid.grid)
	
	new_grid[r][c] = True

	return Grid(new_grid, grid.rows, grid.cols)
	
def count_on(grid):

	count = 0
	for row in grid.grid:
		for col in row:
			count += 1 if col else 0

	return count

def print_row(row):
	row = ['#' if c else '.' for c in row]
	print(''.join(row))

def print_grid(grid):

	for row in grid.grid:
		print_row(row)
	
if __name__ == "__main__":

	steps = int(sys.argv[1])

	grid = get_initial_grid()

	for s in range(steps):
		grid = run_grid(grid)
		grid = set_on(grid, 0, 0)
		grid = set_on(grid, grid.rows-1, 0)
		grid = set_on(grid, 0, grid.cols-1)
		grid = set_on(grid, grid.rows-1, grid.cols-1)

	print_grid(grid)
	print(count_on(grid))