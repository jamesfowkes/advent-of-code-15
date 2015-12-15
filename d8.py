import sys

def escape(s):

	new_string = ["\""]

	for c in s:
		if c == '"':
			c = '\\\"'
		elif c == '\\':
			c = ('\\\\')

		new_string.append(c)

	new_string.append("\"")

	return ''.join(new_string)

def parse(s):
	s = s[1:-1]
	return bytes(s, "utf-8").decode("unicode_escape")

def process_string(s, fn):

	literal_length = len(s)

	parsed_length = len(fn(s))

	return (literal_length, parsed_length)

if __name__ == "__main__":

	strings = [s for s in sys.stdin]

	lengths = [process_string(l, parse) for l in strings]

	result = sum([l[0] - l[1] for l in lengths])

	print (result)

	lengths = [process_string(l, escape) for l in strings]

	result = sum([l[1] - l[0] for l in lengths])

	print (result)