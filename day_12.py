from itertools import product

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

def sum_possibilities(springs):
    """sums the possible number of spring combinations"""
    # instead of actually calculating how many possibilities for each,
    # lets just make a bit list of all possible combinations 
    # and filter them
    pass
