from day_12 import create_all_springs, filter_matching_springs, filter_broken_springs, sum_possibilities, is_valid_possibility, find_possibilities

class TestCreateAllSprings:
    def test_returns_all_possible_springs(self):
        length = 1 

        assert create_all_springs(length) == [".", "#"]

        length = 2

        assert create_all_springs(length) == ["..", ".#", "#.", "##"]

        length = 10

        assert len(create_all_springs(length)) == 2 ** length

class TestFilterMatchingSprings:
    def test_returns_spring_if_no_unknowns(self):
        possible_springs = create_all_springs(2)
        spring = ".."

        assert filter_matching_springs(spring, possible_springs) == [".."]

    def test_returns_all_springs_if_all_unknowns(self):
        possible_springs = create_all_springs(2)
        spring = "??"

        assert filter_matching_springs(spring, possible_springs) == possible_springs

    def test_returns_springs_that_match(self):
        possible_springs = create_all_springs(3)
        spring = "?.?"

        matching_springs = filter_matching_springs(spring, possible_springs)

        assert len(matching_springs) == 4
        assert all(s[1] == "." for s in matching_springs)

class TestFilterBrokenSprings:
    def test_returns_no_springs_if_none_match(self):
        possible_springs = create_all_springs(2)
        spring = ".."
        matching_springs = filter_matching_springs(spring, possible_springs)

        valid_springs = filter_broken_springs((1), possible_springs)

        assert valid_springs == []

    def test_returns_list_of_springs_that_are_valid(self):
        possible_springs = create_all_springs(12)
        spring = "?###????????"
        matching_springs = filter_matching_springs(spring, possible_springs)

        valid_springs = filter_broken_springs((3,2,1), matching_springs)

        assert len(valid_springs) == 10

class TestSumPossibilities:
    def test_returns_possibilities_for_one_springs(self):
        springs = "?###???????? 3,2,1"

        possibilities = sum_possibilities(springs)

        assert possibilities == 10

    def test_returns_sum_for_multiple_springs(self):
        springs = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
        
        possibilities = sum_possibilities(springs)

        assert possibilities == 21

class TestIsValidPossibility:
    def test_returns_false_if_spring_is_not_possible(self):
        spring = "?.."
        damaged_tuple = (1,1)
        
        assert is_valid_possibility(spring, damaged_tuple) == False

    def test_returns_true_if_spring_is_possible(self):
        spring = "??.?"
        spring_2 = "???.###????.###????.###????.###????.###"
        damaged_tuple = (1,1)
        damaged_tuple_2 = (2,)
        damaged_tuple_3 = (1,)
        damaged_tuple_4 = (1,1,3,1,1,3,1,1,3,1,1,3,1,1,3)

        assert is_valid_possibility(spring, damaged_tuple)
        assert is_valid_possibility(spring, damaged_tuple_2)
        assert is_valid_possibility(spring, damaged_tuple_3)
        assert is_valid_possibility(spring_2, damaged_tuple_4)

class TestFindPossibilities:
    def test_returns_zero_if_none_possible(self):
        spring = "?.?."
        damaged_tuple = (3,)

        possibilities = find_possibilities(spring, damaged_tuple)
        
        assert possibilities == 0

    def test_returns_1_if_only_one_possible(self):
        spring = ".??."
        spring_2 = "???.###"
        spring_3 = "?#?#?#?#?#?#?#?"
        spring_4 = "????.#...#..."
        damaged_tuple = (2,)
        damaged_tuple_2 = (1,1,3)
        damaged_tuple_3 = (1,3,1,6)
        damaged_tuple_4 = (4,1,1)

        possibilities = find_possibilities(spring, damaged_tuple)
        possibilities_2 = find_possibilities(spring_2, damaged_tuple_2)
        possibilities_3 = find_possibilities(spring_3, damaged_tuple_3)
        possibilities_4 = find_possibilities(spring_4, damaged_tuple_4)

        assert possibilities == 1 
        assert possibilities_2 == 1 
        assert possibilities_3 == 1 
        assert possibilities_4 == 1 
        
    def test_returns_number_of_possibilities(self):
        spring = ".??..??...?##."
        spring_2 = "????.######..#####."
        spring_3 = "?###????????"
        damaged_tuple = (1,1,3)
        damaged_tuple_2 = (1,6,5)
        damaged_tuple_3 = (3,2,1)

        possibilities = find_possibilities(spring, damaged_tuple)
        possibilities_2 = find_possibilities(spring_2, damaged_tuple_2)
        possibilities_3 = find_possibilities(spring_3, damaged_tuple_3)

        assert possibilities == 4
        assert possibilities_2 == 4
        assert possibilities_3 == 10

    def test_works_on_long_springs(self):
        spring = "?".join(["?###????????"] * 5)
        damaged_tuple = (3,2,1) * 5
        print(spring, damaged_tuple)

        possibilities = find_possibilities(spring, damaged_tuple)

        assert possibilities == 506250
