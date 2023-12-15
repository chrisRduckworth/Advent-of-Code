from functools import reduce

def calc_new_value(current, char):
    current += ord(char)
    current *= 17
    current %= 256
    return current

def calc_value(step):
    """calculates the value of a sequence"""
    total = reduce(calc_new_value, step, 0)
    return total

if __name__ == "__main__":
    with open("inputs/day_15.txt") as f:
        sequence = f.read().split(",")
        total = sum(calc_value(step) for step in sequence)
        print(total, "< total")
