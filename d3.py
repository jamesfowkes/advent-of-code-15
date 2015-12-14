#/usr/bin/python3

import sys
from collections import Counter

def next_location(location, direction):

	if direction == "^":
		return (location[0], location[1] + 1)

	elif direction == ">":
		return (location[0] + 1, location[1])

	if direction == "v":
		return (location[0], location[1] - 1)

	if direction == "<":
		return (location[0] - 1, location[1])

def process_directions(directions):
	houses = {
		(0, 0): 1
	}
	location = (0, 0)

	for direction in directions:

		location = next_location(location, direction)

		if location in houses:
			houses[location] += 1
		else:
			houses[location] = 1

	return houses

if __name__ == "__main__":

	directions = [line for line in sys.stdin]

	directions = ''.join([direction.strip() for direction in directions])

	even_directions = directions[::2]
	odd_directions = directions[1::2]

	even_houses = Counter(process_directions(even_directions))
	odd_houses = Counter(process_directions(odd_directions))

	print(len(even_houses + odd_houses))