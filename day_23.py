from graphlib import TopologicalSorter

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
