import re, copy
from math import prod

def get_info(system):
    """extracts rules and parts from input"""
    rules, parts = system.split("\n\n")
    rules = rules.splitlines()
    final_rules = {}
    for rule in rules:
        values = []
        rule = rule.split("{")
        rule_name = rule[0]
        rule_list = rule[1][:-1].split(",")
        
        for r in rule_list[:-1]:
            values.append(tuple(r.split(':')))
            
        values.append(rule_list[-1])
        final_rules[rule_name] = values
        
    
    parts = [part.replace("=", ":") for part in parts.splitlines()]
    parts = [re.sub(r"x|m|a|s", lambda m: f"\'{m[0]}\'", part) for part in parts]
    parts = [eval(part) for part in parts]
    
    return final_rules, parts

def eval_rule(part, rule):
    """finds result of a part through a rule"""
    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]
    for r in rule[:-1]:
        if eval(r[0]):
            return r[1]
    return rule[-1]

def eval_part(part, rules):
    """finds final location of a part"""
    location = "in"
    while location not in "AR":
        location = eval_rule(part, rules[location])
    return location

def sum_accepted(parts, rules):
    """returns the sum of accepted values"""
    accepted = []
    rejected = []
    for part in parts:
        # could just be a total += sum here but I might
        # need this in part two
        if eval_part(part, rules) == "A":
            accepted.append(part)
        else:
            rejected.append(part)
    return sum(sum(part.values()) for part in accepted)

def find_new_range(old_range, constraint):
    """returns the range which passes, and the range which fails, returns 0 if no ranges pas"""
    key = constraint[0]
    comparison = constraint[1]
    value = int(constraint[2:])
    new_range = copy.deepcopy(old_range) 
    pass_through = copy.deepcopy(old_range)
    if comparison == "<":
        if old_range[key][1] < value:
            # new range is identical to old range
            return new_range, 0
        if old_range[key][0] > value:
            # new range has no possible values, everything passes thru
            return 0, pass_through
        new_range[key][1] = value - 1
        pass_through[key][0] = value
    else:
        if old_range[key][0] > value:
            # new range is identical to old range
            return new_range, 0
        if old_range[key][1] < value:
            # new range has no possible values, everything passes thru
            return 0, pass_through
        new_range[key][0] = value + 1
        pass_through[key][1] = value
    return new_range, pass_through

def total_possibilities(rules):
    """return the total number of possible accepted combinations"""
    total = 0
    start_range = {"x": [1,4000], "m": [1,4000], "a": [1,4000], "s": [1,4000]}
    queue = []
    queue.append((start_range, "in"))
    while queue:
        pass_through, rule_name = queue.pop()
        
        if pass_through == 0 or rule_name == "R":
            # no possibilities or rejected
            continue
        if rule_name == "A":
            # accepted
            total += prod(x[1] - x[0] + 1 for x in pass_through.values())
            continue
        
        rule_list = rules[rule_name]
        
        for rule in rule_list[:-1]:
            # find new ranges and put them in the queue
            new_range, pass_through = find_new_range(pass_through, rule[0])
            queue.append((new_range, rule[1]))
        
        queue.append((pass_through, rule_list[-1]))
    
    return total

if __name__ == "__main__":
    with open("inputs/day_19.txt") as f:
        rules, parts = get_info(f.read())
        total_accepted = sum_accepted(parts, rules)
        print(total_accepted, "< total accepted parts")
        possibilities = total_possibilities(rules)
        print(possibilities, "< number of total possibilites")
