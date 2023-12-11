from day_11 import expand_space, sum_shortest_distances, find_distance

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

    def test_accepts_char_argument(self):
        image = ["...", ".#.", "..."]

        expanded_space = expand_space(image, "@")

        assert expanded_space == ["@@@@@", "@..@.", "@.#@.", "@@@@@", "@..@."]

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

    def test_accepts_space_size_argument(self):
        image = "..#\n...\n#.."

        distances = sum_shortest_distances(image, 9)

        assert distances == 22
        
        distances = sum_shortest_distances(image, 99)

        assert distances == 202
        
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
        distances = sum_shortest_distances(image, 9)

        assert distances == 1030

        distances = sum_shortest_distances(image, 99)

        assert distances == 8410

class TestFindDistance:
    def test_returns_distance_with_no_spaces(self):
        image = ["#..", "...", "..#"]
        
        distance = find_distance(image, 1, (0,0), (2,2))
         
        assert distance == 4
        
        image = ["..#","...","#.."]
         
        distance = find_distance(image, 1, (2,0), (0,2))
         
        assert distance == 4

    def test_returns_distances_in_straight_lines(self):
        image = ["#...#", ".....", "....."]

        distance = find_distance(image, 1, (0,0), (4, 0))

        assert distance == 4

        image = ["#...", "....", "....", "#..."]

        distance = find_distance(image, 1, (0,0), (0,3))

        assert distance == 3

    def test_returns_distance_with_spaces(self):
        image = ["#..","...","..#"]
        image = expand_space(image, "@")

        distance = find_distance(image, 10, (0,0), (3,3))
        
        assert distance == 24

        image = ["..#","...","#.."]
        image = expand_space(image, "@")

        distance = find_distance(image, 10, (3,0), (0,3))
        
        assert distance == 24

    def test_returns_distance_with_spaces_straight_lines(self):
        image = ["#...#", ".....", "....."]
        image = expand_space(image, "@")

        distance = find_distance(image, 10, (0,0), (7, 0))

        assert distance == 34

        image = ["#...", "....", "....", "#..."]
        image = expand_space(image, "@")

        distance = find_distance(image, 10, (0,0), (0,4))

        assert distance == 22
