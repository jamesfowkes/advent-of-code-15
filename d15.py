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

    def calories(self):
        return self.param_score("calories")

    def __repr__(self):
        ingredients = ", ".join([i.name + " (" + str(p) + ")" for i, p in self._ingredient_proportion_zip() if p > 0])
        return ingredients + " = " + str(self.basic_score())

def increment_proportion(proportions):

    i = 0
    while(proportions[i] == 0):
        i += 1

    proportions[i] -= 1
    proportions[i+1] += 1

#def get_possible_proportions(a, existing_combination = None):
#    if existing_combination == None:
#        existing_combination = []
#
#    combosum = sum(existing_combination)
#    
#    if combosum == a:
#        print(existing_combination)
#    
#    else:
#        for number in range(1, a + 1):
#            if combosum + number <= a:
#                new_combination = existing_combination + [number]
#                
#                for c in get_possible_proportions(a, new_combination):
#                    yield c

def get_possible_proportions(a, limit, existing_combination):

    if len(existing_combination) > limit:
        raise StopIteration

    combosum = sum(existing_combination)

    if combosum == a:
        yield existing_combination
    else:
        for number in range(a - combosum, 0, -1):
            new_combination = existing_combination + [number]
            for c in get_possible_proportions(a, limit, new_combination):
                yield c
        
def get_cookies_for_ingredients(ingredients):
    
    for proportions in get_possible_proportions(TEASPOONS, len(ingredients), []):
        yield Cookie(ingredients, proportions)

if __name__ == "__main__":

    TEASPOONS = int(sys.argv[1])

    ingredients = [Ingredient(l) for l in sys.stdin]
    #names = [i.name for i in ingredients]
    #ingredients = dict(zip(names, ingredients))

    cookies = [c for c in get_cookies_for_ingredients(ingredients) if c.basic_score() > 0]
    cookies = [c for c in cookies if c.calories() == 500]

    print(max(cookies, key = lambda c: c.basic_score()))