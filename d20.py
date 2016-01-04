import sys
import operator
from collections import Counter

def matches_or_exceeds(target, lst):
	return any([l >= target for l in lst])

def get_present_counts(elf, house_limit):
	counts = {}
	for e in range(elf, house_limit, elf):
		counts[e] = elf * 10
	
	return Counter(counts)

def get_presents_for_houses(house_limit):

	counts = Counter()

	for elf in range(1, house_limit+1):
		counts += get_present_counts(elf, house_limit)

	return counts

def get_presents_to_target(target):
	counts = Counter()
	house_limit = 1
	while True:
		counts += get_presents_for_houses(house_limit)
		house_limit += 1

		if matches_or_exceeds(target, counts.values()):
			return counts

if __name__ == "__main__":

	target = int(sys.argv[1])

	presents = get_presents_to_target(target)

	print(presents)
	print(max(presents.items(), key=operator.itemgetter(1)))
	