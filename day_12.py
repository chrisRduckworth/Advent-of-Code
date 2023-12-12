from itertools import product
import re

def create_all_springs(length):
    """returns all possible springs of a given length"""
    return ["".join(comb) for comb in product(".#", repeat=length)]

def filter_matching_springs(spring, possible_springs):
    """returns springs which match the . and ? of the input spring"""
    matching_springs = []
    for p_spring in possible_springs:
        if all(char == "?" or char == p_spring[i] for i, char in enumerate(spring)):
            matching_springs.append(p_spring)
    return matching_springs

def filter_broken_springs(damaged_springs, possible_springs):
    """returns those springs with correct numbers of broken springs"""
    # just find the number of damaged springs as a tuple and compare
    valid_springs = []
    for spring in possible_springs:
        broken_springs = re.findall(r"#+", spring)
        damaged_tuple = tuple(int(len(m)) for m in broken_springs)
        if damaged_springs == damaged_tuple:
            valid_springs.append(possible_springs)
    return valid_springs

def sum_possibilities(springs):
    """sums the possible number of spring combinations"""
    # you can be clever here with claculating the length of the
    # possibilities (eg 1,1,3 has min length 7) or:
    # instead of actually calculating how many possibilities for each,
    # lets just make a bit list of all possible combinations 
    # and filter them
    pass
