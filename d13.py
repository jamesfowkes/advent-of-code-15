import sys
from itertools import permutations
from pairwise import pairwise

def parse_line(l):

	parts = l.split(" ")

	points = int(parts[3])
	if parts[2] == "lose":
		points = -points

	return (parts[0], parts[10][:-2], points)

def get_people_from_table(table):

	return set([p[0] for p in table])

def get_points_for_a_next_to_b(a, b, table):

	points = 0
	for p in table:
		if p[0] == a and p[1] == b:
			points += p[2]
		if p[0] == b and p[1] == a:
			points += p[2]

	return points

def get_points(arrangement, table):

	arrangement = list(arrangement)
	arrangement.append(arrangement[0])
	points = 0

	for a, b in pairwise(arrangement):
		points += get_points_for_a_next_to_b(a, b, table)

	return points

def add_person(name, score, table, existing_people):
	
	for person in existing_people:
		table.append((name, person, 0))

if __name__ == "__main__":

	points_table = [parse_line(l) for l in sys.stdin]
	
	people = get_people_from_table(points_table)

	add_person("me", 0, points_table, people)

	people = get_people_from_table(points_table)

	candidate_seating = list(permutations(people, len(people)))

	points = [get_points(candidate, points_table) for candidate in candidate_seating]

	print (max(points))