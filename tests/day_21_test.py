from copy import deepcopy
from day_21 import total_steps, find_steps

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
