#/usr/bin/python3

import sys

def get_dimensions(box_dimension):
    return [int(n) for n in box_dimension.split("x")]

def get_smallest_perimeter(l, w, h):
    perims = [
        2*l+2*w,
        2*l+2*h,
        2*w+2*h
    ]
    return min(perims)

def get_ribbon_length(box_dimension):
    (l, w, h) = get_dimensions(box_dimension)

    length = l*w*h

    length += get_smallest_perimeter(l, w, h)

    return length

def get_smallest_area(l, w, h):
    return min(l*w, l*h, w*h)

def get_area(box_dimension):
    
    (l, w, h) = get_dimensions(box_dimension)

    basic_area = 2*l*w + 2*w*h + 2*h*l

    basic_area += get_smallest_area(l, w, h)

    return basic_area
    
if __name__ == "__main__":

    area = 0
    dimensions = [dim for dim in sys.stdin]

    for dim in dimensions:
        area += get_area(dim)

    print(area)

    length = 0
    for dim in dimensions:
        length += get_ribbon_length(dim)

    print(length)
