import sys

class Reindeer:

	def __init__(self, values):
		self.name = values[0]
		self.speed = values[1]
		self.move_duration = values[2]
		self.rest_duration = values[3]
		
		self.moving = True

		self.timer = 0
		self.distance = 0
		self.points = 0

	def add_point(self):
		self.points += 1

	def stop_moving(self):
		self.moving = False
		self.timer = 0

	def start_moving(self):
		self.moving = True
		self.timer = 0
		
	def move(self):
		self.distance += self.speed
		if self.timer == self.move_duration:
			self.stop_moving()
	
	def rest(self):
		if self.timer == self.rest_duration:
			self.start_moving()
			
	def race(self):
		self.timer += 1

		if self.moving:
			self.move()
		else:
			self.rest()

	def __repr__(self):
		return "{} d = {}, p = {}".format(self.name, self.distance, self.points)

def parse_line(l):

	parts = l.split(" ")

	return (parts[0], int(parts[3]), int(parts[6]), int(parts[13]))

def race(reindeer):
	for r in reindeer:
		r.race()

def get_distance_leaders(reindeer):
	m = max(reindeer, key = lambda r: r.distance)
	return [r for r in reindeer if r.distance == m.distance]

def get_points_leaders(reindeer):
	m = max(reindeer, key = lambda r: r.points)
	return [r for r in reindeer if r.points == m.points]

if __name__ == "__main__":

	reindeer = [Reindeer(parse_line(l)) for l in sys.stdin]
	points = [0] * len(reindeer)

	seconds = int(sys.argv[1])

	for s in range(seconds):
		race(reindeer)
		leaders = get_distance_leaders(reindeer)
		for l in leaders:
			l.add_point()

	print(get_distance_leaders(reindeer))
	print(get_points_leaders(reindeer))