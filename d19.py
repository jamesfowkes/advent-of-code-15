import sys

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
    
if __name__ == "__main__":

    replacements, molecule = read_input()

    new_molecules = [find_replacements(r, molecule) for r in replacements]
    new_molecules = list(chain(*new_molecules))

    print(len(set(new_molecules)))