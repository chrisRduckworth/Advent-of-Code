from day_23 import generate_graph, longest_path

class TestGenerateGraph:
    def test_returns_dict_of_simple_graph(self):
        maze = """#.##
#..#
##.#""".splitlines()
        maze = [list(r) for r in maze]

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

class TestLongestPath:
    def test_returns_length_of_single_path(self):
        maze = """#.##
#..#
##.#""".splitlines()
        maze = [list(r) for r in maze]

        graph = generate_graph(maze)

        longest = longest_path(graph, (len(maze[0]) - 2, len(maze) - 1))

        assert longest == 3

    def test_returns_length_of_complex_path(self):
        maze = """#.###
#.>.#
#.#v#
#.>.#
###.#""".splitlines()
        maze = [list(r) for r in maze]

        graph = generate_graph(maze)

        longest = longest_path(graph, (len(maze[0]) - 2, len(maze) - 1))

        assert longest == 6

    def test_returns_length_for_big_maze(self):
        maze = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".splitlines()

        maze = [list(r) for r in maze]

        graph = generate_graph(maze)

        longest = longest_path(graph, (len(maze[0]) - 2, len(maze) - 1))

        assert longest == 94
