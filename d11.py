import sys
import string

PAIRS = ""
STRAIGHTS = ""

def increment_char(c):

	if c == "z":
		return "a"
	else:
		return chr(ord(c) + 1)

def increment_pwd(pwd):
	
	pwd = list(pwd)

	i = len(pwd) - 1

	pwd[i] = increment_char(pwd[i])

	while pwd[i] == 'a' and i >= 0:
		i -= 1
		pwd[i] = increment_char(pwd[i])		

	return "".join(pwd)

def does_not_contain(pwd, letters):
	return all([l not in pwd for l in letters])

def has_different_pairs(pwd):
	pair_counts = [pwd.count(pair) for pair in PAIRS]
	return len([c for c in pair_counts if c > 0]) > 1

def has_straight(pwd):
	return any([s in pwd for s in STRAIGHTS])

def valid(pwd):

	valid = True
	valid &= does_not_contain(pwd, "iol")
	valid &= has_different_pairs(pwd)
	valid &= has_straight(pwd)

	return valid

def make_pairs():
	return [l+l for l in string.ascii_lowercase]

def make_straight(c, length):

	chars = [c] * length

	for i in range(1, length):
		chars[i] = increment_char(chars[i - 1])
		
	return "".join(chars)

def make_straights(length):

	return [make_straight(l, length) for l in string.ascii_lowercase[:-(length-1)]]

if __name__ == "__main__":

	PAIRS = make_pairs()
	STRAIGHTS = make_straights(3)

	pwd = increment_pwd(sys.argv[1])
	
	while not valid(pwd):
		pwd = increment_pwd(pwd)
		
	print(pwd)


