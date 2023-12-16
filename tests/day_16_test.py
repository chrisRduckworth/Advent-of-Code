from day_16 import is_moving_to_edge, find_energized_tiles, find_optimal_position

class TestIsMovingToEdge:
    def test_returns_false_if_inside(self):
        position = (5,5)
        dimensions = (10,10)

        for d in "NESW":
            assert not is_moving_to_edge(position, d, dimensions)
        
    def test_returns_false_if_moving_inside_when_on_edge(self):
        for x in range(1, 9):
            for d in "ESW":
                assert not is_moving_to_edge((x,0), d, (10,10))
        
        for x in range(1, 9):
            for d in "NEW":
                assert not is_moving_to_edge((x,9), d, (10,10))
        
        for y in range(1, 9):
            for d in "NSW":
                assert not is_moving_to_edge((9,y), d, (10,10))
    
        for y in range(1, 9):
            for d in "NES":
                assert not is_moving_to_edge((0,y), d, (10,10))
                
    def test_returns_true_if_moving_off_north(self):
        dimensions = (10,10)
        direction = "N"

        for x in range(10):
            assert is_moving_to_edge((x,0), direction, dimensions)

    def test_returns_true_if_moving_off_south(self):
        dimensions = (10,10)
        direction = "S"

        for x in range(10):
            assert is_moving_to_edge((x,9), direction, dimensions)

    def test_returns_true_if_moving_off_east(self):
        dimensions = (10,10)
        direction = "E"

        for y in range(10):
            assert is_moving_to_edge((9,y), direction, dimensions)

    def test_returns_true_if_moving_off_west(self):
        dimensions = (10,10)
        direction = "W"

        for y in range(10):
            assert is_moving_to_edge((0,y), direction, dimensions)

class TestFindEnergizedTiles:
    def test_returns_number_of_energized_tiles(self):
        pattern = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()
        pattern = [list(row) for row in pattern]

        assert find_energized_tiles(pattern) == 46

class TestFindOptimalPosition:
    def test_returns_tiles_for_optimal_position(self):
        pattern = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".splitlines()
        pattern = [list(row) for row in pattern]

        assert find_optimal_position(pattern) == 51
