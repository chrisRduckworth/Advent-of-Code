import numpy as np

def move_rocks(platform, direction="N"):
    rotation = {"N": 0, "E":1, "S": 2, "W": 3}
    platform = np.rot90([list(row) for row in platform], rotation[direction])

    for y, row in enumerate(platform[1:]):
        for x, space in enumerate(row):
            if space == "O":
                if platform[y][x] == ".":
                    platform[y][x] = "O" 
                    platform[y+1][x] = "."
    
    platform = np.rot90(platform, 4 - rotation[direction])
    platform = ["".join(row) for row in platform]
    return platform

def calc_load(platform):
    for i in range(len(platform) - 1):
        platform = move_rocks(platform)
    load = 0
    for i, row in enumerate(platform[::-1]):
        load += (i + 1) * row.count("O")
    return load

def spin_platform(platform):
    for i in range(len(platform) - 1):
        platform = move_rocks(platform)
    for i in range(len(platform[0]) - 1):
        platform = move_rocks(platform, "W")
    for i in range(len(platform) - 1):
        platform = move_rocks(platform, "S")
    for i in range(len(platform[0]) - 1):
        platform = move_rocks(platform, "E")
    return platform

def load_after_billion(platform):
    platforms = [platform]
    for i in range(1, 1000000001):
        print(i)
        platform = spin_platform(platform)
        if platform in platforms:
            platforms.append(platform)
            looping_platform = platform
            break
        platforms.append(platform)
    loop_start = platforms.index(looping_platform)
    loop_end = platforms.index(looping_platform, loop_start + 1)
    loop_length = loop_end - loop_start
    position_after_billion = loop_start + ((1000000000 - loop_start) % loop_length)

    final_platform = platforms[position_after_billion]

    load = 0
    for i, row in enumerate(final_platform[::-1]):
        load += (i + 1) * row.count("O")
    return load

if __name__ == "__main__":
    with open("inputs/day_14.txt") as f:
        platform = f.read().splitlines()
        load = calc_load(platform)
        print(load, "< load")
        load_later = load_after_billion(platform)
        print(load_later, "< load after a billion spins")
