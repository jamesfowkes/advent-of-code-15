import sys
from random import shuffle

from collections import namedtuple
from itertools import chain

Replacement = namedtuple('Replacement', ['frm', 'to'])

def joinit(iterable, delimiter):
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x

def read_input():

    replacements = []
    for l in sys.stdin:
        l = l.strip()
        if len(l) == 0:
            break;

        l = l.split(" => ")
        replacements.append(Replacement(l[0], l[1]))

    molecule = sys.stdin.readline().strip()

    return replacements, molecule

def find_indexes_of(haystack, needle):
    return [i for i, item in enumerate(haystack) if item == needle]

def find_replacements(replacement, molecule):

    parts = molecule.split(replacement.frm)
    parts = list(joinit(parts, replacement.frm))
    indexes = find_indexes_of(parts, replacement.frm)

    new_molecules = []
    for i in indexes:
        new_molecule = parts.copy()
        new_molecule[i] = replacement.to
        new_molecules.append(''.join(new_molecule))
  
    return new_molecules

def has_at_least_one_substring(haystack, needles):
    return any([needle in haystack for needle in needles])

def get_replacement_to_list(replacements):
    return [r.to for r in replacements]

def replace_to_with_from(molecule, replacements):
    this_count = 0
    for replacement in replacements:
        if replacement.to in molecule:
            this_count += molecule.count(replacement.to)
            molecule = molecule.replace(replacement.to, replacement.frm)
            print(molecule)

    return molecule, this_count

def reduce_molecule(molecule, replacements):

    this_count = 0
    to_list = get_replacement_to_list(replacements)

    while has_at_least_one_substring(molecule, to_list):
        molecule, count = replace_to_with_from(molecule, replacements)
        this_count += count

    return molecule, this_count

def find_shortest_path(molecule, replacements, target):
    this_count = 0
    while molecule != target:
        molecule, count = reduce_molecule(molecule, replacements)
        this_count += count
        if count == 0:
            shuffle(replacements)
            molecule = original
            this_count = 0

    return this_count

if __name__ == "__main__":

    replacements, molecule = read_input()

    # Part 1
    new_molecules = [find_replacements(r, molecule) for r in replacements]
    new_molecules = list(chain(*new_molecules))

    print(len(set(new_molecules)))

    # Part 2

    original = molecule
    count = find_shortest_path(molecule, replacements, "e")
    
    print(count)
