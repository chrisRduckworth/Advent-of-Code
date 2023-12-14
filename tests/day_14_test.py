from day_14 import move_rocks, calc_load

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
