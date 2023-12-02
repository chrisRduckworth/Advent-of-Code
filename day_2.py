import re

def sum_valid_games(games):
    games = games.splitlines()
    total = 0
    for game in games:
        game_id = re.search(r"(?<=Game )\d+", game)[0]
        red_cubes = re.findall(r"\d+(?= red)", game)
        green_cubes = re.findall(r"\d+(?= green)", game)
        blue_cubes = re.findall(r"\d+(?= blue)", game)
        red_is_valid = all(int(cubes) <= 12 for cubes in red_cubes)
        green_is_valid = all(int(cubes) <= 13 for cubes in green_cubes)
        blue_is_valid = all(int(cubes) <= 14 for cubes in blue_cubes)
        if red_is_valid and green_is_valid and blue_is_valid:
            total += int(game_id)
    return total

if __name__ == "__main__":
    with open("inputs/day_2.txt") as f:
        games = f.read()
        total = sum_valid_games(games)
        print(total)
