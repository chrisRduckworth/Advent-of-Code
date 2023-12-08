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

def find_ghost_steps(maps):
    maps = maps.splitlines()
    directions = maps[0]
    network = {l[:3]: re.findall(r"\w+", l[3:]) for l in maps[2:]}

    locations = [loc for loc in network if loc[2] == "A"]
    i = 0

    while not all(loc[2] == "Z" for loc in locations):
        direction = directions[i % len(directions)]
        for index, location in enumerate(locations):
            if direction == "L":
                location = network[location][0]
            else:
                location = network[location][1]
            locations[index] = location
        i += 1
        
    return i

if __name__ == "__main__":
    with open("inputs/day_8.txt") as f:
        maps = f.read()
        steps = find_steps(maps)
        print(steps, "< steps")
