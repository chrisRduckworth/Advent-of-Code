from day_13 import compare_mirrored

class TestCompareMirrored:
    def test_returns_true_for_symmetrical(self):
        pattern = "#..\n#.."
        k = 1

        assert compare_mirrored(pattern, k, "column") == True
        
        pattern = "##\n..\n.."
        
        assert compare_mirrored(pattern, k, "row") == True

    def test_returns_true_if_pattern_mirrors_around_column_k(self):
        pattern = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.""".splitlines()
        print(pattern)
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
