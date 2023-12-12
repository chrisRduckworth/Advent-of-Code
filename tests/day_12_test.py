from day_12 import create_all_springs, filter_matching_springs, sum_possibilities

class TestCreateAllSprings:
    def test_returns_all_possible_springs(self):
        length = 1 

        assert create_all_springs(length) == [".", "#"]

        length = 2

        assert create_all_springs(length) == ["..", ".#", "#.", "##"]

        length = 10

        assert len(create_all_springs(length)) == 2 ** length

    
