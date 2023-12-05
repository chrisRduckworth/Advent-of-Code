from day_5 import find_lowest_location_number, find_new_value, find_lowest_location_number_from_ranges

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class TestFindNewValue:
    def test_returns_corresponding_value_in_map(self):
        map_values = ["50 98 2", "52 50 48"]
        in_value = 79
        
        out_value = find_new_value(map_values, in_value)

        assert out_value == 81

    def test_returns_same_value_if_not_in_map(self):
        map_values = ["50 98 2", "52 50 48"]
        in_value = 48
        
        out_value = find_new_value(map_values, in_value)

        assert out_value == 48

    def test_swapping_map_columns_reverses_direction(self):
        map_values = ["98 50 2", "50 52 48"]

        in_value = 81

        out_value = find_new_value(map_values, in_value)

        assert out_value == 79

        # no for a number not in the map
        in_value = 48

        out_value = find_new_value(map_values, in_value)

        assert out_value == 48
        
class TestFindLowestLocationNumber:
    def test_returns_lowest_location_number_for_one_seed(self):
        almanac = "seeds: 79\n" + "\n".join(test_input.splitlines()[1:])

        min_location = find_lowest_location_number(almanac)
    
        assert min_location == 82

    def test_returns_lowest_location_number_for_multiple_seeds(self):
        almanac = test_input

        min_location = find_lowest_location_number(almanac)

        assert min_location == 35

class TestFindLowestLocationNumberFromRanges:
    def test_returns_lowest_location(self):
        almanac = test_input

        min_location = find_lowest_location_number_from_ranges(almanac)

        assert min_location == 46
