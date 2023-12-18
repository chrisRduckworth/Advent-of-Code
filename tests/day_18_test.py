from day_18 import dig_trench

class TestDigTrench:
    def test_returns_digs_single_instruction(self):
        instructions = [["R", 6, "(#70c710)"]]

        trenches = dig_trench(instructions)

        assert trenches == [["#","#","#","#","#","#","#"]]

        instructions = [["D", 5, "(#0dc571)"]]

        trenches = dig_trench(instructions)

        assert trenches == [["#"],["#"],["#"],["#"],["#"],["#"]]

        instructions = [["L", 2, "(#5713f0)"]]
        
        trenches = dig_trench(instructions)

        assert trenches == [["#","#","#"]]

        instructions = [["U", 3, "(#a77fa3)"]]
        
        trenches = dig_trench(instructions)

        assert trenches == [["#"],["#"],["#"],["#"],]

    def test_handles_multiple_instructions(self):
        instructions = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".splitlines()
        instructions = [[i.split()[0], int(i.split()[1]), i.split()[2]] for i in instructions]
        expected = """#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######""".splitlines()
        expected = [list(r) for r in expected]

        trenches = dig_trench(instructions)

        assert trenches == expected
