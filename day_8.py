import re, math

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

    # we will find the route each location takes to a Z
    # before it loops back on itself
    # then we can use the lowest common multiple to find
    # the length of all routes running simultaneously

    lengths_of_loops = []
    for location in locations:
        # we check loops twice because there are 2 cases, either
        # we enter on a L or on a R. It's possible the lengths are 
        # different (they aren't for my input but I don't know if 
        # that's generally true)
        loop_indices = []
        steps = 0
        destination = ""
        while len(loop_indices) < 3:
            direction = directions[steps % len(directions)]
            if direction == "L":
                location = network[location][0]
            else:
                location = network[location][1]
            steps += 1
            # if we're at a z, then that's where we end up
            if location[2] == "Z" and len(loop_indices) == 0:
                destination = location
            # keep the number of steps taken so we can count the length of 
            # the loop
            if location == destination:
                loop_indices.append(steps)
        
        if loop_indices[2] - loop_indices[1] != loop_indices[1] - loop_indices[0]:
            # just in case the loops aren't the same length
            raise ValueError("loop lengths aren't the same :(")
        
        lengths_of_loops.append(loop_indices[2] - loop_indices[1])
        
    return math.lcm(*lengths_of_loops)

if __name__ == "__main__":
    with open("inputs/day_8.txt") as f:
        maps = f.read()
        steps = find_steps(maps)
        print(steps, "< steps")
        ghost_steps = find_ghost_steps(maps)
        print(ghost_steps, "< ghost steps")
