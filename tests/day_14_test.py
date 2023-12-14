from day_14 import move_rocks, calc_load, spin_platform, load_after_billion

class TestMoveRocks:
    def test_doesnt_move_top_row(self):
        platform = ["OOO", "..."]

        tilted_platform = move_rocks(platform)

        assert tilted_platform == ["OOO", "..."]

    def test_doesnt_move_into_cubes(self):
        platform = [".#.", ".O."]

        tilted_platform = move_rocks(platform)

        assert tilted_platform == [".#.", ".O."]

    def test_doesnt_move_into_rocks(self):
        platform = ["O..", "O.."]

        tilted_platform = move_rocks(platform)

        assert tilted_platform == ["O..", "O.."]

    def test_moves_rocks_one_space(self):
        platform = ["...", "O.O"]

        tilted_platform = move_rocks(platform)

        assert tilted_platform == ["O.O", "..."]

    def test_multiple_lines(self):
        platform = ["O#..", "O.O#", ".OOO", "..O."]

        tilted_platform = move_rocks(platform)

        assert tilted_platform == ["O#O.", "OOO#", "..OO", "...."]

    def test_moves_in_other_directions(self):
        platform = ["O#..", "O.O#", ".OOO", "..O."]

        tilted_south = move_rocks(platform.copy(), "S")
        tilted_east = move_rocks(platform.copy(), "E")
        tilted_west = move_rocks(platform.copy(), "W")

        assert tilted_south == [".#..", "O.O#", "O.O.", ".OOO"]
        assert tilted_east == ["O#..", ".OO#", ".OOO", "...O"]
        assert tilted_west == ["O#..", "OO.#", "OOO.", ".O.."]

class TestCalcLoad:
    def test_calculates_load_on_platform(self):
        platform = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
""".splitlines()
        
        load = calc_load(platform)

        assert load == 136

class TestSpinPlatform:
    def test_spins_a_platform(self):
        platform = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()
        
        expected = """.....#....
....#...O#
...OO##...
.OO#......
.....OOO#.
.O#...O#.#
....O#....
......OOOO
#...O###..
#..OO#....""".splitlines()
        
        spun = spin_platform(platform)

        assert spun == expected

class TestLoadAfterBillion:
    def test_returns_load(self):
        platform = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()
        
        load = load_after_billion(platform)

        assert load == 64
