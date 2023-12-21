from day_21 import total_steps

class TestTotalSteps:
    def test_returns_0_when_no_options(self):
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
