import re

def find_steps(maps):
    maps = maps.splitlines()
    directions = maps[0]
    network = {l[:3]: re.findall(r"\w+", l[3:]) for l in maps[2:]}

    location = "AAA"
    i = 0

    while location != "ZZZ":
        direction = directions[i % len(directions)]
        if direction == "L":
            location = network[location][0]
        else:
            location = network[location][1]
        i += 1
        
    return i

