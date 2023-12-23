from copy import deepcopy
from day_21 import total_steps, find_steps, find_endings, find_all_endings, brute_force

class TestTotalSteps:
    def skip_test_returns_0_when_no_options(self):
        garden = [["S"]]

        steps = total_steps(garden, 10)
        
        assert steps == 0

    def test_returns_number_of_steps(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        steps = total_steps(garden, 6)
        
        assert steps == 16

class TestFindSteps:
    def test_does_not_mutate_original(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]
        expected = deepcopy(garden)

        find_steps(garden, (0,0))

        assert garden == expected
        
    def test_returns_0_for_simple_array(self):
        garden = [["S"]]

        steps = find_steps(garden, (0,0))

        assert steps == [[0]]

    def test_returns_distances_from_center(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        expected = """abcdcba989a
9abcd###7#b
8###e##56#a
76#4#234#89
6543#1#5678
7##210####9
8##32#678#a
7654345##cb
8##5#5####c
9##67##c##d
a98789abcde
""".splitlines()
        expected = [["#" if x == "#" else int(x, base=16) for x in list(r)] for r in expected]

        steps = find_steps(garden, (5,5))

        assert steps == expected

    def test_returns_distances_from_edge(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        expected = """fedcba98765
gfedc###8#4
h###d##67#3
gf#d#765#32
fedc#8#4321
g##ba9####0
h##cb#fgh#1
gfedcde##32
h##e#e####3
g##dc##9##4
fedcba98765
""".splitlines()
        expected = [["#" if x == "#" else int(x, base=20) for x in list(r)] for r in expected]

        steps = find_steps(garden, (10,5))

        assert steps == expected

    def test_returns_distances_from_corner(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        expected = """kjihgfedcba
jkjih###d#9
i###i##bc#8
hg#e#cba#87
gfed#d#9876
f##cde####5
e##bc#efg#4
dcbabcd##43
c##9#d####2
b##87##4##1
a9876543210""".splitlines()

        expected = [["#" if x == "#" else int(x, base=30) for x in list(r)] for r in expected]

        steps = find_steps(garden, (10,10))

        assert steps == expected

    def test_accepts_optional_initial_step_argument(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        expected = """6789abcdefg
56789###f#h
4###a##de#i
34#6#abc#gh
2345#9#defg
1##678####h
2##78#abc#i
3456789##kj
4##7#9####i
5##89##e##h
6789abcdefg""".splitlines()

        expected = [["#" if x == "#" else int(x, base=30) for x in list(r)] for r in expected]

        steps = find_steps(garden, (0,5), 1)

        assert steps == expected

class TestFindEndings:
    def test_returns_number_of_even_endings(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        garden = find_steps(garden, (5,5))

        valid_endings = find_endings(garden, True)

        assert valid_endings == 42

    def test_returns_number_of_odd_endings(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        garden = find_steps(garden, (10,5))

        valid_endings = find_endings(garden, False)

        assert valid_endings == 42

    def test_only_counts_number_within_distance_even(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        garden = find_steps(garden, (10,5))

        valid_endings = find_endings(garden, True, 7)

        assert valid_endings == 11

    def test_only_counts_number_within_distance_odd(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()
        garden = [list(r) for r in garden]

        garden = find_steps(garden, (10,5))

        valid_endings = find_endings(garden, False, 7)

        assert valid_endings == 14
class TestBruteForce:
    def test_returns_endings(self):
        garden = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
""".splitlines()
        garden = [list(r) for r in garden]

        assert brute_force(garden, 6) == 16
        assert brute_force(garden, 10) == 50
        assert brute_force(garden, 50) == 1594
        assert brute_force(garden, 100) == 6536
        assert brute_force(garden, 500) == 167004
        # assert brute_force(garden, 1000) == 668697
        # assert brute_force(garden, 5000) == 16733044
