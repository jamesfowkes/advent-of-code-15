import sys
import operator
import math

import unittest 

from collections import Counter

def get_factors_with_limit(n, limit):
    factors = get_factors(n)
    factors = filter(lambda x: n/x <= limit, factors)
    return factors

def get_factors(n):
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            b = n / a
            yield int(b)
            if a != b:
                yield int(a)

def get_presents_for_house_1(house):
    factors = get_factors(house)
    return sum(factors) * 10

def get_presents_for_house_2(house):
    factors = get_factors_with_limit(house, 50)
    return sum(factors) * 11

def get_house_for_target(target, present_fn, _print=False, ):
    house = 2
    count = 10
    while count < target:
        count = present_fn(house)
        if _print and house % 1000 == 0:
            print("{} -> {}".format(house, count))
        house += 2

    return house - 2

class D20Tests(unittest.TestCase):
    def test_get_presents_for_house_1_returns_correct_count(self):
        self.assertEqual(10, get_presents_for_house_1(1))
        self.assertEqual(30, get_presents_for_house_1(2))
        self.assertEqual(40, get_presents_for_house_1(3))
        self.assertEqual(70, get_presents_for_house_1(4))
        self.assertEqual(60, get_presents_for_house_1(5))
        self.assertEqual(120, get_presents_for_house_1(6))
        self.assertEqual(80, get_presents_for_house_1(7))
        self.assertEqual(150, get_presents_for_house_1(8))
        self.assertEqual(130, get_presents_for_house_1(9))

    def test_get_factors_with_limit(self):
        self.assertCountEqual([1], get_factors_with_limit(1, 2))
        self.assertCountEqual([1, 2], get_factors_with_limit(2, 2))
        self.assertCountEqual([3], get_factors_with_limit(3, 2))
        self.assertCountEqual([2, 4], get_factors_with_limit(4, 2))
        self.assertCountEqual([5], get_factors_with_limit(5, 2))
        self.assertCountEqual([3, 6], get_factors_with_limit(6, 2))
        self.assertCountEqual([7], get_factors_with_limit(7, 2))
        self.assertCountEqual([4, 8], get_factors_with_limit(8, 2))
        self.assertCountEqual([9], get_factors_with_limit(9, 2))
        self.assertCountEqual([5, 10], get_factors_with_limit(10, 2))
        self.assertCountEqual([11], get_factors_with_limit(11, 2))
        self.assertCountEqual([6, 12], get_factors_with_limit(12, 2))

if __name__ == "__main__":

    target = int(sys.argv[1])
    part = int(sys.argv[2])

    if part == 1:
        print( get_house_for_target(target, get_presents_for_house_1, True) )
    else:
        print( get_house_for_target(target, get_presents_for_house_2, True) )
