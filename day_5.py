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
    seeds = [int(seed) for seed in re.search(r"(?<=seeds: )(\d+ ?)+", almanac)[0].split(" ")]
    maps = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
    maps = {a_map: re.search(r"(?<=" + re.escape(a_map) + r" map:\n)(\d+ \d+ \d+(?:\n)?)+", almanac)[0].splitlines() for a_map in maps}
    
    soils = [find_new_value(maps["seed-to-soil"], seed) for seed in seeds]
    fertilizers = [find_new_value(maps["soil-to-fertilizer"], soil) for soil in soils]
    waters = [find_new_value(maps["fertilizer-to-water"], fertilizer) for fertilizer in fertilizers]
    lights = [find_new_value(maps["water-to-light"], water) for water in waters]
    temperatures = [find_new_value(maps["light-to-temperature"], light) for light in lights]
    humiditys = [find_new_value(maps["temperature-to-humidity"], temperature) for temperature in temperatures]
    locations = [find_new_value(maps["humidity-to-location"], humidity) for humidity in humiditys]
       
    return min(locations)
