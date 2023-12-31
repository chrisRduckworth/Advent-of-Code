from graphlib import TopologicalSorter
import sys

def generate_graph(maze):
    """generates a dictionary of nodes and their predocessors"""
    maze = [["#"] * len(maze[0]), *maze, ["#"] * len(maze[0])]
    graph = {}

    def rec(node, prev):
        n_x, n_y = node

        if (n_x, n_y - 1) not in graph:
            graph[(n_x, n_y - 1)] = set()

        for dir in [(1,0, ">"), (-1,0, "<"), (0,1, "v"), (0,-1, "^")]:
            x, y, slope = (n_x + dir[0], n_y + dir[1], dir[2])

            if maze[y][x] in [".", slope] and (x,y) != prev:
                graph[(n_x, n_y - 1)].add((x, y - 1))
                rec((x, y), node)

    rec((1,1), (1,0))

    reversed = {}

    for node, adj in graph.items():
        for next in adj:
            if next not in reversed:
                reversed[next] = set()
            reversed[next].add(node)

    return reversed

def longest_path(graph, end):
    ordered = tuple(TopologicalSorter(graph).static_order())
    
    distances = {}
    distances[(1,0)] = 0

    for node in ordered[1:]:
        distances[node] = distances[max(graph[node], key=distances.get)] + 1

    return distances[end]

# part 2:
# i can't see a way to do this outside of brute force which is MESSY

def part_2(maze):
    """returns the longest path ignoring slopes"""
    maze = [["#"] * len(maze[0]), *maze, ["#"] * len(maze[0])]

    distances = {}
    optimal = {}
    queue = [(1, 1, [])]

    while queue:
        x, y, path = queue.pop(0)
        if (x,y) in path or maze[y][x] == "#":
            continue

        distances[(x,y)] = len(path)
        path = [*path, (x,y)]
        optimal[(x,y)] = path

        for d_x, d_y in [(1,0), (-1,0), (0,1), (0,-1)]:
            queue.append((x + d_x, y + d_y, path))

    return distances[(len(maze[0]) - 2), len(maze) - 2]

if __name__ == "__main__":
    with open("inputs/day_23.txt") as f:
        maze = [list(r) for r in f.read().splitlines()]
        sys.setrecursionlimit(10000)
        graph = generate_graph(maze)
        longest = longest_path(graph, (len(maze[0]) - 2, len(maze) - 1))
        print(longest, "< longest possible path")
