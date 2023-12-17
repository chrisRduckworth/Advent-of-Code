from day_17 import find_minimum_heat_loss, part_two

class TestFindMinimumHeatLoss:
    def test_returns_min_heat(self):
        heat_map = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".splitlines()
        heat_map = [[int(x) for x in list(r)] for r in heat_map]

        assert find_minimum_heat_loss(heat_map) == 102

class TestPartTwo:
    def test_returns_min_heat(self):
        heat_map = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".splitlines()
        heat_map = [[int(x) for x in list(r)] for r in heat_map]

        assert part_two(heat_map) == 94

        heat_map ="""111111111111
999999999991
999999999991
999999999991
999999999991""".splitlines()
        heat_map = [[int(x) for x in list(r)] for r in heat_map]

        assert part_two(heat_map) == 71
