import sys
import json

def add_numbers(j):

	num = 0

	if type(j) == dict:
		if ("red" in j.values()):
			num = 0
		else:	
			for _, v in j.items():
				num += add_numbers(v)
	elif type(j) == list:
		for v in j:
			num += add_numbers(v)
	elif type(j) == int:
		num = j

	return num

if __name__ == "__main__":

	json_raw = sys.stdin.read()

	decoded = json.loads(json_raw)

	print(add_numbers(decoded))
	