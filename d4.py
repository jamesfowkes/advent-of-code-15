import sys
import hashlib

if __name__ == "__main__":

	_input = sys.argv[1]
	nzeros = int(sys.argv[2])

	result = ""
	suffix = 0
	test = "0" * nzeros
	while not result.startswith(test):
		key = "{0}{1}".format(_input, suffix)
		result = hashlib.md5(key.encode('utf-8')).hexdigest()
		suffix += 1

	print("{} -> {}".format(key, result))
	print(suffix-1)
