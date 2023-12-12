from day_12 import create_all_springs, filter_matching_springs, filter_broken_springs, sum_possibilities

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
