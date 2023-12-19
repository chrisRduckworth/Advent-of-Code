import re

def get_info(system):
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
