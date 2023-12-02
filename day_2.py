import re

def sum_valid_games(games):
    red_cubes = re.findall(r"\d+(?= red)", games)
    green_cubes = re.findall(r"\d+(?= green)", games)
    blue_cubes = re.findall(r"\d+(?= blue)", games)
    red_is_valid = all(int(cubes) <= 12 for cubes in red_cubes)
    green_is_valid = all(int(cubes) <= 13 for cubes in green_cubes)
    blue_is_valid = all(int(cubes) <= 14 for cubes in blue_cubes)
    if red_is_valid and green_is_valid and blue_is_valid:
        return 1
    else:
        return 0

