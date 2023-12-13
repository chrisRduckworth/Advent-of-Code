from day_13 import compare_mirrored, make_notes

class TestCompareMirrored:
    def test_returns_true_for_symmetrical(self):
        pattern = [["#",".","."],["#",".","."]]
        k = 1

        assert compare_mirrored(pattern, k, "row") == True
        
        pattern = [["#","#"], [".", "."], [".","."]] 
        
        assert compare_mirrored(pattern, k, "column") == True

    def test_returns_true_if_pattern_mirrors_around_column_k(self):
        pattern = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()
        
        pattern = [list(row) for row in pattern]
        k = 5

        assert compare_mirrored(pattern, k, "column") == True
        pass

    def test_returns_true_if_pattern_mirrors_around_row_k(self):
        pattern = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()
        pattern = [list(row) for row in pattern]
        k = 4

        assert compare_mirrored(pattern, k, "row") == True

    def test_returns_false_if_pattern_does_not_mirror_column(self):
        pattern = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()
        pattern = [list(row) for row in pattern]
        k = 1

        assert compare_mirrored(pattern, k, "column") == False
    
    def test_returns_false_if_pattern_does_not_mirror_row(self):
        pattern = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()
        pattern = [list(row) for row in pattern]
        k = 6

        assert compare_mirrored(pattern, k, "row") == False

class TestMakeNotes:
    def test_returns_0_if_no_symmetry(self):
        pattern = [[".","#"], ["#","."]]

        notes = make_notes(pattern)

        assert notes == 0

    def test_adds_one_for_each_symmetrical_column(self):
        pattern = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()
        pattern = [list(row) for row in pattern]

        notes = make_notes(pattern)

        assert notes == 5

    def test_adds_100_for_each_symmetrical_row(self):
        pattern = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()
        pattern = [list(row) for row in pattern]

        notes = make_notes(pattern)

        assert notes == 400 
    
    def test_adds_columns_and_rows(self):
        pattern = """....\n....\n....\n####\n####""".splitlines()

        pattern = [list(row) for row in pattern]

        notes = make_notes(pattern)

        assert notes == 506 
