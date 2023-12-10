from day_10 import increment_position, find_start_coordinates, find_route, furthest_point, enclosed_tiles, mark_adjacent_tiles
import pytest

class TestIncrementPosition:
    def test_returns_tuple_of_increment(self):
        assert increment_position("|", "N") == (0, 1)
        assert increment_position("|", "S") == (0, -1)
        
        assert increment_position("-", "W") == (1, 0)
        assert increment_position("-", "E") == (-1, 0)
        
        assert increment_position("L", "N") == (1, 0)
        assert increment_position("L", "E") == (0, -1)

        assert increment_position("J", "N") == (-1, 0)
        assert increment_position("J", "W") == (0, -1)

        assert increment_position("7", "W") == (0, 1)
        assert increment_position("7", "S") == (-1, 0)

        assert increment_position("F", "E") == (0, 1)
        assert increment_position("F", "S") == (1, 0)

    def test_raises_error_if_given_ground(self):
        with pytest.raises(ValueError) as exc_info:
            increment_position(".", "S")
        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == "input must be pipe"

    def test_raises_error_if_given_invalid_direction(self):
        with pytest.raises(ValueError) as exc_info:
            increment_position("-", "S")
        assert exc_info.type is ValueError
        assert exc_info.value.args[0] == "invalid direction"

class TestFindStartCoordinates:
    def test_finds_start_coordinates(self):
        maze = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]

        start_coords = find_start_coordinates(maze)

        assert start_coords == (1, 1)

class TestFindRoute:
    def test_finds_route(self):
        maze = ["-L|F7", "7S-7|", "L|7||", "-L-J|", "L|-JF"]
        expected_route = [(1,1), (1,2), (1,3), (2,3), (3,3), (3,2), (3,1), (2,1)]
        assert find_route(maze, (0,1)) == expected_route

class TestFurthestPoints:
    def test_returns_distance_to_furthest_point(self):
        maze = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
        maze_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
        
        assert furthest_point(maze, (0,1)) == 4
        assert furthest_point(maze_2, (0,1)) == 8

class TestMarkAdjacentTiles:
    def test_marks_adjacent_tiles(self):
        maze = ["...", ".-.", "..."]
        
        north = mark_adjacent_tiles(maze, (1,1), "N")
        south = mark_adjacent_tiles(maze, (1,1), "S")
        east = mark_adjacent_tiles(maze, (1,1), "E")
        west = mark_adjacent_tiles(maze, (1,1), "W")

        expected_north = ["...", "I-O", "..."]
        expected_south = ["...", "O-I", "..."]
        expected_east = [".I.", ".-.", ".O."]
        expected_west = [".O.", ".-.", ".I."]

        assert north == expected_north
        assert south == expected_south
        assert east == expected_east
        assert west == expected_west

    def test_ignores_pipes(self):
        maze = [".|.", "F-J", ".-."]
        
        north = mark_adjacent_tiles(maze, (1,1), "N")
        south = mark_adjacent_tiles(maze, (1,1), "S")
        east = mark_adjacent_tiles(maze, (1,1), "E")
        west = mark_adjacent_tiles(maze, (1,1), "W")

        assert north == maze
        assert south == maze
        assert east == maze
        assert west == maze

    def test_works_at_edges(self):
        maze = ["-..", "..."]

        north = mark_adjacent_tiles(maze, (0,0), "N")
        east = mark_adjacent_tiles(maze, (0,0), "E")

        expected_north = ["-O.", "..."]
        expected_east = ["-..", "O.."]

        assert north == expected_north
        assert east == expected_east

    def test_does_not_mutate_maze(self):
        maze = ["...", ".-.", "..."]

        mark_adjacent_tiles(maze, (1,1), "N")

        assert maze == ["...", ".-.", "..."]

