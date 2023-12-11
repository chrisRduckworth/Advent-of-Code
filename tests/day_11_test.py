from day_11 import expand_space, sum_shortest_distances

class TestExpandSpace:
    def test_returns_input_if_no_empty_space(self):
        image = ["#..", ".#.", "..#"]

        expanded_space = expand_space(image)

        assert expanded_space == ["#..", ".#.", "..#"]

    def test_expands_rows(self):
        image = ["...", "###", "..."]

        expanded_space = expand_space(image)

        assert expanded_space == ["...", "...", "###", "...", "..."]

    def test_expands_columns(self):
        image = [".#.", ".#.", ".#."]

        expanded_space = expand_space(image)
        
        assert expanded_space == ["..#..", "..#..", "..#.."]

    def test_expands_rows_and_columns(self):
        image = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

        expected_image = """....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......""".splitlines()

        expanded_space = expand_space(image)

        assert expanded_space == expected_image

class TestSumShortestDistance:
    def test_returns_zero_for_no_or_one_galaxy(self):
        image = "...\n...\n..."

        distances = sum_shortest_distances(image)

        assert distances == 0

        image = "...\n.#.\n..."

        distances = sum_shortest_distances(image)

        assert distances == 0

    def test_returns_distance_for_two_galaxies(self):
        image = "..#\n...\n#.."

        distances = sum_shortest_distances(image)

        assert distances == 6

    def test_returns_sum_of_distances(self):
        image = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
        
        distances = sum_shortest_distances(image)

        assert distances == 374
