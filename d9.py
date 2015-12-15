import sys
from itertools import permutations

def parse_line(l):

	parts = l.split(" ")

	return (parts[0], parts[2], int(parts[4]))

if __name__ == "__main__":

	parsed = [parse_line(l) for l in sys.stdin]

	places = set([p[0] for p in parsed])

	candidate_routes = permutations(places, len(places))

	distances = [distance(r) for r in candidate_routes]
		