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

if __name__ == "__main__":
    with open("inputs/day_14.txt") as f:
        platform = f.read().splitlines()
        load = calc_load(platform)
        print(load, "< load")
