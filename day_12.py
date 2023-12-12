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
    springs = springs.splitlines()
    springs = [[row.split()[0], tuple(int(n) for n in row.split()[1].split(","))] for row in springs]
    spring_lengths = set(len(spring[0]) for spring in springs)
    
    all_springs = {length: create_all_springs(length) for length in spring_lengths}

    total_possibilities = 0
    for spring in springs:
        possible_springs = filter_matching_springs(spring[0], all_springs[len(spring[0])])
        possible_springs = filter_broken_springs(spring[1], possible_springs)
        total_possibilities += len(possible_springs)
    return total_possibilities

def is_valid_possibility(spring, damaged_tuple):
    """returns bool of if the spring could be valid"""
    damaged_regexs = tuple(r"(#|\?)" * n for n in damaged_tuple)
    test_regex = r"^(\.|\?|^)+" + r"(\.|\?)+".join(damaged_regexs) + r"(\.|\?|$)+$"
    return re.search(test_regex, spring) is not None


def find_possibilities(spring, damaged_tuple):
    print(spring)
    """recursively finds the total number of possibilities for a given spring"""
    if spring.count("?") == 0:
        damaged_springs_lengths = tuple(len(s) for s in re.findall(r"#+", spring))
        if damaged_springs_lengths == damaged_tuple:
            return 1 
        return 0
        
    with_broken = spring.replace("?", "#", 1)
    broken_valid = is_valid_possibility(with_broken, damaged_tuple)
    with_ok = spring.replace("?", ".", 1)
    ok_valid = is_valid_possibility(with_ok, damaged_tuple)
    if broken_valid:
        if ok_valid:
            return find_possibilities(with_broken, damaged_tuple) + find_possibilities(with_ok, damaged_tuple)
        else:
            return find_possibilities(with_broken, damaged_tuple)
    else:
        if ok_valid:
            return find_possibilities(with_ok, damaged_tuple)
    
    return 0 

if __name__ == "__main__":
    with open("inputs/day_12.txt") as f:
        springs = f.read()
        total_possibilities = sum_possibilities(springs)
        print(total_possibilities, "< total possibilities")
