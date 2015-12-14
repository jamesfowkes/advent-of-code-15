import sys

def has_vowels(str, count):
	return len([c for c in str if c in "aeiou"]) >= count

def has_double_letters(str):

	length = len(str)

	for i in range(0, length-1):
		if str[i] == str[i+1]:
			return True

	return False

def does_not_contain_invalids(str, invalid_list):

	return all([invalid not in str for invalid in invalid_list])

def has_non_adjacent_pairs(str):
	length = len(str)

	for i in range(length-1):
		pair = str[i] + str[i+1]

		if pair in str[i+2:]:
			return True
	
	return False

def has_repeating_letters_with_spacing(str, spacing):

	length = len(str)
	for i in range(length-1-spacing):
		if str[i] == str[i+1+spacing]:
			return True

	return False

def is_nice(str):
		
	nice = True
	nice &= has_vowels(str, 3)
	nice &= has_double_letters(str)
	nice &= does_not_contain_invalids(str, ["ab", "cd", "pq", "xy"])

	return nice

def is_nice_2(str):
		
	nice = True
	nice &= has_non_adjacent_pairs(str)
	nice &= has_repeating_letters_with_spacing(str, 1)

	return nice

if __name__ == "__main__":

	nice = 0
	for line in sys.stdin:
		if is_nice_2(line.strip()):
			nice += 1

	print(nice)
