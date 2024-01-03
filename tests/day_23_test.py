import pytest
from day_23 import generate_graph 

class TestGenerateGraph:
    def test_returns_dict_of_simple_graph(self):
        maze = """#.##
#..#
##.#""".splitlines()
        maze = [list(r) for r in maze]
        
        print(maze)

        graph = generate_graph(maze)

        assert graph == {(2,2): {(2,1)}, (2,1): {(1,1)}, (1,1): {(1,0)}}

    def test_returns_dict_with_slopes(self):
        maze = """#.###
#.>.#
#.#v#
#.>.#
###.#""".splitlines()
        maze = [list(r) for r in maze]

        graph = generate_graph(maze)

        assert graph == {
                (3,4): {(3,3)},
                (3,3): {(2,3), (3,2)},
                (2,3): {(1,3)},
                (1,3): {(1,2)},
                (1,2): {(1,1)},
                (3,2): {(3,1)},
                (3,1): {(2,1)},
                (2,1): {(1,1)},
                (1,1): {(1,0)}
                }


