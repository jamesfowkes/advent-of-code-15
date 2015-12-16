import sys
import string

from collections import namedtuple

from parse import parse

def strip_punctuation(s):
	return ''.join([c for c in s if c not in string.punctuation])

def get_sue(l):

	parts = l.split(" ")
	parts = list(map(strip_punctuation, parts))

	return {
		"num" : int(parts[1]),
		parts[2] : int(parts[3]),
		parts[4] : int(parts[5]),
		parts[6] : int(parts[7]),
	}

def get_info(l):

	parts = l.split(" ")
	parts = list(map(strip_punctuation, parts))

	return [parts[0], int(parts[1])]

def match_sue_on_item(sue, k, v):
	match = None
	if k in sue:

		if k in ["cats", "trees"]:
			match = v < sue[k]

		elif k in ["pomeranians", "goldfish"]:
			match = v > sue[k]
		else:
			match = v == sue[k]

	return match

def match_sue(sue, info):
	matches = [match_sue_on_item(sue, k, v) for k, v in info.items()]
	matches = all([m for m in matches if m is not None])

	return sue if matches else None

def eliminate_sues(sues, info):
	sues = [match_sue(sue, info) for sue in sues]
	sues = [sue for sue in sues if sue]

	return sues

if __name__ == "__main__":

	n = int(sys.argv[1])

	lines = [l for l in sys.stdin]

	sues = list(map(get_sue, lines[0:n]))

	info = map(get_info, lines[n:])
	info = {k:v for k, v in info}

	sues = eliminate_sues(sues, info)

	print(sues[0]['num'])