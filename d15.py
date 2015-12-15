import sys
from itertools import combinations

BASIC_PARAMS = ("capacity", "durability", "flavor", "texture")
PARAMS = ("capacity", "durability", "flavor", "texture", "calories")
TEASPOONS = 0

class Ingredient:

	def __init__(self, l):
		parts = l.split(" ")
		self.name = parts[0][:-1]
		self.params = {
			"capacity": int(parts[2][:-1]),
			"durability": int(parts[4][:-1]),
			"flavor": int(parts[6][:-1]),
			"texture": int(parts[8][:-1]),
			"calories": int(parts[10]),
		}

	def __repr__(self):
		return "{}: {}".format(self.name, ', '.join("{} {}".format(k, v) for k, v in self.params.items()))

	def score(self, param, proportion):
		return self.params[param] * proportion


class Cookie:

	def __init__(self, ingredients, proportions):
		self.ingredients = ingredients
		self.proportions = proportions

	def param_score(self, param):
		score = sum( [i.score(param, p) for i, p in self._ingredient_proportion_zip()])
		return score if score > 0 else 0

	def basic_score(self):

		score = 1
		for p in BASIC_PARAMS:
			score *= self.param_score(p)

		return score

	def _ingredient_proportion_zip(self):
		return zip(self.ingredients, self.proportions)

	def __repr__(self):
		return ", ".join([i.name for i, p in self._ingredient_proportion_zip() if p > 0])

def increment_proportion(proportions):

	i = 0
	while(proportions[i] == 0):
		i += 1

	proportions[i] -= 1
	proportions[i+1] += 1


def get_proportions(ingredients):

	for i in range(1, len(ingredients):
		_ingredients = combinations(ingredients)
	stop_value = TEASPOONS - 1
	proportions = [0] * len(ingredients)
	proportions[0] = stop_value

	while proportions[-1] != stop_value:
		yield proportions
		increment_proportion(proportions)

def get_cookies_for_ingredients(ingredients):
	return [Cookie(ingredients, proportions) for proportions in get_proportions(ingredients)]

if __name__ == "__main__":

	TEASPOONS = int(sys.argv[1])

	ingredients = [Ingredient(l) for l in sys.stdin]
	#names = [i.name for i in ingredients]
	#ingredients = dict(zip(names, ingredients))

	cookies = get_cookies_for_ingredients(ingredients)
	for c in cookies:
		print(c)#.basic_score())

	print(len(cookies))
	#print(max(cookies, key = lambda c: c.basic_score()))