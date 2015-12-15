import sys
from itertools import permutations

def find_distance(p1, p2, distances):

	points = (p1, p2)

	for distance in distances:
		if (distance[0] in points) and (distance[1] in points):
			return distance[2]

def distance(route, distances):

	distance = 0
	for n in range(len(route) - 1):
		distance += find_distance(route[n], route[n+1], distances)

	#print('-'.join(route) + " " + str(distance))

	return distance

def parse_line(l):

	parts = l.split(" ")

	return (parts[0], parts[2], int(parts[4]))

if __name__ == "__main__":

	distances = [parse_line(l) for l in sys.stdin]

	places = [p[0] for p in distances]
	places.extend([p[1] for p in distances])

	places = set(places)

	candidate_routes = list(permutations(places, len(places)))

	route_distances = [distance(r, distances) for r in candidate_routes]
	
	print (min(route_distances))
	print (max(route_distances))