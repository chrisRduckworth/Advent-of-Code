import math

def find_minimum_heat_loss(heat_map):
    """Ooooh, this is my first time using Dijkstra"""
    # pad all sides with an inifinte value. This just
    # makes indexing easier
    heat_map.insert(0, [math.inf for n in range(len(heat_map[0]))])
    heat_map.append([math.inf for n in range(len(heat_map[0]))])
    heat_map = [[math.inf, *r, math.inf] for r in heat_map]

    # dictionary keys need to include position,
    # direction,
    # and number of steps in a straight line to get there
    unvisited = {}
    for x in range(len(heat_map[0])):
        for y in range(len(heat_map)):
            for direction in "NESW":
                for steps in range(1,4):
                    unvisited[((x,y), direction, steps)] = heat_map[1][1] if x == y == 1 else math.inf

    visited = {}
    current_node = ((1,1), "E", 1)
    direction_coords = {"N": (0,-1), "E": (1,0), "S":(0,1), "W":(-1,0)}
    directions = {"N": "NEW", "E": "NES", "S": "ESW", "W": "NSW"}
    
    while current_node[0] != (len(heat_map[0]) - 2, len(heat_map) - 2):
        print(current_node, unvisited[current_node])
        # find adjacent nodes
        adjacent_nodes = []
        for direction in directions[current_node[1]]:
            x = current_node[0][0] + direction_coords[direction][0]
            y = current_node[0][1] + direction_coords[direction][1]
            if current_node[1] != direction:
                node = ((x,y), direction, 1)
                if node in unvisited:
                    adjacent_nodes.append(node)
            elif current_node[2] < 3:
                node = ((x,y), direction, current_node[2] + 1)
                if node in unvisited:
                    adjacent_nodes.append(node)

        for node in adjacent_nodes:
            x, y = node[0]
            distance = unvisited[current_node] + heat_map[y][x]
            if distance < unvisited[node]:
                unvisited[node] = distance

        visited[current_node] = unvisited[current_node]
        del unvisited[current_node]
        current_node = min(unvisited, key=unvisited.get)

    return unvisited[current_node] - heat_map[1][1]

if __name__ == "__main__":
    with open("inputs/day_17.txt") as f:
        heat_map = f.read().splitlines()
        heat_map = [[int(x) for x in list(r)] for r in heat_map]
        min_heat_loss = find_minimum_heat_loss(heat_map)
        print(min_heat_loss, "< min heat loss")
