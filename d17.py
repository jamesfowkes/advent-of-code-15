import sys
from itertools import combinations, permutations
from argparse import ArgumentParser

def get_insufficient_and_sufficient_lists(lst, n):
	cumulative_capacity = [sum(lst[0:n]) for n in range(1, len(lst))]
	insufficient = lst[0 : get_index_up_to_num(cumulative_capacity, target) + 1]
	sufficient = lst[get_index_up_to_num(cumulative_capacity, target) + 1 : ]
	
	return insufficient, sufficient

def get_possible_sums(lst):
	sums = []
	for i in range(1, len(lst)+1):
		for combination in combinations(lst, i):
			sums.append(sum(combination))

	return sums

def get_index_up_to_num(lst, n):

	lst = [l for l in lst if l < n]
	return len(lst)-1

def get_candidate_sums(sufficient_sums, insufficient_sums):
	candidate_sums = []

	for s in sufficient_sums:
		for i in insufficient_sums:
			candidate_sums.append(s + i)

	return candidate_sums		

def get_targets(sufficient_list, insufficient_sums, target):

	sufficient_sums = get_possible_sums(sufficient_list)
	sufficient_sums = list(filter(lambda x: x <= target, sufficient_sums))
	
	candidate_sums = get_candidate_sums(sufficient_sums, insufficient_sums)
	
	target_sums = list(filter(lambda x: x == target, candidate_sums))

	return target_sums

def parse_args():

	parser = ArgumentParser()
	parser.add_argument("target")
	parser.add_argument("-m", "--min", action="store_true")

	return parser.parse_args()

def find_lowest_sums_to_meet_target(capacities, target):
	capacities = sorted(capacities, reverse = True)
	
	i = 1
	sums = []
	while len(sums) == 0:
		sums = map(sum, combinations(capacities, i))
		sums = list(filter(lambda x: x == target, sums))
		i += 1

	return len(sums), i-1

if __name__ == "__main__":

	args = parse_args()

	target = int(args.target)

	capacities = sorted(list(map(int, sys.stdin)))
	
	if args.min:
		n_combs, containers = find_lowest_sums_to_meet_target(capacities, target)
		print ("Minimum to reach {}l is {} containers, {} combinations.".format(target, containers, n_combs))

	else:
		insufficient_list, sufficient_list = get_insufficient_and_sufficient_lists(capacities, target)
		insufficient_sums = get_possible_sums(insufficient_list)
		target_sums = get_targets(sufficient_list, insufficient_sums, target)

		print("{} items in insufficient list: {}".format(len(insufficient_list), insufficient_list))
		print("{} items in sufficient list: {}".format(len(sufficient_list), sufficient_list))
		print("{} combinations meet target {}.".format(len(target_sums), target))
	