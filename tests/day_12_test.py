from day_12 import create_all_springs, filter_matching_springs, sum_possibilities

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
