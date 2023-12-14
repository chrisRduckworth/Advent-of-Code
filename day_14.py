def move_rocks(platform):
    for y, row in enumerate(platform[1:]):
        for x, space in enumerate(row):
            if space == "O":
                if platform[y][x] == ".":
                    platform[y] = platform[y][:x] + "O" + platform[y][x+1:]
                    platform[y+1] = platform[y + 1][:x] + "." + platform[y + 1][x+1:]
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
