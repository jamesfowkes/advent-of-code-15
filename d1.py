#/usr/bin/python3

import sys

class Santa:
	def __init__(self, floor, steps):
		self.floor = floor
		self.steps = steps
		self.done = False

	def step(self, c):
		if c == "(":
			next_floor = self.floor + 1
		elif c == ")":
			next_floor = self.floor - 1
		else:
			return self

		return Santa(next_floor, self.steps+1)

def process_while_above_floor(line, floor):
	santa = Santa(0, 0)

	for c in line:
		santa = santa.step(c)
		if santa.floor <= floor:
			break

	return santa.steps

def process_line(line):

	santa = Santa(0, 0)

	for c in line:
		santa = santa.step(c)

	return santa.floor

if __name__ == "__main__":
    for line in sys.stdin:
        print(process_line(line))
        print(process_while_above_floor(line, -1))
