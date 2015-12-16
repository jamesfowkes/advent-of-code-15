import sys
from operator import add
from collections import namedtuple

Reindeer = namedtuple('Reindeer', ['speed', 'move_duration', 'rest_duration'])

def get_reindeer(l):
	values = l.split(" ")
	return Reindeer(int(values[3]), int(values[6]), int(values[13]))

def moving_at_time(r, time):
	
	full_duration = r.move_duration + r.rest_duration

	remaining = time % full_duration

	return remaining <= r.move_duration and not remaining == 0 

def race(r, position, time):

	if moving_at_time(r, time):
		return position + r.speed
	else:
		return position

def get_point_if_position_is_max(pos, _max):
	return 1 if pos == _max else 0

def get_points(points, positions):

	m = max(positions)

	new_points = [get_point_if_position_is_max(p, m) for p in positions]
	
	return list(map(add, points, new_points))

if __name__ == "__main__":

	reindeer = [get_reindeer(l) for l in sys.stdin]
	points = [0] * len(reindeer)
	positions = [0] * len(reindeer)

	seconds = int(sys.argv[1])

	for s in range(1, seconds+1):
		positions = [race(r, p, s) for r, p in zip(reindeer, positions)]
		points = get_points(points, positions)
	
	print(max(positions))
	print(max(points))
