import re

def find_new_value(map_values, in_value):
    """returns the corresponding value from the given map"""
    out_value = -1
    for map_value in map_values:
        out_start, in_start, range_length = [int(n) for n in map_value.split(" ")]
        if in_value in range(in_start, in_start + range_length):
            out_value = out_start + (in_value - in_start)
    if out_value == -1:
        out_value = in_value

    return out_value

def find_lowest_location_number(almanac):
    """returns the lowest location number from given seeds"""
    # retrieve seeds and maps from input strings
    seeds = [int(seed) for seed in re.search(r"(?<=seeds: )(\d+ ?)+", almanac)[0].split(" ")]
    maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    maps = {a_map: re.search(r"(?<=" + re.escape(a_map) + r" map:\n)(\d+ \d+ \d+(?:\n)?)+", almanac)[0].splitlines() for a_map in maps}
    
    # convert seeds to soils, fertilizers to waters, etc
    soils = [find_new_value(maps["seed-to-soil"], seed) for seed in seeds]
    fertilizers = [find_new_value(maps["soil-to-fertilizer"], soil) for soil in soils]
    waters = [find_new_value(maps["fertilizer-to-water"], fertilizer) for fertilizer in fertilizers]
    lights = [find_new_value(maps["water-to-light"], water) for water in waters]
    temperatures = [find_new_value(maps["light-to-temperature"], light) for light in lights]
    humiditys = [find_new_value(maps["temperature-to-humidity"], temperature) for temperature in temperatures]
    locations = [find_new_value(maps["humidity-to-location"], humidity) for humidity in humiditys]

    return min(locations)

def find_lowest_location_number_from_ranges(almanac):
    """returns the lowest location number from a given range of seeds"""
    # lets go backwards
    seed_ranges = [[int(r.split(" ")[0]), int(r.split(" ")[0]) + int(r.split(" ")[1])] for r in re.findall(r"\d+ \d+", almanac.splitlines()[0])]
    location = 0
    maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    maps = {a_map: re.search(r"(?<=" + re.escape(a_map) + r" map:\n)(\d+ \d+ \d+(?:\n)?)+", almanac)[0].splitlines() for a_map in maps}
    for a_map in maps:
        maps[a_map] = [" ".join(row.split(" ")[1::-1] + [row.split(" ")[2]]) for row in maps[a_map]]
    while True:
        humidity = find_new_value(maps["humidity-to-location"], location)
        temperature = find_new_value(maps["temperature-to-humidity"], humidity)
        light = find_new_value(maps["light-to-temperature"], temperature)
        water = find_new_value(maps["water-to-light"], light)
        fertilizer = find_new_value(maps["fertilizer-to-water"], water)
        soil = find_new_value(maps["soil-to-fertilizer"], fertilizer)
        seed = find_new_value(maps["seed-to-soil"], soil)
        # if seed in list of seeds
        for seed_range in seed_ranges:
            if seed_range[0] <= int(seed) < seed_range[1]:
                return location
        location += 1
        
if __name__ == "__main__":
    with open("inputs/day_5.txt") as f:
        almanac = f.read()
        min_location = find_lowest_location_number(almanac)
        print(min_location, " lowest location number")
        min_location_from_ranges = find_lowest_location_number_from_ranges(almanac)
        print(min_location_from_ranges, " lowest location number from ranges")
