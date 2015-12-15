import sys

def process_next_chars(s):

	count = 1;

	if len(s) == 1:
		return ("", "1{}".format(s[0]))

	while s[0] == s[count]:
		count += 1

	new = "{}{}".format(count, s[0])
	s = s[count:]
	
	return (s, new)

def process(s):

	new = []

	while len(s):
		s, next = process_next_chars(s)
		new.append(next)

	return ''.join(new)

if __name__ == "__main__":

	s = sys.argv[1]
	n = int(sys.argv[2])
	for _ in range(n):
		print(_)
		s = process(s)

	print(len(s))

