import re

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

if __name__ == "__main__":
    with open("inputs/day_19.txt") as f:
        rules, parts = get_info(f.read())
        total_accepted = sum_accepted(parts, rules)
        print(total_accepted, "< total accepted parts")
